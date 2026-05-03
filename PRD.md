# PRD: Kaide Recon (Founder Intel Pipeline)

**Codename:** `kaide-recon`
**Author:** Hafeedh (Founder, Kaide Labs)
**Status:** v1 — building today
**Audience:** Hafeedh (operator), future Hafeedh (revisits in 3-6 months), any AI agent assisting on this codebase
**Companion document:** `design_doc.md` (technical design)
**Last revised:** May 3, 2026

---

## 1. Mission

Productize the founder-research → cold-outreach loop so that Kaide Labs can pitch B2B AI startup founders with genuine specificity at a rate that compounds across quarters, not at the rate of manual one-off research.

The output of this pipeline is **the cold pitch artifact itself** — the email body, the InMail body, the LinkedIn note, the demo angle. Everything upstream (gathering, synthesis, indexing) exists to make the artifact undeniable.

---

## 2. Why This Exists

### 2.1 The problem
Cold outreach to YC-backed B2B AI founders is a binary game: either the pitch references a specific public bottleneck the founder has named and proposes a concrete sidecar that addresses it, or it gets archived in 5 seconds. Generic outreach has approximately zero conversion at this audience.

The bottleneck for Kaide Labs is not engineering capacity (Hafeedh ships fast) or quality of build (the architecture decisions and DMZ discipline are already locked). The bottleneck is **research depth per prospect**. A pitch built on 10 minutes of skimming converts dramatically worse than one built on 2 hours of deep recon. But 2 hours per prospect doesn't scale beyond 5 prospects per quarter.

The pipeline fixes this by separating **gathering** (parallelizable, automatable) from **synthesis** (one focused agent run) from **outreach generation** (human-in-the-loop, low-volume). Total active human time per prospect drops from 2+ hours to ~30 minutes, while research depth increases.

### 2.2 The strategic frame
Kaide Labs sells forward-deployed engineering. The sales motion *is* a forward-deployed engagement: the cold pitch demonstrates that you've already done the homework a real FDE would do before showing up. The recon pipeline isn't separate from the product — it's a preview of the product.

Done well, the recipient's reaction to the cold pitch is *"this person already understands my stack"* before they've even watched the demo. That signal is what converts.

---

## 3. Hard Constraints

| Constraint | Value |
|---|---|
| Solo operator | Hafeedh (no team to delegate to) |
| Time budget per prospect | ≤ 30 min active human time end-to-end |
| Money budget per prospect | ≤ $15 (one Deep Research Max call ~$5 + Gemini 3 Flash routing < $0.10 + slack for retries) |
| Manual ToS-bound surfaces | LinkedIn captured manually only; no automation against logged-in LinkedIn (account-ban risk against active GTM channel) |
| Stack alignment | `deep-research-max-preview-04-2026` (Gemini 3.1 Pro–backed) for synthesis; `gemini-3-flash-preview` for cheap routing/dispatch; Nia v2 (`/v2/sources`, `/v2/search`) for indexing + retrieval; Claude via Nia MCP for querying. Single dependency tree: `google-genai`, `requests`, `playwright`. |
| Output format | Markdown dossiers committed to a private GitHub repo, queryable via Nia MCP |
| Maintenance burden | Pipeline must continue to work with zero refactoring for 6 months minimum |
| Engineering taste | Internal-tool discipline: ship rough first, iterate on real use. Not client-facing rigor |

---

## 4. Personas

### 4.1 Hafeedh-the-operator (primary, 100% of traffic)
- Solo founder running Kaide Labs sales motion
- Cycles through 3-10 prospects per quarter depending on engagement load
- Needs to walk into every cold pitch with: founder background, company stage, public pain points, technical preferences, and a specific demo angle
- Friction tolerance: medium. Will tolerate a 20-min Deep Research Max wait. Will not tolerate a broken Nia indexing job blocking the whole pipeline.
- Success state: opens Claude with Nia MCP active, asks "give me the strongest outreach angle for {founder}," receives a draft email referencing specific public statements, edits in 10 min, sends.

### 4.2 Future-Hafeedh (durability persona, 3-6 month horizon)
- Reopens this repo after a break (Ramadan, exam period, AS engagement consuming cycles)
- Needs to remember: what does this do, what's the workflow, where do I put new founder data
- Pass criterion: README + intake checklist template + this PRD give him enough to add a new prospect end-to-end without re-deriving the architecture
- Fail criterion: he reopens the repo and has to read code to figure out the workflow

### 4.3 An AI coding agent helping on this repo
- Claude Code, Codex, or similar agent invoked to extend gather scripts, refactor code, debug indexing failures
- Needs to read the design doc + this PRD to understand intent before modifying anything
- Pass criterion: an agent given the prompt "extend the pipeline to handle a new gather source" can do so without breaking existing flows
- Fail criterion: agent introduces a dependency on a paid SaaS or a service that violates the constraints in §3

---

## 5. V1 Scope

### 5.1 IN
| # | Feature |
|---|---|
| F1 | Manual capture protocol for LinkedIn (PDF + activity screenshots + LI Jobs) per prospect, dropped into `dossiers/{name}/raw/linkedin/` |
| F2 | Playwright-driven gather scripts (the OpenClaw pattern) for: Twitter (via Nitter), personal websites, podcast transcripts, HN comments, Substack/Medium, conference talks, YC pages, company careers page job postings, news coverage |
| F3 | Gemini Deep Research Max synthesis (`research.py`) consuming raw/ folder as multimodal grounding via the Files API + Interactions API, outputting `dossier.md` with 7 cited sections |
| F4 | Gemini 3 Flash router (`route.py`) classifying each new public artifact (worth indexing? worth re-synthesis? skip?) before spending Deep Research Max budget |
| F5 | Nia indexing (`index_to_nia.py`) via `POST /v2/sources` with `type` discriminator for: founder GitHub repos, company GitHub org, company docs site, the kaide-recon dossiers repo itself |
| F6 | Claude-via-Nia-MCP querying (`/v2/search` mode=universal) for outreach-angle generation and red-flag flagging |
| F7 | Locked Kaide Labs positioning prompt injected into all synthesis steps (prevents drift toward generic AI-coding-agent positioning) |
| F8 | Per-prospect intake checklist that tracks gathering → synthesis → outreach → outcome |

### 5.2 OUT (deferred — see §11)
- Automated LinkedIn scraping (banned by ToS, account-risk to active GTM channel)
- Automated Crunchbase scraping (anti-scraping, paid API exists if needed)
- Multi-operator support (current scope is solo Hafeedh)
- Web UI / dashboard (CLI-only is fine for solo use)
- Dossier comparison or pattern detection across founders (interesting in V2 if 50+ dossiers accumulate)
- Automatic outreach sending (the *generation* is automated; the *send* stays human-gated)
- Slack/email notifications when pipeline stages complete
- Paid integrations: LinkedIn Sales Navigator, Apollo.io, Clay, etc.

### 5.3 What this is NOT
- Not a CRM. Folk handles CRM. This pipeline produces inputs that feed Folk.
- Not a sales engagement platform. The send mechanism stays in regular email + LinkedIn.
- Not a mass outreach tool. Volume target is 3-10 prospects per quarter, not 100s per week.
- Not a clone of existing GTM stacks. Kaide-recon is intentionally specialized for technical-buyer hyper-personalization, not generic SDR-team workflows.

---

## 6. User Flow

### 6.1 New prospect intake (end-to-end)
```
[Hafeedh decides to pitch {founder} at {company}]
     |
     v
[creates dossiers/{founder-slug}/ with intake_checklist.md from template]
     |
     v
[10 min: manual LinkedIn capture → raw/linkedin/]
     |
     v
[5 min: kicks off orchestrate.py, all gather_*.py run in parallel; route.py
        classifies each output via Gemini 3 Flash before promoting to raw/]
     |
     v
[~15 min: Deep Research Max runs (background=True, polled async)]
     |
     v
[5 min: review dossier.md, commit to repo, push to GitHub]
     |
     v
[1 min: index_to_nia.py POSTs each source to /v2/sources]
     |
     v
[10 min: query via Claude+Nia MCP, get 3 outreach angles, edit final copy]
     |
     v
[2 min: send the outreach]
```

**Total active human time: ~30 min.**
Total wall-clock time: ~50 min including agent waits.
Total cost: ~$5–7 (one Deep Research Max call dominates; Flash routing is sub-dollar).

### 6.2 Re-pitch / re-engagement
If a prospect goes silent after first pitch, the dossier gets re-queried after a defined cool-down period (4-6 weeks) for a different angle. New public statements they've made since first pitch are gathered as a delta. The router classifies whether the delta is substantive enough to justify a Deep Research Max re-run; otherwise we use `previous_interaction_id` to ask follow-up questions on the existing interaction (cheaper, context-preserving).

### 6.3 Post-engagement (if pitch converts)
Dossier transitions from outreach-prep mode to engagement-prep mode. Same data structure, but Claude queries shift from "draft outreach" to "what should I know before this call?"

---

## 7. Success Criteria

V1 ships when these are all true:

| ✓ | Criterion | Verification |
|---|---|---|
| ☐ | Pipeline runs end-to-end on James He as the validation test | `dossiers/james-he-artificial-societies/dossier.md` exists, references specific public statements, makes a clear outreach angle |
| ☐ | Cost per founder ≤ $15 | Track Gemini API spend on the test run |
| ☐ | Active human time per founder ≤ 30 min | Time the James end-to-end run |
| ☐ | Dossier output is usable without further research | Can Hafeedh draft a cold pitch from dossier.md alone, no other tabs open? |
| ☐ | Repo is pushable + Nia-indexable via `POST /v2/sources` `{type: repository}` | `index_to_nia.py` succeeds on the kaide-recon repo |
| ☐ | Claude+Nia MCP queries return cited responses | Test query against `/v2/search mode=universal`: "what's the strongest outreach angle for {founder}?" returns specific cites |
| ☐ | Future-Hafeedh test passes | Reopen the repo cold, follow README, add a new prospect. If you have to read code to do it, README needs work |

---

## 8. Strategic Decisions Locked

### 8.1 Manual LinkedIn, automated everything else
LinkedIn ban risk against active GTM channel is non-negotiable. 5 min per founder of manual capture is the cost. Everything else is fair game for automation.

### 8.2 Internal tool discipline
This is not a client deliverable. Ship rough, iterate on real use. No multi-proposal red-teaming (the 7-step workflow isn't applied here — see §10).

### 8.3 One prospect at a time, validated before scaling
Build the pipeline against James as the test case. If the dossier is useful, scale to other prospects. If the dossier is mediocre, fix the synthesis prompt before building more gather scripts.

### 8.4 Nia for indexing, not gathering
Nia v2's unified `/v2/sources` endpoint can in principle ingest web pages, but it's specialized for repos + docs + papers + datasets. Use it for what it's best at (GitHub + docs + the dossiers repo). Use Playwright / direct API calls for everything else.

### 8.5 Deep Research Max over Nia Oracle
Both can run multi-step research. `deep-research-max-preview-04-2026` (Gemini 3.1 Pro–backed, ~160 search queries per task, multimodal grounding via the Files API) is the more battle-tested research engine and is what the architecture is locked to. Worth re-evaluating in V2 if Oracle catches up — but for V1, locked to Deep Research Max.

### 8.6 Gemini 3 Flash for routing only
Flash is cheap ($0.50/$3 per million in/out) and fast — it's the right tool for the *do we even need to spend $5 on Deep Research Max for this delta?* decision. Never use Flash for the synthesis itself; quality cliff is too steep on this workload.

### 8.7 Outreach send remains human-gated
The pipeline generates outreach drafts. It does not send them. Every cold outreach gets one final read by Hafeedh before going out. Volume isn't the bottleneck — quality of fit is.

---

## 9. Risk & Mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| LinkedIn detects automation despite manual-only policy and bans Hafeedh's account | Low | High | Strict no-automation rule on LinkedIn surfaces. Manual capture only. |
| Deep Research Max output is too generic to drive specific outreach angles | Medium | High | Validate against James first. If output is mediocre, iterate on prompt before building gather scripts. Failure to validate kills the pipeline before it scales. |
| Nia indexing fails on private repos | Medium | Medium | Test Nia indexing on a public repo first (`POST /v2/sources` with `{type:"repository", repository:"<owner>/<name>"}`). If private indexing breaks, make the dossiers repo public (no client IP in it) or fall back to local file search. |
| Deep Research Max preview-tier rate limits bottleneck batch runs | Low | Low | At V1 volume (≤10 prospects per quarter), rate limits aren't a real constraint. Re-evaluate if volume scales 10x. |
| Cost overruns if pipeline gets used for low-quality prospects | Medium | Low | Budget gate: only run Deep Research Max on prospects worth ≥ £10k engagement. For tire-kickers, skip the recon and reply with a templated polite-no. |
| Founder data captured in raw/ folder accumulates sensitive info that gets pushed to GitHub | Low | High | Gitignore everything in `dossiers/*/raw/linkedin/` to avoid committing LinkedIn PDFs. Only commit dossier.md (synthesized) and gather script outputs that come from public sources. |
| The pipeline becomes more interesting than actual customer work | Medium | Medium | Hard constraint: pipeline build effort capped at 1 weekend day + evening blocks during the week. Beyond that, the pipeline isn't earning its keep. |
| Interactions API still in `v1beta` (preview) — breaking changes possible | Medium | Low | Pin `google-genai` in `requirements.txt`. Re-test on SDK upgrades. The `/v1beta/interactions` endpoint and `client.interactions.create(... background=True)` shape have been stable since the April 2026 launch. |

---

## 10. Why No 7-Step Workflow Here

The Kaide Labs SOP's 7-step workflow (Gemini Deep Research → Web Claude PRD → Claude Code modernization → Codex lateral PRDs → Synthesis → Phase 1 spec → Execution → QA) is calibrated for *productized engineering deliverables for paying clients*. It generates 3 proposals, red-teams them, picks one.

Kaide-recon is internal tooling. There are no genuinely divergent proposals to evaluate (the architecture is already determined: gather → synthesize → index → query). Running 1A and 1B would produce noise.

Internal tools earn their keep through *use*, not through pre-build review. The discipline is:
- Build the spec (this PRD + the design doc)
- Ship rough
- Iterate on real use
- Refactor only when friction surfaces

This is the opposite of the 7-step workflow's discipline (over-engineer safeguards before client exposure).

If kaide-recon ever becomes a Kaide Labs *product offering* (e.g., "we'll do the recon for you"), then the 7-step workflow applies. For internal use, no.

---

## 11. Deferred Backlog

### V1.1 (post-validation, no commitment date)
| # | Feature | Rationale |
|---|---|---|
| 1.1.1 | Per-source freshness tracking — flag dossier as stale if base sources updated after last synthesis | Prospects move; dossiers need refresh logic |
| 1.1.2 | Outcome tracking integration with Folk CRM | If Folk exposes write API, log send dates and response outcomes back to the dossier |
| 1.1.3 | Pre-built outreach templates for common angles (hiring spike, public bottleneck, integration commitment unshipped) | Reduces drafting time once 5-10 dossiers reveal common patterns |
| 1.1.4 | Use `previous_interaction_id` to chain follow-up Deep Research questions on stale dossiers without paying full $5 again | Cuts re-research cost dramatically |

### V2 (next quarter+)
| # | Feature | Rationale |
|---|---|---|
| 2.1 | Pattern detection across dossiers | Useful only when 20+ dossiers accumulate |
| 2.2 | Web UI / dashboard | Only if solo CLI workflow becomes friction at higher volume |
| 2.3 | Multi-operator support | Only if Kaide Labs hires a sales partner |
| 2.4 | Productize as a Kaide Labs offering ("recon-as-a-service") | Only if multiple potential clients ask for it explicitly |

### Never
- Mass outreach
- Outreach send automation (always human-gated)
- LinkedIn scraping
- Anything that requires running real-name accounts on platforms that prohibit automation

---

## 12. Operational Notes

### 12.1 Repo location
`github.com/{your-username}/kaide-recon` — private. Don't share access without an explicit operational reason.

### 12.2 Secrets handling
`.env` gitignored. API keys (`GEMINI_API_KEY`, `NIA_API_KEY`, `GITHUB_TOKEN`) loaded from local env. Rotate immediately if exposed.

### 12.3 LinkedIn PDF handling
LinkedIn PDFs are sensitive. Gitignore the entire `dossiers/*/raw/linkedin/` path. PDFs live locally only.

### 12.4 The pipeline is for B2B AI startup founders specifically
Don't pre-emptively generalize. If you ever want to pitch outside that ICP, the prompt template needs re-tuning. Don't try to make it universal.

### 12.5 First sale rule
The pipeline earns its existence when the first £10k engagement closes. Until then, every weekend hour spent on it is being measured against active outreach work. Watch for the failure mode where pipeline-building displaces actual selling.

---

## 13. The Bet

Kaide-recon is a bet that *research depth, not outreach volume*, is the conversion lever for Kaide Labs' specific ICP (technical-buyer founders at YC-backed B2B AI startups).

If the bet is right: every pitch lands with the recipient thinking "this person already understands my stack." Conversion compounds. The £10k engagement model becomes sustainable at 3-5 closes per year.

If the bet is wrong: research depth doesn't move conversion, and Kaide Labs needs to figure out a different lever. The pipeline becomes shelfware. ~$50/quarter and 1-2 weekends of build time is the cost of testing the bet.

That cost is worth it. One closed engagement returns 100x.

---

## 14. Open Questions Parked

- Should dossiers expire after 6 months without an engagement? Probably yes — stale recon is misleading. But how to handle the case where a prospect goes quiet for 8 months then suddenly responds? **Answer in V1.1.**
- Is there value in a public version of this (recon-as-a-service for other founders)? Probably yes commercially, but it's a pivot from Kaide Labs' core. **Defer until 5 closes have happened on the FDE strike team offer.**
- Do you sometimes need raw human-only research (e.g., asking a mutual contact about a founder's reputation)? Yes. The pipeline doesn't replace that — it complements it. Capture relationship intel manually in the dossier under a "human intel" section.
