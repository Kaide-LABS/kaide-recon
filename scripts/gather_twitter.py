import asyncio
import sys
import os
import datetime
from pathlib import Path
from playwright.async_api import async_playwright

async def gather(founder: str, company: str, raw_dir: str, handle: str):
    # Remove @ if present
    handle = handle.lstrip("@")
    # Default nitter instance
    nitter_instance = os.environ.get("NITTER_INSTANCE", "https://nitter.net")
    url = f"{nitter_instance}/{handle}"
    
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (kaide-recon)")
        page = await context.new_page()
        
        try:
            response = await page.goto(url, timeout=30000)
            if response.status == 429:
                print("Error: Nitter rate limited (429).")
                sys.exit(1)
            
            content = await page.inner_text("body")
            if "Instance has been rate limited" in content or "Rate limit exceeded" in content:
                print("Error: Nitter instance rate limited.")
                sys.exit(1)
                
        except Exception as e:
            print(f"Error gathering Twitter from {url}: {e}")
            raise
        finally:
            await browser.close()

    header = f"# Twitter — {handle}\n\n"
    header += f"**Captured:** {timestamp}\n"
    header += f"**Source URL:** {url}\n\n"
    header += "---\n\n"
    
    out_file = Path(raw_dir) / "twitter.md"
    out_file.write_text(header + content, encoding="utf-8")

async def main():
    if len(sys.argv) < 4:
        print("Usage: python scripts/gather_twitter.py '<founder>' '<company>' '<raw_dir>' [twitter_handle]")
        sys.exit(2)
        
    founder = sys.argv[1]
    company = sys.argv[2]
    raw_dir = sys.argv[3]
    
    handle = None
    if len(sys.argv) >= 5:
        handle = sys.argv[4]
    else:
        handle = os.environ.get("TWITTER_HANDLE")
        
    if not handle or handle.strip() == "":
        out_file = Path(raw_dir) / "twitter.md"
        out_file.write_text("# Twitter\n\nNo twitter handle provided.\n", encoding="utf-8")
        sys.exit(0)
        
    try:
        await gather(founder, company, raw_dir, handle)
    except Exception as e:
        print(f"Error gathering Twitter: {e}")
        out_file = Path(raw_dir) / "twitter.md"
        if not out_file.exists():
            out_file.write_text(f"# Twitter — {handle}\n\nError occurred during gathering: {e}\n", encoding="utf-8")
        sys.exit(0)

if __name__ == "__main__":
    asyncio.run(main())
