# Phase 1 Decisions

## Architecture
- Following 4-layer architecture: Gathering, Synthesis, Indexing, Querying.
- Model lock: `deep-research-max-preview-04-2026` for Synthesis, `gemini-3-flash-preview` for Routing.

## Optimizations for Internal Tool
- No abstract base classes for gatherers.
- Minimal error handling: fail fast, fail loud.
- No logging library; using `print`.
- No tests; validation via end-to-end smoke test.

## Gatherer Specifics
- `gather_twitter.py` uses Nitter. Default instance `nitter.net` used but can be overridden.
- `gather_hn.py` uses Algolia REST API.
- `gather_podcasts.py` focuses on YouTube transcript extraction.

## Synthesis
- `research.py` uses `google-genai` `interactions` API with `background=True`.
- Multimodal grounding via Files API.

## Indexing
- `index_to_nia.py` targets `/v2/sources` with `type` discriminator.

## QA Patch (post-review, 2026-05-04)
Three deviations fixed in `research.py` against PHASE_1_SPEC:
- **Multimodal grounding restored** (spec §3.2 / §5.1): `interactions.create(input=[prompt, *artifacts])` now passes the uploaded `File` objects as list elements. The previous implementation discarded the uploaded refs and inlined text into a single-string prompt, which silently dropped PDFs and images (LinkedIn `profile.pdf` was effectively absent from synthesis).
- **Cost gate added**: prints `~$5.00` estimate + 5s Ctrl-C window before kicking off the Max run. Prevents surprise spend.
- **Wall-clock timeout added**: poll loop capped at 120 iterations × 30s = 60 minutes. Prints the still-running interaction id on timeout so the operator can poll manually instead of hanging.

James He dossier from the original (text-inlined) run remains valid — text artifacts grounded successfully despite the bug. PDF grounding will be exercised on the next prospect.
