import asyncio
import sys
import os
import datetime
from pathlib import Path
from playwright.async_api import async_playwright

async def gather_single_podcast(url: str, raw_dir: Path, idx: int):
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (kaide-recon)")
        page = await context.new_page()
        
        try:
            await page.goto(url, timeout=30000)
            # YouTube transcript extraction is tricky and often changes.
            # For Phase 1, we attempt to find the transcript button or just note it's manual.
            # Realistically, for internal tool, manual capture of transcripts is safer if it's too complex.
            # But let's try a basic text dump.
            await asyncio.sleep(2)
            content = await page.inner_text("body")
            
            # Simple check if it's YouTube
            if "youtube.com" in url:
                # Try to click 'More' then 'Show transcript' - this is fragile
                try:
                    await page.click('button[aria-label="More actions"]', timeout=5000)
                    await page.click('tp-yt-paper-item:has-text("Show transcript")', timeout=5000)
                    await asyncio.sleep(2)
                    transcript_text = await page.inner_text('#segments-container')
                    content = transcript_text
                except:
                    content = f"MANUAL CAPTURE NEEDED FOR {url}\n\nFull page text dump:\n\n" + content
            
        except Exception as e:
            print(f"Error gathering podcast {url}: {e}")
            content = f"Error gathering {url}: {e}"
        finally:
            await browser.close()

    header = f"# Podcast Transcript — {url}\n\n"
    header += f"**Captured:** {timestamp}\n"
    header += f"**Source URL:** {url}\n\n"
    header += "---\n\n"
    
    out_file = raw_dir / f"{idx:02d}_podcast.md"
    out_file.write_text(header + content, encoding="utf-8")

async def gather(founder: str, company: str, raw_dir: str, urls_str: str):
    urls = [u.strip() for u in urls_str.split(",") if u.strip()]
    podcasts_dir = Path(raw_dir) / "podcasts"
    podcasts_dir.mkdir(parents=True, exist_ok=True)
    
    tasks = [gather_single_podcast(url, podcasts_dir, i+1) for i, url in enumerate(urls)]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python scripts/gather_podcasts.py '<founder>' '<company>' '<raw_dir>' '<url1,url2,...>'")
        sys.exit(2)
    asyncio.run(gather(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]))
