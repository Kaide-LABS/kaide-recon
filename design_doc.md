# Kaide Labs — Founder Intel Pipeline

**Codename:** `kaide-recon`
**Author:** Hafeedh (Founder, Kaide Labs)
**Status:** v1 — building today
**Purpose:** Hyper-personalized cold outreach to B2B AI startup founders. Productize the recon → outreach loop.
**Last revised:** May 3, 2026

---

## 1. Architecture (4 layers — locked)

```
GATHERING LAYER          SYNTHESIS LAYER             INDEXING LAYER          QUERYING LAYER
─────────────────        ────────────────────        ─────────────────       ─────────────────
Playwright + manual ───> Gemini Deep Research ────> Nia v2              ──> Claude via Nia MCP
(the "OpenClaw"          Max                          POST /v2/sources       POST /v2/search
 pattern) +              (deep-research-max-          (type discriminator)   (mode=universal)
Gemini 3 Flash router    preview-04-2026)
                         via Interactions API:
- Twitter (Nitter)         POST /v1beta/interactions  - Founder GitHub        - Cross-source
- Podcast transcripts      background=True              repos                   citation-aware
- Personal sites           ~$5/run, ~15 min,          - Company GitHub          search
- HN comments              160 search queries,          org                   - Outreach angle
- GitHub READMEs           multimodal Files API       - Dossiers repo           generation
- Conf talks               grounding                  - Company docs site     - Gap detection
- YC pages                                              (type=documentation)
- News coverage          Cheap routing layer:
- Job postings (open     gemini-3-flash-preview
  web only — not LI)     ($0.50/$3 per M)
- Manual: LinkedIn       decides per-artifact:
  PDFs, LI Jobs          index? re-synth? skip?
```

### 1.1 Model lock
| Role | Model ID | Why |
|---|---|---|
| Synthesis | `deep-research-max-preview-04-2026` | Multi-step autonomous research, multimodal grounding, ~160 grounded search queries per task. Single $5 call replaces hours of manual recon. |
| Routing / triage | `gemini-3-flash-preview` | $0.50/M in, $3/M out, 1M context. Used for the cheap "is this artifact worth promoting?" decision before spending Max budget. |

Do not change either model without an explicit upgrade decision documented here.

---

## 2. Repository Structure

```
kaide-recon/
├── README.md
├── requirements.txt                          (google-genai, requests, playwright, python-dotenv)
├── dossiers/
│   ├── _template/
│   │   └── intake_checklist.md
│   ├── james-he-artificial-societies/
│   │   ├── raw/
│   │   │   ├── linkedin/                     (gitignored — sensitive)
│   │   │   │   ├── profile.pdf               (manual)
│   │   │   │   ├── activity_screenshots/     (manual)
│   │   │   │   └── li_jobs.md                (manual)
│   │   │   ├── twitter.md                    (Playwright via Nitter)
│   │   │   ├── personal_site.md              (Playwright)
│   │   │   ├── podcasts/                     (Playwright + transcription)
│   │   │   ├── hn_comments.md                (HN Algolia API — no automation needed)
│   │   │   ├── conference_talks.md           (Playwright + transcripts)
│   │   │   ├── yc_page.md                    (Playwright)
│   │   │   ├── company_jobs.md               (Playwright)
│   │   │   └── news_coverage.md              (Playwright)
│   │   ├── intake_checklist.md
│   │   └── dossier.md                        (Deep Research Max output)
│   └── ...
├── scripts/
│   ├── research.py                           (Step 2: Deep Research Max via Interactions API)
│   ├── route.py                              (Gemini 3 Flash classifier for delta worth)
│   ├── gather_twitter.py                     (Playwright → Nitter)
│   ├── gather_hn.py                          (HN Algolia REST API)
│   ├── gather_podcasts.py                    (Playwright → YouTube/Spotify + transcription)
│   ├── gather_yc.py                          (Playwright → YC directory)
│   ├── gather_jobs.py                        (Playwright → company careers pages)
│   ├── gather_news.py                        (Playwright → Google News)
│   ├── orchestrate.py                        (asyncio fan-out across gather_*)
│   ├── index_to_nia.py                       (Step 3: POST /v2/sources)
│   └── query_dossier.py                      (Step 4: emits Claude+Nia MCP prompt)
├── prompts/
│   ├── deep_research_prompt.md
│   ├── outreach_angle_prompt.md
│   ├── router_prompt.md                      (Flash classifier rubric)
│   └── kaide_labs_positioning.md             (locked positioning, injected everywhere)
├── .gitignore
└── .env                                      (GEMINI_API_KEY, NIA_API_KEY, GITHUB_TOKEN)
```

---

## 3. Intake Checklist Template

Drop this into every `dossiers/{founder_name}/intake_checklist.md`:

```markdown
# Intake: {Founder Name} / {Company}

**Status:** {gathering | synthesizing | indexed | dossier-complete}
**Started:** {YYYY-MM-DD}
**Outreach target date:** {YYYY-MM-DD}
**Last interaction_id:** {fill in after research.py runs — used for cheap follow-ups}

## Manual capture (LinkedIn — do not automate, ban risk)
- [ ] Profile PDF (LinkedIn three-dot menu → Save to PDF)
- [ ] Activity tab screenshots (last 30-60 days)
- [ ] Featured section
- [ ] Recommendations
- [ ] Recent endorsements/reactions (last 30 days)
- [ ] Open roles on LinkedIn Jobs filtered to this company

## Agent capture (Playwright)
- [ ] Twitter timeline + replies (last 90 days, via Nitter)
- [ ] Personal website / blog
- [ ] Top 2 podcast appearances (transcribed)
- [ ] Substack/Medium archive
- [ ] HN comment history (HN Algolia API)
- [ ] Conference talks (YouTube + transcripts)
- [ ] YC company page (if YC)
- [ ] Open job postings on company careers page (raw HTML capture)
- [ ] Recent news coverage / TechCrunch mentions
- [ ] Press releases / official announcements last 12 months

## Nia indexing (POST /v2/sources)
- [ ] Founder's public GitHub repos    (type=repository)
- [ ] Company GitHub org repos         (type=repository)
- [ ] Company docs site                (type=documentation)
- [ ] Dossiers repo refresh            (type=repository, after dossier.md committed)

## Synthesis
- [ ] Deep Research Max run with all raw/ artifacts uploaded via Files API
- [ ] dossier.md generated, reviewed, committed to repo
- [ ] interaction_id saved above for future follow-ups

## Outreach drafting
- [ ] Pain points identified (3-5 specific bottlenecks the agent surfaced)
- [ ] Outreach angles drafted (Claude via Nia MCP, 2-3 variants)
- [ ] Locked outreach copy
- [ ] Sent — date logged here

## Post-send tracking
- [ ] Vidyard view logged (if applicable)
- [ ] LinkedIn profile view logged
- [ ] Response received (date, channel, content)
- [ ] Outcome: {no response | declined | call booked | engagement closed}
```

---

## 4. The Locked Kaide Labs Positioning (injected into all prompts)

`prompts/kaide_labs_positioning.md`:

```markdown
Kaide Labs is a forward-deployed engineering strike team for B2B AI startups.

CORE OFFER:
- Bolt-on sidecars on rapid sprint cycles (typical: 1 week)
- Productized engagement: £10k/month, 50% upfront, first month refundable
- I embed as the FDE; the team doesn't have to hire one
- DMZ rule: never touch the client's core product, IP, or codebase
- Sidecars sit upstream or alongside the core product, solving specific
  enterprise integration bottlenecks

WHO IT'S FOR:
- Post-seed B2B AI startups (typically YC W25/S25/W26 era)
- Teams of 5-15 where the founders are still in the code
- Companies whose product works but whose enterprise integration story
  is the bottleneck slowing sales cycles
- Specifically: where the team can't justify hiring a full FDE yet but
  needs FDE-quality work to close enterprise deals

OUTREACH ANGLE LOGIC:
The cold pitch should reference a SPECIFIC public bottleneck the founder
or company has expressed — a pain point they've named in a podcast, a
job they've been trying to fill for 60+ days, an integration they've
publicly committed to but haven't shipped, an enterprise feature their
customers are asking for.

The angle is NOT generic ("we help startups scale"). It is specific
("you mentioned on Lenny's Podcast that calibration accuracy at F100
scale is your wedge — I built a sidecar that addresses exactly that
attribute, here's the demo").

The artifact (a specific demo built against their actual problem) is
the proof. The cold pitch is a delivery mechanism for the artifact.
```

---

## 5. Gemini Deep Research Max Prompt Template

`prompts/deep_research_prompt.md`:

```markdown
You are doing comprehensive recon on a founder for a hyper-personalized
cold outreach campaign.

TARGET: {founder_name}, {role}, {company}

CONTEXT ABOUT KAIDE LABS:
{inject kaide_labs_positioning.md here}

RAW ARTIFACTS PROVIDED AS INPUT (uploaded via the Files API and attached
as `file_data` parts on this interaction):
- LinkedIn profile PDF (manual capture)
- Twitter timeline + replies
- Personal website content
- Podcast transcripts
- HN comments
- Substack/Medium posts
- YC page (if applicable)
- Open job postings at the company
- Recent news coverage
- Conference talk transcripts (if any)

You also have grounded Google Search available — use it freely for
anything missing from the artifacts.

YOUR JOB:
Produce a comprehensive founder dossier as cited markdown. The dossier
must answer the following questions specifically. Cite every claim with
the source URL.

## 1. Founder Background
## 2. Company Snapshot
## 3. Stated Pain Points and Bottlenecks
## 4. Technical Decisions and Preferences
## 5. Enterprise Integration Surface (KAIDE LABS-SPECIFIC)
## 6. Recommended Outreach Angle  (3 angles, ranked)
## 7. Red Flags / Gaps

OUTPUT FORMAT:
Markdown. Cited inline. Save as dossier.md. Maximum 4000 words. The
dossier should be readable in 10 minutes by a busy founder making a
go/no-go decision on whether to pitch this person.
```

(Section bodies are intentionally identical to the prior version — see
git history for the full per-section instructions; only the artifact
delivery mechanism changed.)

---

## 6. Build Sequence (Today)

### Step 0 — Repo bootstrap (15 min)

```bash
mkdir kaide-recon && cd kaide-recon
git init
mkdir -p dossiers/_template scripts prompts
touch README.md .env

cat > .gitignore <<'EOF'
.env
venv/
__pycache__/
dossiers/*/raw/linkedin/
*.pdf
EOF

cat > requirements.txt <<'EOF'
google-genai>=1.0.0
requests>=2.32.0
playwright>=1.59.0
python-dotenv>=1.0.0
EOF

python -m venv venv && source venv/bin/activate   # PowerShell: .\venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

Drop the prompts (positioning + deep research template + router rubric) into `prompts/`. Drop the intake template into `dossiers/_template/`. Push to GitHub as `kaide-recon` (private).

### Step 1 — Build research.py (validates the API surface)

Single-purpose script: takes founder name + company + path to raw/ folder, uploads each file via the Files API, calls the Interactions API with `agent="deep-research-max-preview-04-2026"` and `background=True`, polls until complete, saves output to `dossier.md`.

```python
# scripts/research.py
import os, sys, time, glob
from pathlib import Path
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

AGENT = "deep-research-max-preview-04-2026"
TERMINAL = {"completed", "failed", "cancelled"}


def run_research(founder_name: str, company: str, raw_dir: str) -> Path:
    # 1. Upload every file in raw/ via the Files API. The returned File
    #    objects are accepted directly as parts of the Interactions input.
    artifacts = []
    for path in glob.glob(f"{raw_dir}/**/*", recursive=True):
        p = Path(path)
        if p.is_file() and "linkedin/activity_screenshots" not in str(p):
            artifacts.append(client.files.upload(file=str(p)))

    # 2. Compose prompt.
    prompt = Path("prompts/deep_research_prompt.md").read_text()
    positioning = Path("prompts/kaide_labs_positioning.md").read_text()
    prompt = (prompt
              .replace("{founder_name}", founder_name)
              .replace("{company}", company)
              .replace("{inject kaide_labs_positioning.md here}", positioning))

    # 3. Kick off Deep Research Max in background mode (required for agents).
    interaction = client.interactions.create(
        agent=AGENT,
        input=[prompt, *artifacts],
        background=True,
    )
    print(f"Interaction started: {interaction.id}")

    # 4. Poll. Status values: in_progress | completed | failed | cancelled.
    while True:
        current = client.interactions.get(interaction.id)
        if current.status in TERMINAL:
            break
        print(f"  status={current.status} — sleeping 30s")
        time.sleep(30)

    if current.status != "completed":
        raise RuntimeError(f"Research {current.status}: {getattr(current, 'error', None)}")

    # 5. Save output. Final report is the last output's text.
    dossier_path = Path(raw_dir).parent / "dossier.md"
    dossier_path.write_text(current.outputs[-1].text, encoding="utf-8")

    # 6. Stash the interaction id alongside so re-pitches can use
    #    previous_interaction_id for cheap follow-ups.
    (Path(raw_dir).parent / ".interaction_id").write_text(interaction.id)
    print(f"✓ Dossier saved to {dossier_path} (interaction_id={interaction.id})")
    return dossier_path


if __name__ == "__main__":
    run_research(sys.argv[1], sys.argv[2], sys.argv[3])
```

**First test target: James He at Artificial Societies.** Test the full pipeline against him before building any Playwright automation.

### Step 2 — Build the gather scripts (Playwright async, one at a time)

Priority order based on signal-to-effort ratio:

1. `gather_yc.py` (highest signal — YC pages have structured data)
2. `gather_jobs.py` (highest signal for Kaide Labs — tells you what bottlenecks they have)
3. `gather_twitter.py` (Nitter — public, scrapeable, founder voice)
4. `gather_hn.py` (HN Algolia REST API — no browser needed)
5. `gather_podcasts.py` (transcription is the slow part; batch overnight)
6. `gather_news.py` (Google News headlines + summaries)

Canonical Playwright async skeleton for the browser-driven gatherers:

```python
# scripts/gather_twitter.py
import asyncio, sys
from pathlib import Path
from playwright.async_api import async_playwright

async def gather(handle: str, raw_dir: str) -> None:
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context(user_agent="Mozilla/5.0 (kaide-recon)")
        page = await context.new_page()
        await page.goto(f"https://nitter.net/{handle}", timeout=30_000)
        # ... extract timeline + replies, paginate, write markdown ...
        out = Path(raw_dir) / "twitter.md"
        out.write_text("# Twitter\n\n" + "...captured content...", encoding="utf-8")
        await browser.close()

if __name__ == "__main__":
    handle, raw_dir = sys.argv[1], sys.argv[2]
    asyncio.run(gather(handle, raw_dir))
```

`gather_hn.py` skips Playwright entirely — uses `requests` against `https://hn.algolia.com/api/v1/search_by_date?author=<handle>`.

### Step 3 — Build orchestrate.py (parallelize the gathering)

```python
# scripts/orchestrate.py
import asyncio, sys
from pathlib import Path

GATHERERS = ["gather_yc.py", "gather_jobs.py", "gather_twitter.py",
             "gather_hn.py", "gather_news.py"]


async def run_gatherer(script: str, founder: str, company: str, raw_dir: str):
    proc = await asyncio.create_subprocess_exec(
        "python", f"scripts/{script}", founder, company, raw_dir,
        stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    print(f"{script}: rc={proc.returncode}")
    return stdout, stderr


async def main(founder: str, company: str):
    raw_dir = f"dossiers/{founder.lower().replace(' ', '-')}/raw"
    Path(raw_dir).mkdir(parents=True, exist_ok=True)
    await asyncio.gather(*[
        run_gatherer(s, founder, company, raw_dir) for s in GATHERERS
    ])


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
```

### Step 3.5 — Build route.py (Gemini 3 Flash routing)

Cheap pre-filter that decides whether a freshly-gathered artifact is substantive enough to (a) keep in raw/ for the next Deep Research Max run, or (b) trigger an immediate re-synthesis on a stale dossier.

```python
# scripts/route.py
import os, sys
from pathlib import Path
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
ROUTER_MODEL = "gemini-3-flash-preview"


def classify(artifact_path: str) -> str:
    rubric = Path("prompts/router_prompt.md").read_text()
    artifact = Path(artifact_path).read_text(encoding="utf-8", errors="ignore")
    resp = client.models.generate_content(
        model=ROUTER_MODEL,
        contents=[rubric, "\n\n---\nARTIFACT:\n", artifact[:200_000]],
    )
    # Expected verdicts: KEEP | RE_SYNTHESIZE | SKIP
    return resp.text.strip().splitlines()[0]


if __name__ == "__main__":
    print(classify(sys.argv[1]))
```

### Step 4 — Build index_to_nia.py (Nia v2 unified `/v2/sources`)

Nia v2 consolidated repo, documentation, paper, dataset, local-folder, and Slack indexing under a single `POST /v2/sources` endpoint with a `type` discriminator. The legacy `POST /v2/repositories` shape is retained as an alias but new code should target `/v2/sources`.

```python
# scripts/index_to_nia.py
import os, sys, requests

BASE = "https://apigcp.trynia.ai/v2"
HEADERS = lambda: {
    "Authorization": f"Bearer {os.environ['NIA_API_KEY']}",
    "Content-Type": "application/json",
}


def index_repository(owner_slash_name: str, branch: str = "main"):
    body = {"type": "repository", "repository": owner_slash_name, "branch": branch}
    r = requests.post(f"{BASE}/sources", headers=HEADERS(), json=body, timeout=30)
    r.raise_for_status()
    return r.json()


def index_documentation(url: str):
    body = {"type": "documentation", "url": url}
    r = requests.post(f"{BASE}/sources", headers=HEADERS(), json=body, timeout=30)
    r.raise_for_status()
    return r.json()


if __name__ == "__main__":
    kind, target = sys.argv[1], sys.argv[2]   # kind in {repo, docs}
    if kind == "repo":
        print(index_repository(target))
    elif kind == "docs":
        print(index_documentation(target))
    else:
        sys.exit(f"unknown kind: {kind}")
```

Used for: founder's GitHub repos, company GitHub org, company docs site, the kaide-recon repo itself.

### Step 5 — Build query_dossier.py (Claude via Nia MCP)

`query_dossier.py` emits a prompt designed for a Claude session that has the Nia MCP server attached. Nia v2's `/v2/search` endpoint accepts `mode: "universal"` to search across every indexed source in one call (the prior `/v2/universal-search` shape is deprecated).

```python
# scripts/query_dossier.py
import sys

QUERY_TEMPLATE = """
Using the Nia MCP server (https://apigcp.trynia.ai/mcp), run a
universal search (POST /v2/search with mode=universal) for the
indexed dossier on {founder_name} at {company}.

Cross-reference these sources:
- The synthesized dossier.md (in the kaide-recon repo)
- Their public GitHub repos
- Their company's docs site if indexed

Output:
1. The 3 strongest cold-outreach angles, ranked by how specific the
   public bottleneck they reference is.
2. For each angle, draft a complete email or InMail message in
   Hafeedh's voice (operator-grade, direct, brief, with a specific
   demo artifact mentioned by name).
3. Flag any red flags from the dossier I should reconsider before
   sending.

Hafeedh's voice rules:
- Lead with the work, not the introduction
- One specific hook tied to a public statement they've made
- Hedge intelligently ("I don't know your X, happy to be wrong")
- Engagement model and pricing stated factually
- Soft close, no high-pressure CTA
- 250-400 words total
"""

if __name__ == "__main__":
    print(QUERY_TEMPLATE.format(founder_name=sys.argv[1], company=sys.argv[2]))
```

---

## 7. Validation Path (today)

End-of-Sunday goal: pipeline runs end-to-end on James He at AS as the test case.

```
[ ] kaide-recon repo created, pushed to GitHub
[ ] requirements.txt installed, playwright chromium installed
[ ] Prompts dropped in (positioning, deep research, router rubric, outreach angle)
[ ] Intake template in place
[ ] dossiers/james-he-artificial-societies/raw/ populated:
    - Manual: LinkedIn PDF
    - Manual: Activity screenshots
    - A few basic artifacts to test multimodal grounding
[ ] research.py written and tested against James (one Deep Research Max
    call, ~15 min, ~$5)
[ ] dossier.md committed to repo
[ ] kaide-recon repo indexed via POST /v2/sources type=repository
[ ] Nia MCP queried via Claude — outputs an outreach angle for a
    SECOND prospect (not James)
```

If that works end-to-end, the architecture is validated. Then build the Playwright gather scripts during the week.

---

## 8. Cost Model (verified May 2026)

| Item | Cost | Frequency |
|---|---|---|
| Deep Research Max (`deep-research-max-preview-04-2026`) | ~$5/run (900k input + 80k output ≈ $4.80; ~160 grounded search queries included) | Per founder, one-time |
| Gemini 3 Flash routing (`gemini-3-flash-preview`) | $0.50/M in + $3/M out — typically <$0.10 per founder | Per artifact |
| Files API uploads | Free | Per artifact |
| Nia indexing (`/v2/sources`) | Free tier covers low-volume internal use | Per source, one-time |
| Nia search (`/v2/search`) | Within free tier limits at low volume | Ongoing |
| Playwright / browser automation | $0 (self-hosted, headless Chromium) | Per run |
| Manual capture time | ~10 min / founder | Per founder |
| **Per-founder total** | **~$5–7 + 30 min active human time** | One-time per target |

At 10 founders/quarter: ~$50–70/quarter in API costs. Trivial against the £10k engagement value of even one closed sale.

---

## 9. Endpoint Reference (canonical, May 2026)

| Action | Method + Endpoint | Notes |
|---|---|---|
| Start Deep Research Max | `POST /v1beta/interactions` | `agent="deep-research-max-preview-04-2026"`, `background=true`. SDK: `client.interactions.create(...)`. |
| Poll interaction | `GET /v1beta/interactions/{id}` | SDK: `client.interactions.get(id)`. Status: `in_progress|completed|failed|cancelled`. |
| Continue interaction | `POST /v1beta/interactions` with `previous_interaction_id` | Cheap follow-up on an existing dossier. |
| Upload file for grounding | Files API via SDK `client.files.upload(file=path)` | Returns a `File` ref; pass directly into `input=[...]`. |
| Index source (repo/docs/paper/dataset) | `POST /v2/sources` | Body: `{"type":"repository","repository":"owner/name"}` or `{"type":"documentation","url":"..."}`. |
| Universal search across indexed sources | `POST /v2/search` | Body: `{"mode":"universal","query":"..."}`. Replaces deprecated `/v2/universal-search`. |
| Sandbox (ephemeral repo search) | `POST /v2/sandbox/search` | For one-off public-repo queries without indexing. |

---

## 10. The Honest Operating Principle

**One closed sale pays for everything 100x over.**

The whole pipeline costs less than $80 to run for an entire quarter. Your first £10k engagement returns 100x that in month one alone.

Build the pipeline. Run it on James first as a validation. Then run it on Wexler as your real first commercial use. Then ten more after that.

Rest comes after the first sale. Until then, the work is the work.
