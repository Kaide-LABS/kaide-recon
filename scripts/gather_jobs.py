import asyncio
import sys
import os
import datetime
from pathlib import Path
from playwright.async_api import async_playwright

async def gather(founder: str, company: str, raw_dir: str, careers_url: str):
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (kaide-recon)")
        page = await context.new_page()
        
        try:
            print(f"Navigating to {careers_url}...")
            await page.goto(careers_url, timeout=30000)
            # Wait a bit for JS to load jobs
            await asyncio.sleep(5)
            content = await page.inner_text("body")
        except Exception as e:
            print(f"Error gathering jobs from {careers_url}: {e}")
            raise
        finally:
            await browser.close()

    header = f"# Company Jobs — {company}\n\n"
    header += f"**Captured:** {timestamp}\n"
    header += f"**Source URL:** {careers_url}\n\n"
    header += "---\n\n"
    
    out_file = Path(raw_dir) / "company_jobs.md"
    out_file.write_text(header + content, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python scripts/gather_jobs.py '<founder>' '<company>' '<raw_dir>' '<careers_url>'")
        sys.exit(2)
    asyncio.run(gather(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
