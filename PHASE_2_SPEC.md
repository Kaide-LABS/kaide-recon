# PHASE 2 SPEC — Hardening, Re-Pitch Flow, Future-Hafeedh Readability

**Codename:** `kaide-recon`
**Author:** Principal Systems Architect (handoff doc for execution agent)
**Status:** Phase 2 blueprint — implementation-ready, no application code in this file
**Audience:** Execution agent (Gemini) writing the Phase 2 changes
**Companion docs:** `PRD.md`, `design_doc.md`, `PHASE_1_SPEC.md`, `decisions/phase_1_decisions.md`
**Last revised:** 2026-05-04
**Prerequisite:** Phase 1 is shipped, James He dossier exists, `research.py` QA patch (multimodal grounding + cost gate + poll timeout) is on master.

---

## 0. What's Already Shipped (Phase 1 Recap — Do Not Rebuild)

The execution agent must read this section before starting and must not re-implement anything in it.

| Layer | Component | Status |
|---|---|---|
| Gathering | `orchestrate.py` + 5 default `gather_*.py` (yc, jobs, twitter, hn, news) + `gather_podcasts.py` (manual-only) | Shipped |
| Synthesis | `research.py` with multimodal Files API grounding, $5 cost gate, 60-min wall-clock cap | Shipped (QA-patched) |
| Routing | `route.py` (Gemini 3 Flash classifier) — exists but **not yet wired into a flow** | Partially shipped |
| Indexing | `index_to_nia.py` for `repo` and `docs` modes | Shipped |
| Querying | `query_dossier.py` (prompt emitter for Claude+Nia MCP) | Shipped |
| Prompts | `kaide_labs_positioning.md`, `deep_research_prompt.md`, `router_prompt.md` | Shipped |
| Templates | `dossiers/_template/intake_checklist.md` | Shipped |
| Validation case | `dossiers/james-he-artificial-societies/dossier.md` (cited, 7 sections, draws Figma-plugin angle) | Shipped |
| Repo hygiene | `.gitignore` excludes `dossiers/*/raw/linkedin/`, `*.pdf`, `.env`, `.interaction_id`. `.env.example` present. | Shipped |

**Deliberately deferred to V1.1+ — do not implement in Phase 2:**
- `previous_interaction_id` chaining (V1.1.4)
- Per-source freshness tracking (V1.1.1)
- Folk CRM integration (V1.1.2)
- Pre-built outreach templates (V1.1.3)
- Pattern detection across dossiers (V2)
- Web UI (V2)

---

## 1. Phase 2 Mission

Phase 1 proved the architecture works against James He. Phase 2 makes the pipeline **operationally durable** — meaning Future-Hafeedh (PRD §4.2) can reopen the repo cold in 3-6 months and run it end-to-end on a new prospect without reading source code, **and** the re-pitch flow (PRD §6.2) is a real path rather than a sketch.

Phase 2 scope is intentionally narrow. Three deliverables only:

1. **D1 — `README.md`**: the Future-Hafeedh runbook. PRD §7 acceptance criterion #7 ("Future-Hafeedh test passes") is currently failing because no README exists.
2. **D2 — Re-pitch flow (`scripts/repitch.py` + `route.py` integration)**: PRD §6.2 specifies that delta artifacts on a stale prospect get classified by Flash before deciding whether to spend on Deep Research Max. `route.py` exists but is operator-manual; Phase 2 wires it into a single-command re-pitch path.
3. **D3 — `scripts/validate_pipeline.py`**: a 30-second smoke check that confirms the operator's local environment is wired correctly (env vars present, prompts files exist, James dossier committed, gitignore honoring sensitive paths). This is what Future-Hafeedh runs first when reopening the repo.

Anything not listed above is out of scope. If a fourth idea feels obvious, the answer is no — see PRD §11 deferred backlog.

---

## 2. Discipline Reminders (Carry Forward From Phase 1)

| Rule | Implication |
|---|---|
| Internal tool, ship rough | No frameworks. Each script stays flat. |
| `print()` is the logging contract | No `logging` module. |
| No tests | Validation = the Phase 2 acceptance test in §6. |
| Locked stack | Models, endpoints, dep tree from PRD §3 / design_doc §1.1 unchanged. |
| Manual LinkedIn rule | Phase 2 must not introduce any code path that touches `linkedin.com`. The README must explicitly re-state the rule for Future-Hafeedh. |
| Dependencies | No new pip packages. Phase 2 uses only what's already in `requirements.txt`. |

---

## 3. D1 — `README.md` (Future-Hafeedh Runbook)

**Location:** repo root.
**Audience:** Hafeedh, returning cold after 3-6 months. Must be readable in 5 minutes and runnable without reading any `.py` file.

**Required sections, in order:**

### 3.1 Header
- One-paragraph mission (paraphrase PRD §1).
- Single line: "If you are reopening this repo cold, run `python scripts/validate_pipeline.py` first."

### 3.2 What This Is / Is Not
- 4-6 bullets max. Pull from PRD §5.3.

### 3.3 Hard Constraints (one-line each)
- Manual LinkedIn only — no automation, ever.
- Cost ceiling: ≤ $15 per prospect.
- Time ceiling: ≤ 30 min active human time per prospect.
- Stack lock: do not change models or endpoints without updating `design_doc.md` §1.1.

### 3.4 First-Time Setup (≤ 5 commands)
```
git clone <repo>
cd kaide-recon
python -m venv venv && .\venv\Scripts\Activate.ps1   # PowerShell on Windows; bash equivalent in a comment
pip install -r requirements.txt
playwright install chromium
cp .env.example .env   # then fill in GEMINI_API_KEY, NIA_API_KEY, GITHUB_TOKEN
python scripts/validate_pipeline.py   # confirm everything's wired
```

### 3.5 Adding a New Prospect (the 30-minute path)
A numbered runbook matching PRD §6.1 exactly. Each step states: command to run, what it does, expected wall-clock time, what file appears.

```
1. python scripts/orchestrate.py "<Founder>" "<Company>" [twitter_handle]
2. Drop LinkedIn PDF into dossiers/<slug>/raw/linkedin/profile.pdf
   Drop activity screenshots into dossiers/<slug>/raw/linkedin/activity_screenshots/
3. python scripts/research.py "<Founder>" "<Company>" "dossiers/<slug>/raw"
   (~15 min wall-clock, ~$5; you'll get a 5s abort window)
4. Review dossiers/<slug>/dossier.md, edit if needed, git commit + push
5. python scripts/index_to_nia.py repo "<gh-user>/kaide-recon" master
   (and optionally: founder repo, company repo, company docs)
6. python scripts/query_dossier.py "<Founder>" "<Company>"
   Paste output into Claude (with Nia MCP attached). Read 3 angles, edit, send.
7. Update intake_checklist.md with outcome.
```

### 3.6 Re-Pitching a Stale Prospect
- One paragraph + one command pointing at `repitch.py` (D2).
- Note: re-pitch only triggers a fresh $5 Max run if Flash classifies the delta as `RE_SYNTHESIZE`.

### 3.7 File Map
A 10-line `tree`-style block showing where things live:
```
scripts/        — pipeline scripts (don't edit unless changing architecture)
prompts/        — locked prompt templates (edit cautiously)
dossiers/       — one folder per prospect
decisions/      — phase decision logs (audit trail of deviations from spec)
PRD.md          — why this exists + scope
design_doc.md   — architecture + endpoint reference (canonical)
PHASE_*_SPEC.md — what each phase shipped
```

### 3.8 Troubleshooting
Five short Q&A entries. The required ones:
1. "Deep Research Max hangs / never completes" → poll loop times out at 60min and prints the interaction id; run `client.interactions.get(<id>)` from a Python REPL to inspect.
2. "Nitter is rate-limiting" → set `NITTER_INSTANCE=https://<other-mirror>` env var and re-run `gather_twitter.py` only.
3. "Nia returns 409" → already indexed, that's success.
4. "I forgot what state a prospect is in" → open its `intake_checklist.md`.
5. "I want to spend less than $5 on a re-pitch" → use `repitch.py`; it runs Flash classification first and skips the Max call if the delta is thin.

### 3.9 What's Banned
A short, blunt list:
- Automated LinkedIn anything.
- Adding pip dependencies without updating `requirements.txt` and `decisions/`.
- Changing the model IDs.
- Sending outreach from a script (always human-gated).

### 3.10 First Sale Rule
A one-line callout to PRD §12.5: pipeline earns its existence when the first £10k engagement closes. Until then, every weekend hour is measured against active selling.

**README acceptance test (D1):** Hafeedh, given only this README and a fresh clone, can add a new prospect end-to-end without opening any `.py` file. The execution agent self-tests by re-reading the README after writing it and checking each runbook step matches an actual command in the codebase.

---

## 4. D2 — Re-Pitch Flow (`scripts/repitch.py`)

PRD §6.2 specifies: when a prospect goes silent and we want a second angle, gather the delta since the last synthesis, classify whether it's substantive enough via Flash, then either (a) re-run Deep Research Max if `RE_SYNTHESIZE`, or (b) skip the spend if `KEEP` / `SKIP`.

Phase 2 implements this as `scripts/repitch.py`. It is a thin orchestrator on top of existing scripts — it must not duplicate gather, route, or research logic.

### 4.1 CLI

```
python scripts/repitch.py "<founder>" "<company>" [twitter_handle]
```

### 4.2 Module-level constants
- `DELTA_DIR_NAME = "delta"` (subdir of `raw/` where re-pitch artifacts land — keeps the original raw/ pristine for audit).

### 4.3 Logic flow

1. **Resolve prospect.** Compute slug. Verify `dossiers/<slug>/dossier.md` exists. If not, exit 2 with `"no prior dossier — run a first-time pitch via orchestrate.py + research.py"`.
2. **Stage delta directory.** `dossiers/<slug>/raw/delta/<YYYY-MM-DD>/`. Mkdir parents. This is where fresh gather output goes — the original `raw/` files stay frozen as historical record.
3. **Run gatherers, redirected.** Reuse `orchestrate.py`'s per-script subprocess pattern, but pass the delta dir as `<raw_dir>`. Implementation note: `repitch.py` may simply `subprocess.run` each of the 5 default gatherers itself with the delta path — code duplication of the fan-out loop is acceptable and preferable to refactoring `orchestrate.main` into a library. Internal-tool discipline (§2).
4. **Per-artifact route classification.** For each non-empty file in the delta dir, run `python scripts/route.py <path>` and capture its single-line verdict. Tabulate:
   - `KEEP` → quietly retain the file in delta dir for inclusion next time research is run.
   - `SKIP` → delete the file (low signal).
   - `RE_SYNTHESIZE` → set a `should_resynth` flag.
5. **Print a delta summary table.** Columns: artifact path, verdict, size. Operator-facing.
6. **Decision branch.**
   - If `should_resynth` is True (any artifact returned `RE_SYNTHESIZE`): print the cost gate (`~$5.00`, 5s Ctrl-C window) and call `python scripts/research.py <founder> <company> <prospect_dir>/raw/delta/<date>` as a subprocess. The Max run grounds **only on the delta dir**, not on the full historical raw/ — this is intentional: we want a fresh angle from the delta, not a wholesale re-synthesis. Output goes to `dossiers/<slug>/dossier_<date>.md` (suffixed by date so the original isn't overwritten).
   - Else: print `"Delta is thin — no Max spend. Re-query the existing dossier via Claude+Nia MCP for a different angle instead."` and exit 0.
7. **On a fresh dossier_<date>.md being written, print** the next-step hint: `"Re-index: python scripts/index_to_nia.py repo <gh-user>/kaide-recon master"` so the new dossier reaches Nia.

### 4.4 Banned in `repitch.py`
- Calling Deep Research Max twice in one invocation.
- Auto-running `index_to_nia.py` (operator gates the push).
- Auto-running `query_dossier.py` (operator gates the outreach draft).
- Modifying anything in the original `dossiers/<slug>/raw/` (delta dir is sibling, not in-place mutation).

### 4.5 Failure modes
- Missing prior dossier → exit 2.
- Any gatherer subprocess failing → print stderr, continue with remaining gatherers (re-pitch tolerates partial gathering — the Flash router will see what's there).
- `route.py` returning malformed verdict on an artifact → print warning, treat as `KEEP` (conservative default; we'd rather hold a maybe-useful artifact than discard it).
- Max research call exits non-zero → bubble up the exit code.

### 4.6 Router prompt update (`prompts/router_prompt.md`)
Verify the existing rubric explicitly emits one of `KEEP | RE_SYNTHESIZE | SKIP` on the first line, and that it knows context: it's classifying *delta artifacts on a stale prospect*. If the existing rubric doesn't already explain that framing, the executor should append a one-paragraph "CONTEXT" section to the rubric file. **Do not rewrite the rubric** — append only.

---

## 5. D3 — `scripts/validate_pipeline.py` (Future-Hafeedh's First Command)

A 30-second offline smoke check. **Calls no external APIs.** Confirms the local environment is wired before the operator wastes time debugging mid-pipeline.

### 5.1 CLI
```
python scripts/validate_pipeline.py
```

No arguments.

### 5.2 Checks (each prints `[OK]` or `[FAIL] <reason>`; exits non-zero if any FAIL)

| # | Check | Pass criterion |
|---|---|---|
| 1 | `.env` exists at repo root | File present |
| 2 | `GEMINI_API_KEY` and `NIA_API_KEY` are set after `dotenv.load_dotenv()` | Both non-empty strings |
| 3 | `GITHUB_TOKEN` is set | Non-empty (warn-only if missing — used for private indexing) |
| 4 | All 11 scripts exist in `scripts/` | Each script file present and non-empty |
| 5 | All 4 prompt files exist in `prompts/` | `kaide_labs_positioning.md`, `deep_research_prompt.md`, `router_prompt.md`, plus any outreach prompt referenced by `query_dossier.py` |
| 6 | `requirements.txt` matches the locked dep tree | Exactly the 4 deps from PRD §3 / design_doc §6 step 0 are present (no extras, no missing) |
| 7 | `dossiers/_template/intake_checklist.md` exists | File present and non-empty |
| 8 | `dossiers/james-he-artificial-societies/dossier.md` exists | File present and contains all 7 required headings (`Founder Background`, `Company Snapshot`, `Stated Pain Points`, `Technical Decisions`, `Enterprise Integration Surface`, `Recommended Outreach Angle`, `Red Flags`) |
| 9 | `.gitignore` contains the four sensitive patterns | `.env`, `dossiers/*/raw/linkedin/`, `*.pdf`, `.interaction_id` |
| 10 | No file under `dossiers/*/raw/linkedin/` is tracked by git | Run `git ls-files dossiers/*/raw/linkedin/` — must return empty. If non-empty, FAIL with the offending paths (gitignore was added too late). |
| 11 | `playwright` chromium is installed | `playwright._impl._driver` import + a quick `chromium.executable_path` existence check, OR a single subprocess call to `playwright install --dry-run chromium`. If unsure, skip with `[WARN]` rather than `[FAIL]` — Playwright bootstrap is platform-finicky. |
| 12 | `python -c "from google import genai"` succeeds | Module importable |

### 5.3 Output format
```
kaide-recon pipeline validator
─────────────────────────────────
[OK]   .env present
[OK]   GEMINI_API_KEY set
[OK]   NIA_API_KEY set
[WARN] GITHUB_TOKEN not set — private repo indexing will fail
[OK]   11/11 scripts present
[OK]   4/4 prompts present
[OK]   requirements.txt matches lock
[OK]   intake_checklist template present
[OK]   James He dossier present (7/7 sections)
[OK]   .gitignore covers sensitive paths
[OK]   No LinkedIn artifacts tracked by git
[OK]   playwright chromium installed
[OK]   google-genai importable
─────────────────────────────────
Result: PASS (12 ok, 1 warn, 0 fail)
```

Exit code: 0 on all OK or OK+WARN. 1 if any FAIL.

### 5.4 Banned in `validate_pipeline.py`
- Network calls to Gemini, Nia, or any other service. Validation must work offline.
- Modifying any file (read-only).
- Recursive globs over `dossiers/*/raw/` (could be slow if many prospects). Limit to specific known paths.

---

## 6. Phase 2 Acceptance Test

Phase 2 is done when **all** are true:

| ✓ | Criterion |
|---|---|
| ☐ | `README.md` exists at repo root, contains all 10 sections from §3 |
| ☐ | A first-time reader can run the §3.4 setup commands and reach a green `validate_pipeline.py` without opening any `.py` file |
| ☐ | `scripts/repitch.py` exists, runs against James as a smoke target (no actual Max spend required for the test — verify dry-run logic by passing an empty delta dir, asserting it correctly emits "Delta is thin — no Max spend") |
| ☐ | `scripts/validate_pipeline.py` exists and reports PASS on a correctly-set-up clone |
| ☐ | `validate_pipeline.py` reports FAIL when `.env` is missing (negative test — operator can verify by `mv .env .env.bak && python scripts/validate_pipeline.py; mv .env.bak .env`) |
| ☐ | No new pip dependencies added (`requirements.txt` unchanged) |
| ☐ | No new model IDs introduced |
| ☐ | No file in `scripts/` references `linkedin.com` |
| ☐ | `decisions/phase_2_decisions.md` exists, documents any deviations from this spec |
| ☐ | All Phase 2 work fits in three new files (`README.md`, `scripts/repitch.py`, `scripts/validate_pipeline.py`) plus minor edits to `prompts/router_prompt.md` and `decisions/phase_2_decisions.md`. If the executor needs a fourth new file, that's a scope expansion — flag it instead of writing it. |

---

## 7. Anti-Scope (Things the Execution Agent Must Not Do in Phase 2)

1. Do not implement `previous_interaction_id` chaining inside `repitch.py`. That's V1.1.4. The Phase 2 re-pitch always grounds on the delta dir as fresh input.
2. Do not auto-discover careers URLs, GitHub orgs, or twitter handles. Operator passes them.
3. Do not add a config file (`config.yaml`, `pyproject.toml` for tooling, etc.).
4. Do not refactor `orchestrate.py` into a library `repitch.py` imports. Subprocess fan-out duplicated across the two scripts is the right call here.
5. Do not add any retry/backoff layer beyond what Phase 1 already has.
6. Do not implement Folk CRM hooks, outcome tracking, or Slack notifications.
7. Do not write a CHANGELOG.md.
8. Do not reorganize the repo structure (folder layout is locked by design_doc §2).
9. Do not push to GitHub from inside Python — pushing stays in the operator's terminal.
10. Do not add a `--dry-run` flag to `research.py`. The 5s cost gate is the dry-run.

---

## 8. Handoff Note

The execution agent should:
1. Read `PRD.md` §6.2 (re-pitch motion) and §4.2 (Future-Hafeedh persona) before writing D1 and D2.
2. Read `decisions/phase_1_decisions.md` to understand what was patched and why — Phase 2 must not regress the multimodal grounding fix.
3. Write D3 (`validate_pipeline.py`) first — it gives a fast feedback loop while building D1 and D2.
4. Write D2 (`repitch.py`) second — exercising it shakes out any rough edges in `route.py` that the operator should know about for D1's troubleshooting section.
5. Write D1 (`README.md`) last — it documents what actually exists, not what was planned.

When in doubt: **less code, not more.** Phase 2 should add fewer than 500 lines of Python and one Markdown file. If you're writing more than that, escalate.

Phase 2 is done when Future-Hafeedh's first command works.
