# Phase 2 Decisions

## Architecture
- Added `scripts/validate_pipeline.py` to allow Future-Hafeedh to easily check if the pipeline is ready to run.
- Added `scripts/repitch.py` to handle the delta gathering and conditional re-synthesis flow.
- Reused `subprocess.run` inside `repitch.py` for gatherers instead of refactoring `orchestrate.py` into an imported library, preserving the internal-tool principle of flat, independent scripts.

## Prompt Changes
- Appended a `CONTEXT` section to `prompts/router_prompt.md` to clarify the routing agent's role in classifying "delta" artifacts on stale prospects, to ensure accurate KEEP/SKIP/RE_SYNTHESIZE classification.

## Validations
- Made `validate_pipeline.py` gracefully handle the `playwright` check by running a subprocess dry-run install command to avoid cross-platform driver path issues.
