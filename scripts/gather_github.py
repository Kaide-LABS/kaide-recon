import os
import sys
import requests
import datetime
from pathlib import Path

# Load env vars manually to avoid dependency issues in this flat script
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

def get_headers():
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "kaide-recon/1.0"
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    return headers

def fetch_profile(username):
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url, headers=get_headers(), timeout=10)
    if r.status_code == 404:
        return None
    r.raise_for_status()
    return r.json()

def fetch_repos(username):
    url = f"https://api.github.com/users/{username}/repos?sort=stars&direction=desc&per_page=20"
    r = requests.get(url, headers=get_headers(), timeout=10)
    r.raise_for_status()
    return r.json()

def fetch_readme(username, repo_name):
    url = f"https://api.github.com/repos/{username}/{repo_name}/readme"
    try:
        r = requests.get(url, headers=get_headers(), timeout=10)
        if r.status_code == 404:
            return ""
        r.raise_for_status()
        download_url = r.json().get("download_url")
        if not download_url:
            return ""
        content_r = requests.get(download_url, timeout=10)
        content_r.raise_for_status()
        return content_r.text[:5000]
    except Exception as e:
        print(f"Warning: Failed to fetch README for {repo_name}: {e}")
        return ""

def fetch_pinned(username):
    # GraphQL for pinned repos
    if not GITHUB_TOKEN:
        return []
    
    query = """
    {
      user(login: "%s") {
        pinnedItems(first: 6, types: REPOSITORY) {
          nodes {
            ... on Repository {
              name
              description
              primaryLanguage {
                name
              }
              stargazerCount
              forkCount
              pushedAt
            }
          }
        }
      }
    }
    """ % username
    
    url = "https://api.github.com/graphql"
    try:
        r = requests.post(url, headers=get_headers(), json={"query": query}, timeout=15)
        r.raise_for_status()
        data = r.json()
        if "errors" in data:
            print(f"Warning: GraphQL errors: {data['errors']}")
            return []
        nodes = data.get("data", {}).get("user", {}).get("pinnedItems", {}).get("nodes", [])
        return nodes
    except Exception as e:
        print(f"Warning: GraphQL fetch for pinned repos failed: {e}")
        return []

def fetch_events(username):
    url = f"https://api.github.com/users/{username}/events/public?per_page=30"
    try:
        r = requests.get(url, headers=get_headers(), timeout=10)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        print(f"Warning: Failed to fetch events: {e}")
        return []

def gather(founder, company, raw_dir, username):
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    out_file = Path(raw_dir) / "github.md"
    
    profile = fetch_profile(username)
    if not profile:
        out_file.write_text(f"# GitHub — {username}\n\nGitHub username not found.\n", encoding="utf-8")
        return

    # Check rate limit
    headers = get_headers()
    rate_r = requests.get("https://api.github.com/rate_limit", headers=headers, timeout=10)
    if rate_r.status_code == 200:
        remaining = rate_r.json().get("resources", {}).get("core", {}).get("remaining", 0)
        if remaining < 10:
            print(f"Warning: Low GitHub API rate limit: {remaining} remaining.")
            if not GITHUB_TOKEN:
                print("Hint: Set GITHUB_TOKEN in .env to increase limits.")

    pinned = fetch_pinned(username)
    repos = fetch_repos(username)
    events = fetch_events(username)

    md = f"# GitHub — {username}\n\n"
    md += f"**Captured:** {timestamp}\n"
    md += f"**Source:** https://github.com/{username}\n\n"
    
    md += "## Profile\n"
    md += f"- **Bio:** {profile.get('bio') or 'N/A'}\n"
    md += f"- **Location:** {profile.get('location') or 'N/A'}\n"
    md += f"- **Company:** {profile.get('company') or 'N/A'}\n"
    md += f"- **Blog:** {profile.get('blog') or 'N/A'}\n"
    md += f"- **Followers:** {profile.get('followers')}\n"
    md += f"- **Created:** {profile.get('created_at')}\n\n"

    if pinned:
        md += "## Pinned Repositories\n"
        for r in pinned:
            md += f"### {r['name']}\n"
            md += f"- **Description:** {r.get('description') or 'N/A'}\n"
            md += f"- **Language:** {r.get('primaryLanguage', {}).get('name') if r.get('primaryLanguage') else 'N/A'}\n"
            md += f"- **Stars/Forks:** {r.get('stargazerCount')}/{r.get('forkCount')}\n"
            md += f"- **Last Activity:** {r.get('pushedAt')}\n\n"

    md += "## Top Repositories (by stars)\n"
    for r in repos:
        md += f"### {r['name']}\n"
        md += f"- **Description:** {r.get('description') or 'N/A'}\n"
        md += f"- **Language:** {r.get('language') or 'N/A'}\n"
        md += f"- **Stars/Forks:** {r.get('stargazers_count')}/{r.get('forks_count')}\n"
        md += f"- **Last Activity:** {r.get('pushed_at')}\n"
        
        readme = fetch_readme(username, r['name'])
        if readme:
            md += "\n#### README Excerpt\n```text\n"
            md += readme.replace("```", "'''") # Minimal escaping
            md += "\n```\n"
        md += "\n---\n\n"

    md += "## Recent Activity\n"
    for e in events:
        etype = e.get("type")
        repo = e.get("repo", {}).get("name")
        created = e.get("created_at")
        md += f"- **{created}:** {etype} on {repo}\n"

    out_file.write_text(md, encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usage: python scripts/gather_github.py '<founder>' '<company>' '<raw_dir>' '<github_username>'")
        sys.exit(2)
    
    try:
        gather(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    except Exception as e:
        print(f"Error gathering GitHub: {e}")
        # Write stub on failure to not break orchestration
        out_path = Path(sys.argv[3]) / "github.md"
        if not out_path.exists():
            out_path.write_text(f"# GitHub — {sys.argv[4]}\n\nError occurred during gathering: {e}\n", encoding="utf-8")
        sys.exit(0)
