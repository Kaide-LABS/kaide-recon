# Phase 3 Decisions

## Cost Ledger

| Item | Estimated | Actual |
|---|---|---|
| Deep Research Max | ~$5.00 | ~$5.00 |
| Flash routing | $0.00 | $0.00 |
| Files API uploads | $0.00 | $0.00 |
| Nia indexing | $0.00 | $0.00 |
| **Total per-prospect** | **~$5.00** | **~$5.00** |

Active human time per run: ~15-20 min. (Well within the 30-min budget constraint).

## Patches Applied

*   **`scripts/query_dossier.py`:** Patched to include a `CRITICAL INSTRUCTION` explicitly preventing Claude from using local bash scripts or the GitHub CLI (like `repos.sh`). When asked to query the newly gathered Wexler dossier, Claude's MCP agent initially tried to use local scripts to traverse the `Kaide-LABS/kaide-recon` repository. Because the repository is private and the local environment lacked a `GITHUB_TOKEN`, this approach failed with a 404. By patching the query to strictly demand the use of Nia's MCP `/v2/search` endpoints, Claude successfully used the unified search tool to locate the indexed `dossier.md` content and synthesize the cited outreach angles.

## Retrospective

The Phase 3 execution ran smoothly over a real second-prospect validation case (Gregory Mostyn at Wexler). The pipeline successfully handled partial gathering execution (handling the absence of specific Twitter/HN inputs gracefully) and manually ingested additional context via the `raw/` artifact drops (e.g., an article text drop). The final dossier passed all requirements, triggering an optimal, citation-backed response via the Claude + Nia MCP integration.

V1 SHIPPED
