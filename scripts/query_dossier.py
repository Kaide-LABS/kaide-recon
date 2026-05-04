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
    if len(sys.argv) < 3:
        print("Usage: python scripts/query_dossier.py '<founder_name>' '<company>'")
        sys.exit(2)
    print(QUERY_TEMPLATE.format(founder_name=sys.argv[1], company=sys.argv[2]))
