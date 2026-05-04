import asyncio
import sys
import os
import shutil
from pathlib import Path

GATHERERS = [
    "gather_yc.py",
    "gather_jobs.py",
    "gather_twitter.py",
    "gather_hn.py",
    "gather_news.py",
]

async def run_gatherer(script: str, founder: str, company: str, raw_dir: str, twitter_handle: str = None):
    args = [sys.executable, f"scripts/{script}", founder, company, raw_dir]
    if script == "gather_twitter.py" and twitter_handle:
        args.append(twitter_handle)
    
    proc = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    return script, proc.returncode, stdout, stderr

async def main(founder: str, company: str, twitter_handle: str = None):
    slug = f"{founder.lower().replace(' ', '-')}-{company.lower().replace(' ', '-')}"
    prospect_dir = Path("dossiers") / slug
    raw_dir = prospect_dir / "raw"
    
    (raw_dir / "linkedin" / "activity_screenshots").mkdir(parents=True, exist_ok=True)
    (raw_dir / "podcasts").mkdir(parents=True, exist_ok=True)
    
    checklist_path = prospect_dir / "intake_checklist.md"
    if not checklist_path.exists():
        template_path = Path("dossiers/_template/intake_checklist.md")
        if template_path.exists():
            shutil.copy(template_path, checklist_path)
            # Personalize checklist
            content = checklist_path.read_text()
            content = content.replace("{founder_name}", founder).replace("{company}", company)
            import datetime
            today = datetime.date.today().isoformat()
            content = content.replace("{YYYY-MM-DD}", today)
            checklist_path.write_text(content)

    print(f"Starting gathering for {slug}...")
    tasks = [run_gatherer(s, founder, company, str(raw_dir), twitter_handle) for s in GATHERERS]
    results = await asyncio.gather(*tasks)

    print("\nGathering Summary:")
    print(f"{'Script':<20} | {'RC':<3} | {'Size':<10}")
    print("-" * 40)
    
    GATHERER_MAP = {
        "gather_yc.py": "yc_page.md",
        "gather_jobs.py": "company_jobs.md",
        "gather_twitter.py": "twitter.md",
        "gather_hn.py": "hn_comments.md",
        "gather_news.py": "news_coverage.md",
    }
    
    failed_count = 0
    for script, rc, stdout, stderr in results:
        out_filename = GATHERER_MAP.get(script, "unknown.md")
        out_file = raw_dir / out_filename
        size = f"{out_file.stat().st_size}B" if out_file.exists() else "MISSING"
        print(f"{script:<20} | {rc:<3} | {size:<10}")
        if rc != 0:
            failed_count += 1
            print(f"  Error in {script}: {stderr.decode()[:2000]}")

    print(f"\nNext: python scripts/research.py '{founder}' '{company}' '{raw_dir}'")
    sys.exit(failed_count)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/orchestrate.py '<founder_name>' '<company>' [twitter_handle]")
        sys.exit(2)
    
    founder = sys.argv[1]
    company = sys.argv[2]
    twitter_handle = sys.argv[3] if len(sys.argv) > 3 else None
    
    asyncio.run(main(founder, company, twitter_handle))
