import os
import sys
import time
from pathlib import Path
from google import genai
import dotenv

dotenv.load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not set in environment or .env file.")
    sys.exit(2)

client = genai.Client(api_key=GEMINI_API_KEY)

AGENT = "deep-research-max-preview-04-2026"
TERMINAL_STATUSES = {"completed", "failed", "cancelled"}
POLL_INTERVAL_SECONDS = 30
MAX_POLL_ITERATIONS = 120  # 60 minutes wall-clock cap
MAX_ARTIFACT_BYTES = 200_000
ALLOWED_EXTENSIONS = {".pdf", ".md", ".txt", ".html", ".htm", ".png", ".jpg", ".jpeg"}
ESTIMATED_COST_USD = 5.0
COST_GATE_SECONDS = 5


def run_research(founder_name: str, company: str, raw_dir: str):
    raw_path = Path(raw_dir)
    if not raw_path.exists():
        print(f"Error: raw_dir '{raw_dir}' not found.")
        sys.exit(2)

    files_to_upload = [f for f in raw_path.rglob("*") if f.is_file()]
    if not files_to_upload:
        print("Error: raw/ is empty — run orchestrate.py first or capture LinkedIn manually")
        sys.exit(1)

    artifacts = []
    temp_paths = []
    for p in files_to_upload:
        if "linkedin/activity_screenshots" in p.as_posix():
            continue
        if p.suffix.lower() not in ALLOWED_EXTENSIONS:
            print(f"Warning: Skipping {p} (unsupported extension)")
            continue

        file_to_upload = p
        if p.stat().st_size > MAX_ARTIFACT_BYTES:
            if p.suffix.lower() in {".md", ".txt", ".html", ".htm"}:
                print(f"Truncating {p} (> {MAX_ARTIFACT_BYTES} bytes)")
                content = p.read_text(encoding="utf-8", errors="ignore")
                truncated = content[:MAX_ARTIFACT_BYTES] + "\n\n[...truncated]"
                temp_path = p.with_suffix(p.suffix + ".truncated.md")
                temp_path.write_text(truncated, encoding="utf-8")
                file_to_upload = temp_path
                temp_paths.append(temp_path)
            else:
                print(f"Warning: Skipping {p} (binary file too large for grounding)")
                continue

        print(f"Uploading {file_to_upload}...")
        try:
            artifact = client.files.upload(file=str(file_to_upload))
            artifacts.append(artifact)
        except Exception as e:
            print(f"Error uploading {file_to_upload}: {e}")
            for tp in temp_paths:
                if tp.exists():
                    tp.unlink()
            raise

    for tp in temp_paths:
        if tp.exists():
            tp.unlink()

    prompt_template = Path("prompts/deep_research_prompt.md").read_text(encoding="utf-8")
    positioning = Path("prompts/kaide_labs_positioning.md").read_text(encoding="utf-8")
    prompt = (prompt_template
              .replace("{founder_name}", founder_name)
              .replace("{company}", company)
              .replace("{role}", "Founder")
              .replace("{inject kaide_labs_positioning.md here}", positioning))

    prompt += "\n\n--- GROUNDING DATA ---\n"
    for p in files_to_upload:
        if "linkedin/activity_screenshots" in p.as_posix():
            continue
        if p.suffix.lower() in {".md", ".txt", ".html", ".htm"}:
            try:
                content = p.read_text(encoding="utf-8", errors="ignore")
                prompt += f"\n\nSOURCE: {p.name}\n{content[:MAX_ARTIFACT_BYTES]}\n"
            except Exception as e:
                print(f"Warning: could not read {p}: {e}")

    print(f"\nReady to spend ~${ESTIMATED_COST_USD:.2f} on Deep Research Max for "
          f"{founder_name} at {company} ({len(artifacts)} artifacts attached).")
    print(f"Ctrl-C within {COST_GATE_SECONDS}s to abort.")
    try:
        time.sleep(COST_GATE_SECONDS)
    except KeyboardInterrupt:
        print("\nAborted by operator before spend.")
        sys.exit(130)

    print(f"Starting research for {founder_name} at {company}...")
    interaction = client.interactions.create(
        agent=AGENT,
        input=prompt,
        background=True,
    )

    print(f"Interaction started: {interaction.id}")

    current = None
    for i in range(MAX_POLL_ITERATIONS):
        try:
            current = client.interactions.get(interaction.id)
            print(f"  [{i+1}/{MAX_POLL_ITERATIONS}] status={current.status}")
            if current.status in TERMINAL_STATUSES:
                break
        except Exception as e:
            print(f"  Connection error during poll: {e}. Retrying in 5s...")
            time.sleep(5)
            continue
        time.sleep(POLL_INTERVAL_SECONDS)
    else:
        print(f"Error: Research did not reach terminal status within "
              f"{MAX_POLL_ITERATIONS * POLL_INTERVAL_SECONDS // 60} minutes.")
        print(f"Interaction id (still running, can be polled manually): {interaction.id}")
        sys.exit(1)

    if current is None or current.status != "completed":
        status = current.status if current else "unknown"
        print(f"Error: Research {status}")
        if current is not None and hasattr(current, "error"):
            print(f"Reason: {current.error}")
        sys.exit(1)

    dossier_path = raw_path.parent / "dossier.md"
    full_text = ""
    for out in current.outputs:
        if hasattr(out, "text") and out.text:
            full_text += out.text + "\n\n"
    dossier_path.write_text(full_text, encoding="utf-8")
    (raw_path.parent / ".interaction_id").write_text(interaction.id)
    print(f"✓ Dossier saved to {dossier_path} (interaction_id={interaction.id})")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python scripts/research.py '<founder_name>' '<company>' '<path/to/raw>'")
        sys.exit(2)
    run_research(sys.argv[1], sys.argv[2], sys.argv[3])
