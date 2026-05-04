# kaide-recon

## 3.1 Header

Productize the founder-research → cold-outreach loop so that Kaide Labs can pitch B2B AI startup founders with genuine specificity at a rate that compounds across quarters.

If you are reopening this repo cold, run `python scripts/validate_pipeline.py` first.

## 3.2 What This Is / Is Not

- Not a CRM. Folk handles CRM. This pipeline produces inputs that feed Folk.
- Not a sales engagement platform. The send mechanism stays in regular email + LinkedIn.
- Not a mass outreach tool. Volume target is 3-10 prospects per quarter, not 100s per week.
- Not a clone of existing GTM stacks. Kaide-recon is intentionally specialized for technical-buyer hyper-personalization, not generic SDR-team workflows.

## 3.3 Hard Constraints

- Manual LinkedIn only — no automation, ever.
- Cost ceiling: ≤ $15 per prospect.
- Time ceiling: ≤ 30 min active human time per prospect.
- Stack lock: do not change models or endpoints without updating `design_doc.md` §1.1.

## 3.4 First-Time Setup

```bash
git clone <repo>
cd kaide-recon
python -m venv venv && .\venv\Scripts\Activate.ps1   # PowerShell on Windows; bash: source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env   # then fill in GEMINI_API_KEY, NIA_API_KEY, GITHUB_TOKEN
python scripts/validate_pipeline.py   # confirm everything's wired
```

## 3.5 Adding a New Prospect (the 30-minute path)

1. `python scripts/orchestrate.py "<Founder>" "<Company>" [twitter_handle]`
   - Runs gathering scripts in parallel. Takes a few minutes. Creates the raw/ dossier.
2. Drop LinkedIn PDF into `dossiers/<slug>/raw/linkedin/profile.pdf`
   - Drop activity screenshots into `dossiers/<slug>/raw/linkedin/activity_screenshots/`
3. `python scripts/research.py "<Founder>" "<Company>" "dossiers/<slug>/raw"`
   - Synthesizes the dossier. (~15 min wall-clock, ~$5; you'll get a 5s abort window).
4. Review `dossiers/<slug>/dossier.md`, edit if needed, git commit + push
   - Manual QA of the output.
5. `python scripts/index_to_nia.py repo "<gh-user>/kaide-recon" master`
   - Indexes the new dossier into Nia (and optionally: founder repo, company repo, company docs).
6. `python scripts/query_dossier.py "<Founder>" "<Company>"`
   - Paste output into Claude (with Nia MCP attached). Read 3 angles, edit, send.
7. Update `intake_checklist.md` with outcome.

## 3.6 Re-Pitching a Stale Prospect

If a prospect has gone cold and you want a fresh angle, run:
`python scripts/repitch.py "<Founder>" "<Company>" [twitter_handle]`

Note: re-pitch only triggers a fresh $5 Max run if Flash classifies the delta artifacts as `RE_SYNTHESIZE`. Otherwise, it skips the spend and prompts you to query the existing dossier.

## 3.7 File Map

```text
scripts/        — pipeline scripts (don't edit unless changing architecture)
prompts/        — locked prompt templates (edit cautiously)
dossiers/       — one folder per prospect
decisions/      — phase decision logs (audit trail of deviations from spec)
PRD.md          — why this exists + scope
design_doc.md   — architecture + endpoint reference (canonical)
PHASE_*_SPEC.md — what each phase shipped
```

## 3.8 Troubleshooting

**Q: Deep Research Max hangs / never completes**
A: Poll loop times out at 60min and prints the interaction id; run `client.interactions.get(<id>)` from a Python REPL to inspect.

**Q: Nitter is rate-limiting**
A: Set `NITTER_INSTANCE=https://<other-mirror>` env var and re-run `gather_twitter.py` only.

**Q: Nia returns 409**
A: Already indexed, that's success.

**Q: I forgot what state a prospect is in**
A: Open its `intake_checklist.md`.

**Q: I want to spend less than $5 on a re-pitch**
A: Use `repitch.py`; it runs Flash classification first and skips the Max call if the delta is thin.

## 3.9 What's Banned

- Automated LinkedIn anything.
- Adding pip dependencies without updating `requirements.txt` and `decisions/`.
- Changing the model IDs.
- Sending outreach from a script (always human-gated).

## 3.10 First Sale Rule

The pipeline earns its existence when the first £10k engagement closes. Until then, every weekend hour is measured against active selling.
