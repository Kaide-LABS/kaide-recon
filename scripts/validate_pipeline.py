import os
import sys
import subprocess
from pathlib import Path
import dotenv

def run_checks():
    print("kaide-recon pipeline validator")
    print("─────────────────────────────────")
    
    fails = 0
    warns = 0
    oks = 0

    def ok(msg):
        nonlocal oks
        oks += 1
        print(f"[OK]   {msg}")
        
    def warn(msg):
        nonlocal warns
        warns += 1
        print(f"[WARN] {msg}")

    def fail(msg):
        nonlocal fails
        fails += 1
        print(f"[FAIL] {msg}")

    # 1. .env exists
    if Path(".env").exists():
        ok(".env present")
    else:
        fail(".env missing")

    # Load env
    dotenv.load_dotenv()

    # 2 & 3. API Keys
    if os.environ.get("GEMINI_API_KEY"):
        ok("GEMINI_API_KEY set")
    else:
        fail("GEMINI_API_KEY not set")

    if os.environ.get("NIA_API_KEY"):
        ok("NIA_API_KEY set")
    else:
        fail("NIA_API_KEY not set")

    if os.environ.get("GITHUB_TOKEN"):
        ok("GITHUB_TOKEN set")
    else:
        warn("GITHUB_TOKEN not set — private repo indexing will fail")

    # 4. Scripts present
    scripts = [
        "orchestrate.py", "research.py", "index_to_nia.py", "query_dossier.py", 
        "route.py", "gather_yc.py", "gather_jobs.py", "gather_twitter.py", 
        "gather_hn.py", "gather_news.py", "gather_podcasts.py", "repitch.py", "validate_pipeline.py"
    ]
    missing_scripts = [s for s in scripts if not Path(f"scripts/{s}").exists()]
    if not missing_scripts:
        ok(f"{len(scripts)}/{len(scripts)} scripts present")
    else:
        fail(f"Missing scripts: {', '.join(missing_scripts)}")

    # 5. Prompts present
    prompts = ["kaide_labs_positioning.md", "deep_research_prompt.md", "router_prompt.md"]
    missing_prompts = [p for p in prompts if not Path(f"prompts/{p}").exists()]
    if not missing_prompts:
        ok(f"{len(prompts)}/{len(prompts)} prompts present")
    else:
        fail(f"Missing prompts: {', '.join(missing_prompts)}")

    # 6. Requirements
    reqs_path = Path("requirements.txt")
    if reqs_path.exists():
        reqs = reqs_path.read_text().strip().split("\n")
        # Check against the 4 locked deps
        locked = ["google-genai>=1.0.0", "requests>=2.32.0", "playwright>=1.59.0", "python-dotenv>=1.0.0"]
        if sorted([r.strip() for r in reqs]) == sorted(locked):
            ok("requirements.txt matches lock")
        else:
            fail("requirements.txt does not match locked dependencies")
    else:
        fail("requirements.txt missing")

    # 7. Intake checklist template
    if Path("dossiers/_template/intake_checklist.md").exists():
        ok("intake_checklist template present")
    else:
        fail("intake_checklist template missing")

    # 8. James He dossier
    dossier_path = Path("dossiers/james-he-artificial-societies/dossier.md")
    if dossier_path.exists():
        content = dossier_path.read_text()
        sections = [
            "Founder Background", "Company Snapshot", "Stated Pain Points", 
            "Technical Decisions", "Enterprise Integration Surface", 
            "Recommended Outreach Angle", "Red Flags"
        ]
        missing_sections = [s for s in sections if s not in content]
        if not missing_sections:
            ok("James He dossier present (7/7 sections)")
        else:
            fail(f"James He dossier missing sections: {', '.join(missing_sections)}")
    else:
        fail("James He dossier missing")

    # 9. .gitignore patterns
    gitignore_path = Path(".gitignore")
    if gitignore_path.exists():
        git_content = gitignore_path.read_text()
        patterns = [".env", "dossiers/*/raw/linkedin/", "*.pdf", ".interaction_id"]
        missing_patterns = [p for p in patterns if p not in git_content]
        if not missing_patterns:
            ok(".gitignore covers sensitive paths")
        else:
            fail(f".gitignore missing patterns: {', '.join(missing_patterns)}")
    else:
        fail(".gitignore missing")

    # 10. No LinkedIn artifacts tracked
    try:
        # Use git ls-files to check if anything under dossiers/*/raw/linkedin/ is tracked
        result = subprocess.run(["git", "ls-files", "dossiers/*/raw/linkedin/"], capture_output=True, text=True)
        if result.stdout.strip():
            fail(f"LinkedIn artifacts tracked by git:\n{result.stdout.strip()}")
        else:
            ok("No LinkedIn artifacts tracked by git")
    except Exception as e:
        fail(f"Could not run git ls-files: {e}")

    # 11. Playwright installed
    try:
        result = subprocess.run([sys.executable, "-m", "playwright", "install", "--dry-run", "chromium"], capture_output=True, text=True)
        if result.returncode == 0:
            ok("playwright chromium check passed")
        else:
            warn("playwright chromium check failed (may need 'playwright install chromium')")
    except Exception as e:
        warn(f"playwright check failed: {e}")

    # 12. google-genai importable
    try:
        import google.genai
        ok("google-genai importable")
    except ImportError:
        fail("google-genai not importable")

    print("─────────────────────────────────")
    result_str = "PASS" if fails == 0 else "FAIL"
    print(f"Result: {result_str} ({oks} ok, {warns} warn, {fails} fail)")
    
    sys.exit(1 if fails > 0 else 0)

if __name__ == "__main__":
    run_checks()
