import os
import sys
import time
import glob
from pathlib import Path
from google import genai
import dotenv

# Load env from .env file
dotenv.load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not set in environment or .env file.")
    sys.exit(2)

client = genai.Client(api_key=GEMINI_API_KEY)

AGENT = "deep-research-max-preview-04-2026"
TERMINAL_STATUSES = {"completed", "failed", "cancelled"}
POLL_INTERVAL_SECONDS = 30
MAX_ARTIFACT_BYTES = 200_000
ALLOWED_EXTENSIONS = {".pdf", ".md", ".txt", ".html", ".htm", ".png", ".jpg", ".jpeg"}

def run_research(founder_name: str, company: str, raw_dir: str):
    raw_path = Path(raw_dir)
    if not raw_path.exists():
        print(f"Error: raw_dir '{raw_dir}' not found.")
        sys.exit(2)

    files_in_raw = list(raw_path.rglob("*"))
    files_to_upload = [f for f in files_in_raw if f.is_file()]

    if not files_to_upload:
        print("Error: raw/ is empty — run orchestrate.py first or capture LinkedIn manually")
        sys.exit(1)

    artifacts = []
    for p in files_to_upload:
        # Skip screenshots per spec §6.1.3
        if "linkedin/activity_screenshots" in str(p.as_posix()):
            continue
        
        if p.suffix.lower() not in ALLOWED_EXTENSIONS:
            print(f"Warning: Skipping {p} (unsupported extension)")
            continue

        file_to_upload = p
        if p.stat().st_size > MAX_ARTIFACT_BYTES:
            # Simple truncation for text-like files
            if p.suffix.lower() in {".md", ".txt", ".html", ".htm"}:
                print(f"Truncating {p} (> {MAX_ARTIFACT_BYTES} bytes)")
                content = p.read_text(encoding="utf-8", errors="ignore")
                truncated_content = content[:MAX_ARTIFACT_BYTES] + "\n\n[...truncated]"
                temp_truncated = p.with_suffix(p.suffix + ".truncated.md")
                temp_truncated.write_text(truncated_content, encoding="utf-8")
                file_to_upload = temp_truncated
            else:
                print(f"Warning: Skipping {p} (binary file too large for grounding)")
                continue

        print(f"Uploading {file_to_upload}...")
        try:
            artifact = client.files.upload(file=str(file_to_upload))
            artifacts.append(artifact)
            # Cleanup temp truncated file if created
            if file_to_upload != p:
                file_to_upload.unlink()
        except Exception as e:
            print(f"Error uploading {file_to_upload}: {e}")
            raise

    # 2. Compose prompt
    prompt_template = Path("prompts/deep_research_prompt.md").read_text()
    positioning = Path("prompts/kaide_labs_positioning.md").read_text()
    
    prompt = (prompt_template
              .replace("{founder_name}", founder_name)
              .replace("{company}", company)
              .replace("{role}", "Founder") # Defaulting role as it's in the template but not CLI
              .replace("{inject kaide_labs_positioning.md here}", positioning))

    # 3. Kick off Deep Research Max
    print(f"Starting research for {founder_name} at {company}...")
    interaction = client.interactions.create(
        agent=AGENT,
        input=[prompt, *artifacts],
        background=True,
    )
    print(f"Interaction started: {interaction.id}")

    # 4. Poll
    while True:
        current = client.interactions.get(interaction.id)
        print(f"  status={current.status}")
        if current.status in TERMINAL_STATUSES:
            break
        time.sleep(POLL_INTERVAL_SECONDS)

    if current.status != "completed":
        print(f"Error: Research {current.status}")
        if hasattr(current, 'error'):
            print(f"Reason: {current.error}")
        sys.exit(1)

    # 5. Save output
    dossier_path = raw_path.parent / "dossier.md"
    dossier_path.write_text(current.outputs[-1].text, encoding="utf-8")

    (raw_path.parent / ".interaction_id").write_text(interaction.id)
    print(f"✓ Dossier saved to {dossier_path} (interaction_id={interaction.id})")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python scripts/research.py '<founder_name>' '<company>' '<path/to/raw>'")
        sys.exit(2)
    run_research(sys.argv[1], sys.argv[2], sys.argv[3])
