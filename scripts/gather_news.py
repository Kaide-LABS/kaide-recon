import asyncio
import sys
import os
import datetime
import urllib.parse
from pathlib import Path
from playwright.async_api import async_playwright

async def gather(founder: str, company: str, raw_dir: str):
    query = f'"{founder}" OR "{company}"'
    encoded_query = urllib.parse.quote(query)
    url = f"https://news.google.com/search?q={encoded_query}"
    
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (kaide-recon)")
        page = await context.new_page()
        
        try:
            await page.goto(url, timeout=30000)
            # Basic scrape of headlines and snippets
            content = await page.inner_text("body")
        except Exception as e:
            print(f"Error gathering news from {url}: {e}")
            raise
        finally:
            await browser.close()

    header = f"# News Coverage — {founder} / {company}\n\n"
    header += f"**Captured:** {timestamp}\n"
    header += f"**Source URL:** {url}\n\n"
    header += "---\n\n"
    
    out_file = Path(raw_dir) / "news_coverage.md"
    out_file.write_text(header + content, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python scripts/gather_news.py '<founder>' '<company>' '<raw_dir>'")
        sys.exit(2)
    asyncio.run(gather(sys.argv[1], sys.argv[2], sys.argv[3]))
