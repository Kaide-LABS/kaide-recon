import asyncio
import sys
import os
import shutil
import argparse
from pathlib import Path

GATHERERS = [
    "gather_yc.py",
    "gather_jobs.py",
    "gather_twitter.py",
    "gather_hn.py",
    "gather_news.py",
    "gather_github.py",
    "gather_personal_site.py",
]

async def run_gatherer(script: str, founder: str, company: str, raw_dir: str, extra_arg: str = None):
    args = [sys.executable, f"scripts/{script}", founder, company, raw_dir]
    if extra_arg:
        args.append(extra_arg)
    
    proc = await asyncio.create_subprocess_exec(
        *args,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    return script, proc.returncode, stdout, stderr

async def main():
    parser = argparse.ArgumentParser(description="Orchestrate gathering layer for kaide-recon")
    parser.add_argument("founder", help="Founder name")
    parser.add_argument("company", help="Company name")
    parser.add_argument("--twitter-handle", help="Twitter handle")
    parser.add_argument("--github-username", help="GitHub username")
    parser.add_argument("--personal-site-url", help="Personal site URL")
    
    # Support legacy positional twitter_handle for backwards compat if needed, 
    # but the new flag pattern is preferred.
    # Actually, the spec says "Add THREE optional CLI flags", so I'll follow that.
    
    args, unknown = parser.parse_known_args()
    
    founder = args.founder
    company = args.company
    
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
    
    tasks = []
    for script in GATHERERS:
        extra = None
        if script == "gather_twitter.py":
            if not args.twitter_handle: continue
            extra = args.twitter_handle
        elif script == "gather_github.py":
            if not args.github_username: continue
            extra = args.github_username
        elif script == "gather_personal_site.py":
            if not args.personal_site_url: continue
            extra = args.personal_site_url
            
        tasks.append(run_gatherer(script, founder, company, str(raw_dir), extra))
        
    results = await asyncio.gather(*tasks)

    print("\nGathering Summary:")
    print(f"{'Script':<25} | {'RC':<3} | {'Size':<10}")
    print("-" * 45)
    
    GATHERER_MAP = {
        "gather_yc.py": "yc_page.md",
        "gather_jobs.py": "company_jobs.md",
        "gather_twitter.py": "twitter.md",
        "gather_hn.py": "hn_comments.md",
        "gather_news.py": "news_coverage.md",
        "gather_github.py": "github.md",
        "gather_personal_site.py": "personal_site.md",
    }
    
    failed_count = 0
    for script, rc, stdout, stderr in results:
        out_filename = GATHERER_MAP.get(script, "unknown.md")
        out_file = raw_dir / out_filename
        size = f"{out_file.stat().st_size}B" if out_file.exists() else "MISSING"
        print(f"{script:<25} | {rc:<3} | {size:<10}")
        if rc != 0:
            failed_count += 1
            print(f"  Error in {script}: {stderr.decode()[:2000]}")

    print(f"\nNext: python scripts/research.py '{founder}' '{company}' '{raw_dir}'")
    sys.exit(failed_count)

if __name__ == "__main__":
    asyncio.run(main())
