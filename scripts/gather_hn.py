import sys
import os
import datetime
import requests
from pathlib import Path

def gather(founder: str, company: str, raw_dir: str, hn_handle: str):
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    url = f"https://hn.algolia.com/api/v1/search_by_date?tags=author_{hn_handle}&hitsPerPage=200"
    
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        data = r.json()
        
        hits = data.get("hits", [])
        content = ""
        for hit in hits:
            created_at = hit.get("created_at")
            title = hit.get("story_title") or hit.get("title") or "N/A"
            text = hit.get("comment_text") or hit.get("text") or ""
            content += f"## {created_at} — {title}\n\n{text}\n\n---\n\n"
            
    except Exception as e:
        print(f"Error gathering HN comments for {hn_handle}: {e}")
        raise

    header = f"# HN Comments — {hn_handle}\n\n"
    header += f"**Captured:** {timestamp}\n"
    header += f"**Source URL:** {url}\n\n"
    header += "---\n\n"
    
    out_file = Path(raw_dir) / "hn_comments.md"
    out_file.write_text(header + content, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python scripts/gather_hn.py '<founder>' '<company>' '<raw_dir>' '<hn_handle>'")
        sys.exit(2)
    gather(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
