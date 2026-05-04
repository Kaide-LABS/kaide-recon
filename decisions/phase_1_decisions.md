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
