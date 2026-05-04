import os
import sys
import requests
import dotenv

dotenv.load_dotenv()

BASE = "https://apigcp.trynia.ai/v2"
NIA_API_KEY = os.environ.get("NIA_API_KEY")

def get_headers():
    if not NIA_API_KEY:
        print("Error: NIA_API_KEY not set.")
        sys.exit(2)
    return {
        "Authorization": f"Bearer {NIA_API_KEY}",
        "Content-Type": "application/json",
    }

def post_source(body: dict):
    try:
        r = requests.post(f"{BASE}/sources", headers=get_headers(), json=body, timeout=30)
        if r.status_code == 409:
            print(f"Already indexed: {body}")
            return
        r.raise_for_status()
        print(r.json())
    except requests.exceptions.HTTPError as e:
        if 500 <= r.status_code < 600:
            print(f"Server error {r.status_code}, retrying once...")
            import time
            time.sleep(5)
            r = requests.post(f"{BASE}/sources", headers=get_headers(), json=body, timeout=30)
            if r.status_code == 409:
                 print(f"Already indexed: {body}")
                 return
            r.raise_for_status()
            print(r.json())
        else:
            print(f"HTTP Error: {r.text}")
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:")
        print("  python scripts/index_to_nia.py repo '<owner>/<name>' [branch]")
        print("  python scripts/index_to_nia.py docs '<url>'")
        sys.exit(2)
    
    kind = sys.argv[1]
    target = sys.argv[2]
    
    if kind == "repo":
        branch = sys.argv[3] if len(sys.argv) > 3 else "main"
        post_source({"type": "repository", "repository": target, "branch": branch})
    elif kind == "docs":
        post_source({"type": "documentation", "url": target})
    else:
        print(f"Unknown kind: {kind}")
        sys.exit(2)
