import os
import sys
from pathlib import Path
from google import genai
import dotenv

dotenv.load_dotenv()

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not set.")
    sys.exit(2)

client = genai.Client(api_key=GEMINI_API_KEY)

ROUTER_MODEL = "gemini-3-flash-preview"
MAX_INPUT_CHARS = 200_000
VALID_VERDICTS = {"KEEP", "RE_SYNTHESIZE", "SKIP"}

def classify(artifact_path: str):
    p = Path(artifact_path)
    if not p.exists():
        print(f"Error: Artifact {artifact_path} not found.")
        sys.exit(2)

    rubric = Path("prompts/router_prompt.md").read_text()
    artifact_content = p.read_text(encoding="utf-8", errors="ignore")[:MAX_INPUT_CHARS]
    
    prompt = rubric.replace("{artifact_content}", artifact_content)

    resp = client.models.generate_content(
        model=ROUTER_MODEL,
        contents=[prompt],
    )
    
    verdict = resp.text.strip().splitlines()[0].strip().upper()
    
    if verdict not in VALID_VERDICTS:
        print(f"Error: Malformed verdict: {verdict}")
        print(f"Raw output: {resp.text}")
        sys.exit(1)
        
    print(verdict)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/route.py '<path/to/artifact.md>'")
        sys.exit(2)
    classify(sys.argv[1])
