import asyncio
import sys
import os
import datetime
from pathlib import Path
from playwright.async_api import async_playwright

async def gather(founder: str, company: str, raw_dir: str):
    # Derive YC company slug from company name - simple heuristic for now
    # In a real run, this might need manual override or better search
    company_slug = company.lower().replace(" ", "-")
    url = f"https://www.ycombinator.com/companies/{company_slug}"
    
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (kaide-recon)")
        page = await context.new_page()
        
        try:
            response = await page.goto(url, timeout=30000)
            if response.status == 404:
                content = "No YC page found for this company."
            else:
                # Extract text aggressively
                content = await page.inner_text("body")
        except Exception as e:
            print(f"Error gathering YC page {url}: {e}")
            raise
        finally:
            await browser.close()

    header = f"# YC Page — {company}\n\n"
    header += f"**Captured:** {timestamp}\n"
    header += f"**Source URL:** {url}\n\n"
    header += "---\n\n"
    
    out_file = Path(raw_dir) / "yc_page.md"
    out_file.write_text(header + content, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python scripts/gather_yc.py '<founder>' '<company>' '<raw_dir>'")
        sys.exit(2)
    asyncio.run(gather(sys.argv[1], sys.argv[2], sys.argv[3]))
