import asyncio
import sys
import os
import shutil
import datetime
from pathlib import Path
import subprocess

DELTA_DIR_NAME = "delta"
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
    
    if not (prospect_dir / "dossier.md").exists():
        print("Error: no prior dossier — run a first-time pitch via orchestrate.py + research.py")
        sys.exit(2)
        
    date_str = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
    delta_dir = prospect_dir / "raw" / DELTA_DIR_NAME / date_str
    delta_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Starting gathering into {delta_dir}...")
    tasks = [run_gatherer(s, founder, company, str(delta_dir), twitter_handle) for s in GATHERERS]
    results = await asyncio.gather(*tasks)

    for script, rc, stdout, stderr in results:
        if rc != 0:
            print(f"Warning: {script} failed. Stderr: {stderr.decode()[:500]}")

    print("\nDelta Classification Summary:")
    print(f"{'Artifact':<30} | {'Verdict':<15} | {'Size':<10}")
    print("-" * 60)

    should_resynth = False
    
    for f in delta_dir.iterdir():
        if not f.is_file():
            continue
            
        if f.stat().st_size == 0:
            continue
            
        route_proc = subprocess.run(
            [sys.executable, "scripts/route.py", str(f)],
            capture_output=True, text=True
        )
        
        verdict = route_proc.stdout.strip()
        if route_proc.returncode != 0 or verdict not in ["KEEP", "SKIP", "RE_SYNTHESIZE"]:
            print(f"Warning: route.py malformed for {f.name}. Defaulting to KEEP.")
            verdict = "KEEP"
            
        size_str = f"{f.stat().st_size}B"
        print(f"{f.name:<30} | {verdict:<15} | {size_str:<10}")
        
        if verdict == "SKIP":
            f.unlink()
        elif verdict == "RE_SYNTHESIZE":
            should_resynth = True

    if should_resynth:
        print("\nDelta indicates RE_SYNTHESIZE. Cost gate: ~$5.00.")
        print("Starting Deep Research Max in 5 seconds... (Ctrl-C to abort)")
        try:
            import time
            time.sleep(5)
        except KeyboardInterrupt:
            print("\nAborted.")
            sys.exit(0)
            
        research_proc = subprocess.run(
            [sys.executable, "scripts/research.py", founder, company, str(delta_dir)]
        )
        if research_proc.returncode != 0:
            sys.exit(research_proc.returncode)
            
        # Move dossier and .interaction_id
        temp_dossier = delta_dir.parent / "dossier.md"
        temp_id = delta_dir.parent / ".interaction_id"
        
        final_dossier = prospect_dir / f"dossier_{date_str}.md"
        final_id = prospect_dir / f".interaction_id_{date_str}"
        
        if temp_dossier.exists():
            shutil.move(temp_dossier, final_dossier)
        if temp_id.exists():
            shutil.move(temp_id, final_id)
            
        print(f"\nRe-index: python scripts/index_to_nia.py repo <gh-user>/kaide-recon master")
    else:
        print("\nDelta is thin — no Max spend. Re-query the existing dossier via Claude+Nia MCP for a different angle instead.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/repitch.py '<founder>' '<company>' [twitter_handle]")
        sys.exit(2)
        
    founder = sys.argv[1]
    company = sys.argv[2]
    twitter_handle = sys.argv[3] if len(sys.argv) > 3 else None
    
    asyncio.run(main(founder, company, twitter_handle))
