# PHASE 1 SPEC — `kaide-recon/scripts/`

**Codename:** `kaide-recon`
**Author:** Principal Systems Architect (handoff doc for execution agent)
**Status:** Phase 1 blueprint — implementation-ready, no code in this file
**Audience:** Execution agent (Claude Code / Codex) writing the actual scripts
**Companion docs:** `PRD.md`, `design_doc.md`
**Last revised:** 2026-05-04
**Source verification:** Nia-indexed `docs.trynia.ai`, `ai.google.dev/gemini-api/docs`, `playwright.dev/python/docs`, plus the canonical endpoint table in `design_doc.md` §9.

---

## 0. Scope Lock

Phase 1 implements the **4-layer architecture for a single prospect run**, end-to-end, with **James He at Artificial Societies** as the validation target. Every requirement below is scoped to that. This spec deliberately excludes:

- Web UI / dashboard
- Mass outreach
- Multi-prospect batch orchestration
- Any LinkedIn automation (manual capture only — locked by PRD §3, §8.1)
- Pattern-detection across dossiers
- Outcome tracking integrations
- Authenticated-surface scraping of any kind

The execution agent must not introduce features outside this list. If a deferred feature feels tempting, the answer is no — see PRD §11.

The deliverable of Phase 1 is a working `scripts/` directory that, given a populated `dossiers/{slug}/raw/` folder, produces `dossiers/{slug}/dossier.md` and indexes the resulting state into Nia, with the dossier reachable via Claude+Nia MCP universal search.

---

## 1. Engineering Discipline (Internal-Tool Mode)

PRD §3, §8.2: This is an internal tool. Apply the following discipline:

| Rule | Implication for the executing agent |
|---|---|
| Ship rough, iterate on real use | No retry/backoff frameworks beyond a single `try/except` around network I/O. No abstract base classes. No plugin systems. |
| No premature abstraction | Each `gather_*.py` is a flat script. No shared `BaseGatherer` class. Three similar files is better than one clever hierarchy. |
| Fail loud, fail fast | Scripts exit non-zero on any failure. Print the offending URL/path/payload. Do not swallow exceptions to "keep going." |
| No tests in Phase 1 | Validation is the James end-to-end run. Pytest scaffolding is out of scope. |
| No logging library | `print()` is the logging contract. Prefix lines with the script name when fanned out by `orchestrate.py`. |
| Idempotent re-runs | Every script must be safe to re-run. Re-running `research.py` overwrites `dossier.md`; re-running `index_to_nia.py` is allowed to 409 (handle gracefully — see §6.4). |

---

## 2. Dependency Manifest

Single `requirements.txt` at repo root, pinned to the values established in `design_doc.md` §6 Step 0. Phase 1 adds nothing beyond what the design doc already specifies.

```
google-genai>=1.0.0
requests>=2.32.0
playwright>=1.59.0
python-dotenv>=1.0.0
```

**Per-script dependency map** (the executing agent must not import anything outside this map; if a script needs more, escalate before adding it):

| Script | stdlib | google-genai | requests | playwright | python-dotenv |
|---|---|---|---|---|---|
| `research.py` | os, sys, time, glob, pathlib, mimetypes | ✓ | — | — | ✓ (load `.env`) |
| `route.py` | os, sys, pathlib | ✓ | — | — | ✓ |
| `index_to_nia.py` | os, sys, json | — | ✓ | — | ✓ |
| `query_dossier.py` | sys, pathlib | — | — | — | — |
| `orchestrate.py` | asyncio, sys, pathlib, subprocess | — | — | — | ✓ |
| `gather_yc.py` | asyncio, sys, pathlib | — | — | ✓ | — |
| `gather_jobs.py` | asyncio, sys, pathlib | — | — | ✓ | — |
| `gather_twitter.py` | asyncio, sys, pathlib | — | — | ✓ | — |
| `gather_hn.py` | sys, pathlib, json | — | ✓ | — | — |
| `gather_news.py` | asyncio, sys, pathlib | — | — | ✓ | — |
| `gather_podcasts.py` | asyncio, sys, pathlib | — | — | ✓ | — |

`.env` loading: every script that needs `GEMINI_API_KEY` or `NIA_API_KEY` calls `dotenv.load_dotenv()` at module top before reading `os.environ`. `gather_*.py` scripts do not need this (they hit no auth'd APIs). `gather_hn.py` is unauth'd HN Algolia.

`playwright install chromium` must be run once after `pip install` — bootstrap doc, not a runtime dep.

---

## 3. Data Structures

These are the only data shapes Phase 1 cares about. The executing agent must not introduce additional intermediate types (no `Prospect` dataclass, no `RawArtifact` model — keep it flat).

### 3.1 On-disk layout per prospect

```
dossiers/{slug}/
├── intake_checklist.md         # copied from dossiers/_template/, manually edited
├── raw/
│   ├── linkedin/               # gitignored
│   │   ├── profile.pdf
│   │   ├── activity_screenshots/
│   │   │   ├── 01.png
│   │   │   ├── 02.png
│   │   │   └── ...
│   │   └── li_jobs.md
│   ├── twitter.md              # gather_twitter.py output
│   ├── personal_site.md        # manual or future gatherer
│   ├── hn_comments.md          # gather_hn.py output
│   ├── yc_page.md              # gather_yc.py output
│   ├── company_jobs.md         # gather_jobs.py output
│   ├── news_coverage.md        # gather_news.py output
│   └── podcasts/               # gather_podcasts.py output dir
│       ├── 01_lennys_podcast.md
│       └── ...
├── dossier.md                  # research.py output
└── .interaction_id             # research.py side-effect, used by V1.1 follow-ups
```

`{slug}` derivation: `founder_name.lower().replace(' ', '-') + '-' + company.lower().replace(' ', '-')`. Example: `james-he-artificial-societies`. The slug is computed in `orchestrate.py` and passed positionally to every gatherer.

### 3.2 Multimodal input shape passed to Gemini

`research.py` walks `raw/` recursively and uploads every file (excluding `linkedin/activity_screenshots/`, see §4.2 for rationale). The Files API returns `File` objects. The Interactions API `input` parameter is a list whose elements are **either** strings (prompt text) **or** `File` objects (multimodal grounding). The exact in-memory shape:

```
input = [
    str,                # the composed prompt (prompt template + positioning)
    File,               # uploaded raw/linkedin/profile.pdf  (mime: application/pdf)
    File,               # uploaded raw/twitter.md            (mime: text/markdown)
    File,               # uploaded raw/hn_comments.md
    File,               # uploaded raw/yc_page.md
    File,               # uploaded raw/company_jobs.md
    File,               # uploaded raw/news_coverage.md
    File,               # uploaded raw/podcasts/01_*.md
    ...
]
```

**Verified MIME handling:** `client.files.upload(file=path)` infers MIME from extension. Phase 1 only needs `.pdf`, `.md`, `.txt`, `.html`, `.png`, `.jpg`. Do not pass binary blobs of unknown type — skip them with a `print` warning. The only deliberately-skipped subtree is `linkedin/activity_screenshots/` (see §4.2).

**No chunking.** Deep Research Max accepts up to ~900k input tokens per design doc §8 cost model. A typical prospect's raw/ folder is well under this. If a single artifact exceeds 200k chars, truncate at 200k and append a `[…truncated]` marker — do not attempt to split it across multiple Files.

### 3.3 Gather-script output contract

Every `gather_*.py` writes exactly one of:
- A single markdown file at `raw/{source}.md`, **or**
- A single directory `raw/{source}/` with one markdown file per item (used only by `gather_podcasts.py`).

The markdown file structure is fixed:

```markdown
# {Source} — {founder or company}

**Captured:** {ISO-8601 UTC timestamp}
**Source URL:** {canonical URL the gatherer hit}

---

{captured content, lightly cleaned, no further processing}
```

This shape is what Deep Research Max sees as grounding. It is also what `route.py` reads to classify. Do not deviate — the synthesis prompt assumes this header presence.

### 3.4 Router verdict shape

`route.py` emits a single line on stdout: `KEEP` | `RE_SYNTHESIZE` | `SKIP`. No JSON, no rationale, no extra lines. If the model returns multi-line output (it sometimes does), `route.py` returns the first non-empty line. If the first line is none of the three valid tokens, `route.py` exits non-zero with `print` of the malformed verdict.

---

## 4. Nia API Payload Shapes (verified against `docs.trynia.ai`)

Base URL: `https://apigcp.trynia.ai/v2`. Auth header: `Authorization: Bearer ${NIA_API_KEY}`. Content-Type: `application/json` on all POSTs.

### 4.1 `POST /v2/sources` — index a repository

```json
{
  "type": "repository",
  "repository": "{owner}/{name}",
  "branch": "main"
}
```

- `type` is the discriminator. Required.
- `repository` is `owner/name`, never a full URL. Required.
- `branch` defaults to the repo default branch when omitted; pass it explicitly for determinism.
- Response: `{"id": "<uuid>", "type": "repository", "status": "processing|completed", ...}`. `status=processing` is normal — Nia indexes async. Do not poll in Phase 1; trust the returned 200 and move on.

### 4.2 `POST /v2/sources` — index a documentation site

```json
{
  "type": "documentation",
  "url": "https://docs.{company}.com"
}
```

- `url` should be the **root** docs URL (Nia crawls from there; verified per Nia capability docs: "always index the root link").
- For Phase 1 this is used for the company docs site only (e.g. James's company's docs root if it exists). If no docs site exists, skip this call — do not synthesize a docs URL.

### 4.3 Sources `index_to_nia.py` must call for one prospect run

In order, after `dossier.md` is committed and pushed:

| # | Source | Type | Body |
|---|---|---|---|
| 1 | The kaide-recon dossiers repo itself | `repository` | `{"type":"repository","repository":"{your-gh-user}/kaide-recon","branch":"master"}` |
| 2 | Founder's primary public GitHub repo (if any) | `repository` | `{"type":"repository","repository":"<founder-handle>/<repo>","branch":"main"}` — caller-supplied identifier |
| 3 | Company GitHub org's most-active public repo | `repository` | `{"type":"repository","repository":"<org>/<repo>","branch":"main"}` |
| 4 | Company docs site root (if exists) | `documentation` | `{"type":"documentation","url":"https://docs.<company>.com"}` |

Sources 2/3/4 are **optional inputs** to `index_to_nia.py` — the script does not auto-discover them. The operator passes them on the CLI.

### 4.4 `POST /v2/search` — universal mode (queried by Claude via MCP, not by Phase 1 scripts directly)

```json
{
  "mode": "universal",
  "query": "..."
}
```

Phase 1 scripts do not call `/v2/search` directly. `query_dossier.py` only emits a prompt that **instructs Claude (with Nia MCP attached) to perform** the search. This boundary is intentional — see §6.5.

### 4.5 Error handling

- `200/201` → success, parse JSON, return.
- `409 Conflict` (already indexed) → treat as success. Print `"already indexed: {target}"` and continue. This is the most common non-success state.
- `4xx` other → print response body, exit non-zero.
- `5xx` → one retry after 5s, then exit non-zero. No exponential backoff machinery.
- Network exception (`requests.exceptions.RequestException`) → one retry after 5s, then exit non-zero.

---

## 5. Gemini API Payload Shapes (verified against `ai.google.dev/gemini-api/docs`)

### 5.1 Files API upload (used by `research.py`)

SDK call: `client.files.upload(file="{path}")`. Returns a `File` object whose `.name` field is the resource handle (`files/{id}`). The returned object is passed **directly** as a list element into `client.interactions.create(input=[...])`. The SDK handles serializing it as a `file_data` part on the wire (verified: Gemini multimodal generateContent accepts `inlineData` and `fileData` parts — the SDK chooses `fileData` for uploaded `File` refs, which is the path we want for >20MB or for reuse).

### 5.2 Interactions API — start Deep Research Max

Endpoint: `POST /v1beta/interactions` (per design_doc §9). SDK call:

```
client.interactions.create(
    agent="deep-research-max-preview-04-2026",
    input=[<prompt_str>, <File_1>, <File_2>, ...],
    background=True,
)
```

- `agent` is a **locked** string (PRD §3, design_doc §1.1). The execution agent must not parameterize this — hardcode it as a module-level constant.
- `background=True` is required for the deep-research-max agent (long-running).
- Returns an `Interaction` with `.id` (string) and `.status` (`in_progress` initially).

### 5.3 Interactions API — poll

SDK: `client.interactions.get(interaction_id)`. Status enum: `in_progress | completed | failed | cancelled`. Terminal set: `{completed, failed, cancelled}`.

Poll cadence: **30 seconds**. Do not get clever. A typical run is ~15 minutes (30 polls). On `failed` or `cancelled`, raise `RuntimeError` with `getattr(current, 'error', None)` included.

### 5.4 Interactions output shape

`current.outputs` is a list. The synthesized markdown report is `current.outputs[-1].text`. This is the only field Phase 1 reads. The agent must not parse intermediate steps, citations metadata, or tool-call traces — those are useful in V2 but not Phase 1.

### 5.5 Generate Content (used by `route.py`)

SDK: `client.models.generate_content(model="gemini-3-flash-preview", contents=[...])`. `contents` for routing is a list of strings — no Files, no multimodal. Read response via `resp.text`.

Model lock: `gemini-3-flash-preview` — hardcoded module-level constant. Do not parameterize.

---

## 6. File-by-File Specification

### 6.1 `scripts/research.py` — Synthesis (Layer 2)

**Single responsibility:** Given a populated `raw/` folder, run Deep Research Max once, save `dossier.md` and `.interaction_id`.

**CLI:**
```
python scripts/research.py "<founder_name>" "<company>" "<path/to/raw>"
```

**Module-level constants:**
- `AGENT = "deep-research-max-preview-04-2026"`
- `ROUTER_MODEL` is **not** in this file — it lives in `route.py`.
- `TERMINAL_STATUSES = {"completed", "failed", "cancelled"}`
- `POLL_INTERVAL_SECONDS = 30`
- `MAX_ARTIFACT_BYTES = 200_000` (truncation guard, see §3.2)

**Logic flow:**

1. **Load env.** `dotenv.load_dotenv()`. Read `GEMINI_API_KEY` from `os.environ`. Fail fast if missing.
2. **Validate inputs.** `raw_dir` must exist and contain ≥1 file. If empty, exit non-zero with message `"raw/ is empty — run orchestrate.py first or capture LinkedIn manually"`.
3. **Walk raw/.** Use `glob.glob(f"{raw_dir}/**/*", recursive=True)`. For each path:
   - Skip if not a file.
   - Skip if path contains `linkedin/activity_screenshots` (rationale: screenshots are visual context, not text grounding; uploading them works but consumes input budget for marginal signal — defer to V1.1).
   - Skip if extension not in `{.pdf, .md, .txt, .html, .htm, .png, .jpg, .jpeg}`. Print a warning for skipped files.
   - If file size > `MAX_ARTIFACT_BYTES` and extension is text-like, read, truncate, write to a sibling `.truncated.md` in a tempdir, upload the truncated copy. Do not modify the original.
4. **Upload via Files API.** Collect returned `File` objects into `artifacts: list`.
5. **Compose prompt.** Read `prompts/deep_research_prompt.md`. Read `prompts/kaide_labs_positioning.md`. Substitute `{founder_name}`, `{company}`, and the literal token `{inject kaide_labs_positioning.md here}` (yes, including the curly braces and surrounding text — the prompt template is locked to that token, design_doc §5).
6. **Kick off interaction.** `client.interactions.create(agent=AGENT, input=[prompt, *artifacts], background=True)`. Print the returned `interaction.id`.
7. **Poll loop.** Every 30s call `client.interactions.get(id)`. Print `status=...`. Break on terminal status.
8. **Handle non-completed terminals.** On `failed`/`cancelled`, raise `RuntimeError`. Do not retry — Deep Research Max runs are expensive ($5); a retry on opaque failure burns budget.
9. **Save outputs.**
   - `Path(raw_dir).parent / "dossier.md"` ← `current.outputs[-1].text`
   - `Path(raw_dir).parent / ".interaction_id"` ← `interaction.id`
10. **Print success line** with dossier path and interaction id.

**Failure modes the agent must surface clearly:**
- Missing `GEMINI_API_KEY` → exit 2, message: `"GEMINI_API_KEY not set"`.
- `raw_dir` not found → exit 2.
- Files API upload error → re-raise with the offending path printed.
- Interaction `failed` → exit 1, print `error` field if present.

**Out of scope for Phase 1:** `previous_interaction_id` chaining (deferred to V1.1.4). Streaming output. Custom safety settings. Citation extraction.

---

### 6.2 `scripts/route.py` — Cheap Triage (Layer 1.5)

**Single responsibility:** Given an artifact path, classify whether it's worth keeping/re-synthesizing/skipping using `gemini-3-flash-preview`.

**CLI:**
```
python scripts/route.py "<path/to/artifact.md>"
```

**Module-level constants:**
- `ROUTER_MODEL = "gemini-3-flash-preview"`
- `MAX_INPUT_CHARS = 200_000`
- `VALID_VERDICTS = {"KEEP", "RE_SYNTHESIZE", "SKIP"}`

**Logic flow:**

1. Load env, init `genai.Client`.
2. Read `prompts/router_prompt.md` (the rubric — design_doc §6 step 3.5; the rubric content is owned by the prompts dir, not by this script).
3. Read the target artifact, truncate to `MAX_INPUT_CHARS`.
4. Call `client.models.generate_content(model=ROUTER_MODEL, contents=[rubric, "\n\n---\nARTIFACT:\n", artifact])`.
5. Take `resp.text.strip().splitlines()[0].strip().upper()`.
6. If verdict not in `VALID_VERDICTS`, exit non-zero, print malformed output for debugging.
7. Print verdict to stdout. Exit 0.

**Caller contract:** `orchestrate.py` does **not** call `route.py` in Phase 1. Phase 1 routing is operator-driven: the operator runs `route.py` manually against suspect artifacts after a re-pitch. This is intentional — auto-routing every artifact is a V1.1 hardening, premature for the validation run.

---

### 6.3 `scripts/orchestrate.py` — Gathering Fan-Out (Layer 1)

**Single responsibility:** Given a founder name and company, create the dossier directory tree and run all gather scripts in parallel via `asyncio.create_subprocess_exec`. **Does not run synthesis or indexing** — those are explicit operator-triggered next steps.

**CLI:**
```
python scripts/orchestrate.py "<founder_name>" "<company>"
```

Optional positional 3rd arg: `<twitter_handle>` (defaults to founder slug if absent — but `gather_twitter.py` will fail loudly if that guess is wrong, which is the intended behavior).

**Module-level constants:**
- `GATHERERS` — ordered list of script filenames. The order matches PRD signal-priority (design_doc §6 step 2):
  ```
  GATHERERS = [
      "gather_yc.py",
      "gather_jobs.py",
      "gather_twitter.py",
      "gather_hn.py",
      "gather_news.py",
      # gather_podcasts.py is excluded from default fan-out — too slow, run manually
  ]
  ```

**Logic flow:**

1. Compute `slug = f"{founder.lower().replace(' ', '-')}-{company.lower().replace(' ', '-')}"`.
2. Compute `prospect_dir = Path("dossiers") / slug`.
3. Create `prospect_dir / "raw" / "linkedin" / "activity_screenshots"` (mkdir parents=True, exist_ok=True). The LinkedIn subtree is always created so the operator has the manual-capture target ready.
4. Create `prospect_dir / "raw" / "podcasts"` (operator drops podcast captures there manually for now).
5. If `prospect_dir / "intake_checklist.md"` does not exist, copy `dossiers/_template/intake_checklist.md` into place.
6. **Fan out gatherers.** For each script in `GATHERERS`, spawn `asyncio.create_subprocess_exec("python", f"scripts/{script}", founder, company, str(prospect_dir / "raw"), stdout=PIPE, stderr=PIPE)`. Pass twitter_handle as a 4th arg only to `gather_twitter.py`.
7. `await asyncio.gather(...)` on all subprocess `.communicate()` calls. **Do not** use `return_exceptions=True` — let one gatherer's exception abort the run loudly.

   *Override:* per the "fail loud" rule (§1), but for orchestrate specifically, **wrap each `.communicate()` in its own try/except**: a YC-page 404 should not kill the Twitter fetch. Print per-script `rc=` and the first 2KB of stderr if `rc != 0`. Exit code of orchestrate.py itself is `max(0, count_of_failed_subprocesses)` — non-zero if any failed, but only after all have finished.
8. **Print summary table** at end: each script, return code, output file size in bytes (or `MISSING` if the expected `raw/{source}.md` doesn't exist post-run).
9. **Print next-step hint:** `"Next: python scripts/research.py '<founder>' '<company>' '<prospect_dir>/raw'"`.

**Sequence within a session (operator-facing, design_doc §6 step 6.1):**
```
orchestrate.py    →  raw/ populated by gatherers
[manual]          →  drop LinkedIn PDF + activity screenshots
research.py       →  dossier.md
[git commit + push]
index_to_nia.py   →  /v2/sources POSTs
[Claude + Nia MCP] →  outreach drafts
```

**Out of scope:** Calling `research.py` automatically. Calling `route.py` per-artifact. Retrying failed gatherers. Slack/email notification on completion.

---

### 6.4 `scripts/index_to_nia.py` — Indexing (Layer 3)

**Single responsibility:** POST to `/v2/sources` for each source the operator passes on the CLI.

**CLI (one of):**
```
python scripts/index_to_nia.py repo "<owner>/<name>" [branch]
python scripts/index_to_nia.py docs "<https://...>"
```

The script supports exactly two modes (`repo`, `docs`) in Phase 1. Multi-source batch mode is deferred — the operator runs the script multiple times (it's three commands, not worth a config file).

**Module-level constants:**
- `BASE = "https://apigcp.trynia.ai/v2"`

**Logic flow:**

1. Load `.env`, read `NIA_API_KEY`. Fail fast if missing.
2. Parse argv. If mode not in `{"repo","docs"}`, exit 2 with usage message.
3. Build body per §4.1 / §4.2.
4. POST with header `Authorization: Bearer {NIA_API_KEY}`, `Content-Type: application/json`, `timeout=30`.
5. Handle response:
   - `200/201` → print `id`, `type`, `status` from response. Exit 0.
   - `409` → print `"already indexed: {target}"`, exit 0 (idempotent re-run is desired).
   - `4xx` other → print response body, exit 1.
   - `5xx` → wait 5s, retry once. On second failure, print and exit 1.
6. **Do not** poll for indexing completion. Nia indexing is async (1-5 min per docs note); the operator does not block on it. The next time the operator runs Claude+Nia MCP, the source is queryable.

**Failure modes:**
- Missing `NIA_API_KEY` → exit 2.
- Bad arg shape → exit 2 with usage.
- 5xx after retry → exit 1.

---

### 6.5 `scripts/query_dossier.py` — Outreach Prompt Emitter (Layer 4)

**Single responsibility:** Print a Claude-ready prompt to stdout. **Does not call any API.** This is intentional: the actual querying happens in a Claude session that has the Nia MCP server attached, and the prompt instructs Claude to invoke `/v2/search mode=universal`.

**CLI:**
```
python scripts/query_dossier.py "<founder_name>" "<company>"
```

**Logic flow:**

1. Substitute `{founder_name}` and `{company}` into the `QUERY_TEMPLATE` string (template body in design_doc §6 step 5; the executing agent copies that template literally into the script — do not paraphrase).
2. Print to stdout.
3. Exit 0.

The operator pipes this into clipboard or pastes manually into Claude. No file I/O. No API calls.

**Why no direct API call:** Phase 1 keeps querying in the human-in-the-loop pane (Claude + Nia MCP). Adding direct `/v2/search` calls to a script duplicates Claude's MCP plumbing without adding value, and the dossier-to-outreach step is the part Hafeedh must read carefully — automating it through a script invites the operator to skip review.

---

### 6.6 `scripts/gather_*.py` — Gathering Layer (Layer 1)

Phase 1 ships **five** gather scripts for `orchestrate.py`'s default fan-out, plus a sixth that runs manually:

| Script | Source | Mechanism | Output path |
|---|---|---|---|
| `gather_yc.py` | YC company directory page | Playwright async, headless Chromium | `raw/yc_page.md` |
| `gather_jobs.py` | Company careers page | Playwright async, headless Chromium | `raw/company_jobs.md` |
| `gather_twitter.py` | Nitter mirror | Playwright async, headless Chromium | `raw/twitter.md` |
| `gather_hn.py` | HN Algolia REST | `requests`, no browser | `raw/hn_comments.md` |
| `gather_news.py` | Google News results | Playwright async, headless Chromium | `raw/news_coverage.md` |
| `gather_podcasts.py` | YouTube transcripts | Playwright async + transcript scrape | `raw/podcasts/{n}_{slug}.md` |

**Common contract (every gather_*.py):**

- CLI signature: `python scripts/gather_<src>.py "<founder>" "<company>" "<raw_dir>" [extra]`. The 4th positional is source-specific (twitter handle, careers URL, etc.). If the 4th positional is required and missing, the script must exit 2 with a usage message — never guess.
- Each script writes its single output file (or directory) atomically: write to `{out}.tmp`, then `os.replace` to final. This guards against half-written markdown if the script is interrupted.
- Each script must include the §3.3 markdown header (`# {Source} — ...`, `**Captured:** ...`, `**Source URL:** ...`).
- Headless Chromium with `user_agent="Mozilla/5.0 (kaide-recon)"`. No cookies, no auth, no logged-in state.
- Page timeout: 30s per `page.goto`. Do not extend.
- On any exception, print the offending URL and re-raise. The subprocess return code is what `orchestrate.py` reads.
- **No retries inside gatherers.** A failed gather is a signal to run the script manually with eyes on it.

**Per-script specifics:**

- **`gather_yc.py`** — URL pattern `https://www.ycombinator.com/companies/{company-slug}`. Extract the page text; the YC pages are mostly static markup. If the page is 404, write a stub markdown noting "no YC page found" and exit 0 (this is a non-failure for non-YC prospects).
- **`gather_jobs.py`** — Operator must pass the careers URL as the 4th positional (auto-discovery of careers URLs is out of scope). Capture all visible job postings as a flat list of `## {title}` sections with the full description body. This is the highest-signal source for Kaide Labs angle work — extract aggressively.
- **`gather_twitter.py`** — URL pattern `https://nitter.net/{handle}`. Capture the timeline (~ last 90 days). If Nitter is rate-limiting (HTTP 429 or visible block page), exit 1 with a clear message — do not silently produce empty output. Operator may need to switch Nitter instance.
- **`gather_hn.py`** — Uses `requests` against `https://hn.algolia.com/api/v1/search_by_date?author={handle}&hitsPerPage=200`. The operator passes `{handle}` as the 4th positional. Format each comment as `## {created_at} — {story_title}\n\n{comment_text}\n`. No Playwright.
- **`gather_news.py`** — URL pattern `https://news.google.com/search?q={quoted founder name OR company}`. Capture top ~20 result headlines + source + snippet. Do not follow into article bodies in Phase 1 (that's a V1.1 enhancement).
- **`gather_podcasts.py`** — Excluded from `orchestrate.py`'s default fan-out. The operator runs it explicitly with a list of YouTube URLs (passed as comma-separated 4th positional). For each URL, open the page, extract the transcript via the YT transcript panel (or fall back to a printed-message "manual capture needed for {url}"). Phase 1 acceptance does not require this gatherer to work end-to-end — it must merely exist as a runnable script.

**Banned in every gather_*.py:**
- `linkedin.com` — never visit, never even resolve. The script must reject any 4th-positional argument containing `linkedin.com` and exit 2.
- Authenticated cookies, logged-in states, OAuth tokens.
- Selenium, undetected-chromedriver, or any anti-detection tooling.
- Reading `.env` (gatherers do not need API keys).

---

## 7. Logic Flow End-to-End (single prospect)

This is the canonical Phase 1 sequence. The execution agent should validate the deliverable by running this sequence against James He:

```
1.  Operator: python scripts/orchestrate.py "James He" "Artificial Societies"
            └─ creates dossiers/james-he-artificial-societies/raw/{linkedin/,podcasts/}
            └─ copies intake_checklist.md from template
            └─ fans out 5 gatherers in parallel
            └─ prints summary + next-step hint

2.  Operator: drops LinkedIn PDF into raw/linkedin/profile.pdf
            drops activity screenshots into raw/linkedin/activity_screenshots/
            optionally edits raw/li_jobs.md by hand

3.  Operator: python scripts/research.py "James He" "Artificial Societies" \
              "dossiers/james-he-artificial-societies/raw"
            └─ uploads every eligible file via Files API
            └─ POST /v1beta/interactions agent=deep-research-max-preview-04-2026 background=True
            └─ polls every 30s until terminal
            └─ writes dossier.md + .interaction_id

4.  Operator: review dossier.md, edit if needed, git commit + push

5.  Operator: python scripts/index_to_nia.py repo "<gh-user>/kaide-recon" master
            python scripts/index_to_nia.py repo "<founder-handle>/<repo>" main   (if applicable)
            python scripts/index_to_nia.py docs "https://docs.<company>.com"     (if applicable)

6.  Operator: python scripts/query_dossier.py "James He" "Artificial Societies" | clip
            paste into Claude (with Nia MCP attached)
            Claude calls POST /v2/search mode=universal
            Claude returns 3 outreach angles, ranked

7.  Operator: edit, send, log outcome in intake_checklist.md
```

**Active human time budget per PRD §3:** ~30 minutes. Steps 2, 4, 6, 7 are the human time. Steps 1, 3, 5 are wall-clock time (machine work).

---

## 8. Acceptance Criteria for Phase 1

The execution agent's work is complete when **all** of these are true:

| ✓ | Criterion |
|---|---|
| ☐ | All 11 scripts in §3 dependency map exist in `scripts/`, runnable via `python scripts/<name>.py --help`-style usage messages |
| ☐ | `orchestrate.py` runs on James He without crashing; produces `dossiers/james-he-artificial-societies/raw/` with at least 3 of 5 default gatherers writing valid output (some gatherers will legitimately produce stubs — that's fine) |
| ☐ | `research.py` completes a real Deep Research Max run on James, producing a `dossier.md` of >1500 words with inline citations |
| ☐ | `dossier.md` has the 7 sections specified in `design_doc.md` §5 (Founder Background, Company Snapshot, Stated Pain Points, Technical Decisions, Enterprise Integration Surface, Recommended Outreach Angle, Red Flags) |
| ☐ | `.interaction_id` file is written next to `dossier.md` |
| ☐ | `index_to_nia.py repo "<user>/kaide-recon" master` returns 200/201 or 409 |
| ☐ | `query_dossier.py` prints a coherent prompt to stdout (no API call from this script) |
| ☐ | Total cost of one James end-to-end run ≤ $7 (PRD §3, §7) |
| ☐ | Active human time in the run ≤ 30 minutes |
| ☐ | No script imports anything outside the §2 dependency manifest |
| ☐ | No script touches `linkedin.com` programmatically |
| ☐ | No new files created outside `scripts/`, `prompts/`, `dossiers/`, and `requirements.txt` |

---

## 9. Anti-Scope (Things the Execution Agent Must Not Do)

These are explicit prohibitions. If any feels like a "natural extension" while implementing — it isn't. Stop and escalate.

1. Do not introduce a `Prospect` / `Dossier` / `Artifact` dataclass. Pass strings and Paths.
2. Do not refactor the gather scripts behind a `BaseGatherer` ABC.
3. Do not add a `config.yaml`. Constants live as module-level Python.
4. Do not add a logging library. `print()` is the contract.
5. Do not add tests. Validation is the James run.
6. Do not parameterize the model IDs. They are locked.
7. Do not call `/v2/search` from any Phase 1 script. That layer lives in Claude+Nia MCP.
8. Do not auto-run `research.py` from `orchestrate.py`. The human is the gate between gathering and the $5 spend.
9. Do not auto-run `index_to_nia.py` from `research.py`. The human reviews `dossier.md` before pushing.
10. Do not implement `previous_interaction_id` chaining. That is V1.1.4.
11. Do not implement automated LinkedIn anything. Manual capture is the rule, not the workaround.
12. Do not write a README expansion as part of Phase 1 — the existing PRD/DESIGN are sufficient handoff. README polish is a separate pass.

---

## 10. Handoff Note

This spec is exhaustive enough that the execution agent should not need to re-read `design_doc.md` while writing the scripts — but should re-read it once before starting, to internalize §1.1 (model lock), §4 (positioning prompt), §5 (deep research prompt template), and §9 (endpoint reference). All payload shapes in those four sections override anything ambiguous in this spec.

When in doubt about a design choice not covered here: **default to less code, not more.** The pipeline earns its existence through use, not through cleverness. — PRD §8.2.

Phase 1 is done when James He's dossier exists and reads well. That's the bar.
