import sys
import os
import requests
import datetime
from pathlib import Path

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Warning: BeautifulSoup4 not found. Attempting to install...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

def gather(founder, company, raw_dir, site_url):
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    out_file = Path(raw_dir) / "personal_site.md"
    
    headers = {
        "User-Agent": "kaide-recon/1.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    
    try:
        r = requests.get(site_url, headers=headers, timeout=30, allow_redirects=True)
        r.raise_for_status()
        html = r.text
        
        soup = BeautifulSoup(html, 'html.parser')
        
        title = soup.title.string if soup.title else "N/A"
        
        headings = []
        for h in soup.find_all(['h1', 'h2', 'h3']):
            text = h.get_text().strip()
            if text:
                headings.append(f"{h.name}: {text}")
        
        # Strip noise
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            tag.decompose()
            
        main_content = ""
        # Try prioritized tags
        main_tag = soup.find('main') or soup.find('article') or soup.body
        if main_tag:
            main_content = main_tag.get_text(separator='\n').strip()
        
        # If GitHub Pages, try fetching /about.md or /index.md (unlikely to work directly via HTTP, but good for some setups)
        # Actually, many Jekyll/Hugo sites have a /about/ or /index.html
        
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            text = a.get_text().strip()
            if href.startswith('http') and text:
                links.append(f"- [{text}]({href})")
        
        md = f"# Personal Site — {site_url}\n\n"
        md += f"**Captured:** {timestamp}\n"
        md += f"**Source:** {site_url}\n\n"
        
        md += f"## Site Title\n{title}\n\n"
        
        md += "## Headings\n"
        if headings:
            md += "\n".join(headings) + "\n\n"
        else:
            md += "None found.\n\n"
            
        md += "## Main Content\n"
        if main_content:
            md += main_content[:10000] + ("\n\n[...truncated]" if len(main_content) > 10000 else "") + "\n\n"
        else:
            md += "Could not extract main content.\n\n"
            
        md += "## External Links\n"
        if links:
            # Cap links to top 50 to avoid bloat
            md += "\n".join(links[:50]) + "\n"
        else:
            md += "None found.\n"
            
        out_file.write_text(md, encoding="utf-8")

    except Exception as e:
        print(f"Error gathering personal site: {e}")
        out_file.write_text(f"# Personal Site — {site_url}\n\nFailed to load site: {e}\n", encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python scripts/gather_personal_site.py '<founder>' '<company>' '<raw_dir>' '<site_url>'")
        sys.exit(2)
        
    gather(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
