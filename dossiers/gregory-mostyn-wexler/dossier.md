# Founder Dossier: Gregory Mostyn (Wexler)

Gregory Mostyn represents a highly specific archetype in the B2B AI landscape: the domain-native visionary paired with a deeply technical co-founder. Steering Wexler—a "Fact Intelligence" platform for complex litigation—Mostyn has successfully parlayed his family’s deep ties to the UK legal establishment into early enterprise traction with elite global law firms. He is highly articulate regarding the limitations of generic AI models, publicly rejecting "Swiss Army knife" solutions in favor of a precision "scalpel" designed specifically for dispute resolution.

For Kaide Labs, Wexler represents an ideal target profile. They operate in the post-seed window, possess a working core product, and are actively shifting their focus toward scaling enterprise deployments and ensuring ironclad data security. Because Mostyn has explicitly praised the concept of using AI to maximize developer productivity rather than permanently inflating headcount, Kaide Labs’ productized, rapid-sprint FDE (Forward-Deployed Engineer) sidecar model is positioned to resonate perfectly with his operational philosophy.

***

## Executive Summary

*   **Founder Background:** Gregory Mostyn is a domain-native commercial leader from a prominent UK legal family, strategically paired with CTO Kush Madlani, an elite ML engineer with experience scaling distributed systems at Google, Amazon, and J.P. Morgan.
*   **Company Snapshot:** Wexler is a post-seed AI litigation startup (with ~$6.7M in total funding and an estimated ARR of ~$1.36M) pivoting from successful proofs-of-concept to massive enterprise deployments across top-tier law firms.
*   **Stated Pain Points and Bottlenecks:** The company is functionally bottlenecked by stringent enterprise InfoSec audits (rooted in Mostyn's anxiety over "Ransomware 3.0" and the lack of continuous exploit validation) and the technical hurdle of scaling ingestion from 500k to millions of evidentiary documents.
*   **Technical Decisions and Preferences:** Wexler utilizes a heavily guarded, model-agnostic neuro-symbolic GraphRAG pipeline, prioritizing AI-driven developer productivity and lean engineering over headcount bloat.
*   **Enterprise Integration Surface:** The ideal FDE targets are entirely upstream: automated red-team security validation harnesses, legacy e-discovery API connectors, and real-time A/V ingestion streams for depositions.
*   **Recommended Outreach Angle:** Pitch an automated, bolt-on security red-teaming sidecar that continuously validates Wexler's APIs against prompt injections and data exfiltration, directly satisfying Mostyn's public demand for enterprise security validation without requiring them to fill their open £75k+ "Founding Security Engineer" role.
*   **Red Flags / Gaps:** The team is fiercely protective of its core IP "black box," highly cash-conscious regarding permanent headcount, and currently obscures its exact underlying cloud infrastructure stack, requiring preemptive GitHub reconnaissance before initiating a sprint demo.

***

## 1. Founder Background

### The Legal Dynasty and the Atypical Path
To understand Gregory Mostyn’s approach to legal technology, one must first understand his immersion in the UK legal establishment. Mostyn is the son of Sir Nicholas Mostyn, a recently retired and highly prominent High Court judge, and his siblings are practicing partners and barristers [cite: 1, 2, 3]. His exposure to the friction of litigation is not theoretical; he cites childhood memories of his father bringing home massive stacks of physical ring binders to review late into the night as the foundational inspiration for Wexler [cite: 1, 3, 4]. 

However, Mostyn’s own professional background is highly eclectic and non-technical. Prior to founding Wexler, his career spanned public relations, marketing (such as serving as Growth Marketing Director at CogX), and even a brief stint as a television actor, where he played a "Posh student" in the second season of the HBO finance drama *Industry* [cite: 5, 6, 7]. 

### The Technical Partnership
Because Mostyn is a domain and commercial expert rather than a software engineer, the technical viability of Wexler rests entirely on his co-founder and CTO, Kush Madlani. The two met in January 2023 during the LD19 cohort of Entrepreneur First (EF), an accelerator program known for pairing domain experts with technical talent [cite: 3, 8]. 

Madlani provides the immense technical counterweight to Mostyn's legal fluency. Holding a Master's degree in Computer Science from Columbia University and a Master's in Machine Learning from UCL, Madlani's background is anchored in elite enterprise scaling [cite: 3, 8]. His career trajectory includes serving as an Equity Derivatives Trader at J.P. Morgan, an Applied Researcher developing fraud-detection models at Tractable, a Software Development Engineer at Amazon (focusing on AWS cloud technologies), and a Senior Software Engineer at Google, where he focused on the scalability and reliability of core infrastructure [cite: 3, 8]. 

**Synthesis for Kaide Labs:** Mostyn is the ultimate buyer, but Madlani is the technical gatekeeper. Outreach must appeal to Mostyn’s commercial drive—specifically his desire to close enterprise deals and solve specific integration bottlenecks—while providing technical artifacts that prove to Madlani that Kaide Labs operates at a Google/JPMorgan tier of engineering rigor. 

## 2. Company Snapshot

### Wexler: Fact Intelligence for Litigation
Founded in 2023, Wexler operates in a highly specific niche of the legal technology market: Fact Intelligence for dispute resolution [cite: 9, 10]. Rather than attempting to build a generalist AI that drafts contracts and answers broad legal queries, Wexler focuses exclusively on the extraction, verification, and chronological ordering of facts from massive litigation datasets [cite: 1, 11]. 

The company recently secured a $5.3M Seed funding round led by the Bay Area-based Pear VC, with participation from Seedcamp, Myriad Venture Partners, and The LegalTech Fund, bringing their total raised capital to $6.7M [cite: 9, 12]. Since its pre-seed round, the company’s ARR (Annual Recurring Revenue) has reportedly grown 20x, reaching an estimated $1.36M [cite: 9, 13]. The team currently consists of 11 to 20 employees based primarily out of London, though they are actively utilizing the new capital to expand their commercial footprint into the United States [cite: 9].

### Product Attributes & Market Positioning
Wexler has achieved notable early adoption among elite global law firms. Their disclosed client roster includes Clifford Chance, HSF Kramer, Goodwin Procter, Burges Salmon, and Addleshaw Goddard [cite: 12, 13, 14]. 

*   **Functional Scope:** The core platform ingests up to 500,000 documents per matter, analyzing them at the "fact level" to build verifiable chronologies and expose timeline conflicts automatically [cite: 11, 13, 15]. Additionally, the newly launched "Wexler Real-Time" feature ingests live audio streams from depositions and hearings to perform real-time fact-checking, instantly flagging false or contradictory testimony as it is spoken [cite: 4, 16, 17]. 
*   **Current Price/Cost:** Wexler avoids a standard flat SaaS fee. Instead, they price "by the page," allowing enterprise law firms to purchase bulk packages of pages (e.g., a 500,000-page limit) to be drawn down and allocated across multiple client matters [cite: 18]. This aligns perfectly with law firms' need to pass specific technology costs directly through to the client as billable disbursements.
*   **Availability:** Live, deployed globally, and currently supporting multilingual, region-specific operations across the US, UK, Europe, Canada, and Australia [cite: 13, 17].
*   **Real-World Context (Ideal vs. Anti-Use Cases):**
    *   *Ideal Users:* Specialist litigation and disputes teams, forensic accountants, and internal investigators dealing with massive, complex, and unstructured evidentiary records (e-discovery adjacent) [cite: 9, 11, 18].
    *   *Anti-Use Cases:* Firms seeking generalist contract drafting, corporate due diligence, or simple M&A support should avoid Wexler. Mostyn strictly contrasts Wexler against generalist platforms (such as Harvey and Legora), stating that generalist tools "treat documents as text to analyse rather than evidence to mine" [cite: 11].

### Future Outlook and Expansion Hurdles
Wexler is aggressively scaling beyond document ingestion. Mostyn's stated future roadmap includes:
1.  **Expansion into the UK Bar:** This presents a massive structural hurdle. The UK Bar operates as a "split profession," meaning independent barristers who share the same chambers may simultaneously represent opposing sides in the same dispute [cite: 15]. Any software deployed in this environment requires flawless data siloing and absolute protection against cross-contamination.
2.  **Applying Law to the Facts:** Once the factual matrix of a case is fully mastered, Wexler intends to evolve the product to begin automatically applying rigid legal statutes and frameworks directly to those extracted facts [cite: 15]. 

**Synthesis for Kaide Labs:** Wexler has transitioned from a proof-of-concept startup to a company attempting to digest massive, highly sensitive enterprise datasets from some of the most risk-averse organizations in the world. Their recent push into real-time audio ingestion and massive document scaling introduces severe enterprise integration and pipeline stability challenges—an ideal environment for an FDE sidecar.

## 3. Stated Pain Points and Bottlenecks

### Security Validation vs. Security Dashboards
Mostyn has publicly expressed deep anxiety regarding the security vulnerabilities introduced by AI at the enterprise level. In a recent thought leadership article, he warned of the "confidence gap" where financial and legal institutions deploy AI code faster than they can validate it, leading to "Machine-Speed Failure" [cite: 19, 20]. He further theorized the advent of "Ransomware 3.0," wherein threat actors shift from simple data encryption to LLM-driven orchestration and malicious data integrity manipulation [cite: 19, 21].

Crucially, Mostyn explicitly stated a core pain point regarding info-sec tools: *“A green dashboard does not mean you are secure... Real security is not about how calm your dashboard looks. It is about how thoroughly your environment has been tested and validated... Continuous penetration testing and exploit validation give you evidence, not assumptions”* [cite: 19].

**The Real-World Threat (Hypothetical Case Study):** To ground Mostyn's fears, consider a hypothetical deployment at an AmLaw100 firm. If a global firm integrates an unvalidated LLM agent without continuous adversarial testing, a bad actor (or even an accidental "prompt injection attack" from a careless associate) could manipulate the retrieval index. This could result in a cross-matter data leak, where highly confidential M&A strategy documents are exposed to a litigation team operating on the other side of a Chinese wall within the same firm. This type of data integrity failure would instantly destroy a top-tier firm's reputation and invite regulatory sanctions. 

This public philosophy perfectly aligns with a glaring operational bottleneck: according to the company's Ashby job board, Wexler is currently attempting to hire a **Founding Security Engineer**. The role is listed as an on-site position in London with a salary band of £75K–£100K [cite: 19]. The length of time this role has been open, combined with the relatively low salary band for an elite, AI-fluent security engineer, indicates they are struggling to fill a critical gap required to pass risk-averse enterprise vendor security assessments.

### Scaling from 500k to Millions of Documents
In a recent interview with *Artificial Lawyer*, Mostyn highlighted a major technical hurdle: scaling their ingestion pipeline. While Wexler can currently handle 500,000 documents per matter, the stated roadmap goal is to expand this scale to "millions of documents" [cite: 13, 15]. Handling this volume of unstructured, multi-format legal data (emails, PDFs, scanned footnotes) requires immense pipeline optimization and robust external data connectors (e.g., integrating with existing e-discovery platforms like Relativity).

**Synthesis for Kaide Labs:** Wexler is bottlenecked by enterprise security validation and ingestion scalability. They need elite engineering to pass stringent law firm InfoSec audits and scale their pipelines, but they are trying to hire for this locally in London at a mid-market salary. Kaide Labs can immediately step into this gap for £10k/month without permanent headcount.

## 4. Technical Decisions and Preferences

### The Neuro-Symbolic, Agnostic LLM Pipeline
Under CTO Kush Madlani's direction, Wexler does not rely on a single foundational model. Mostyn describes their architecture as a "model agnostic, basically daisy chaining together multiple different models in a LLM pipeline," utilizing a "neuro-symbolic approach" [cite: 15]. 

*   **Jargon Definition (Neuro-symbolic approach):** A hybrid AI architecture that integrates the raw pattern-recognition power of neural networks (LLMs) with the strict, rules-based logic of symbolic systems. 
    *   *Analogy:* Neural networks are the junior associates rapidly reading and summarizing thousands of pages of unstructured evidence, while the symbolic engine is the senior partner applying rigid, unchanging legal frameworks to ensure the final logic holds up in court. 
    *   *Relevance to Sidecar:* Kaide Labs FDEs must respect this duality. Sidecar connectors must be designed to feed raw data cleanly into the neural layer without corrupting or bypassing the symbolic logic's strict operational constraints.

*   **Jargon Definition (GraphRAG):** Graph Retrieval-Augmented Generation. Instead of merely chunking text into raw vector embeddings, GraphRAG maps entities and their relationships into a structured knowledge graph before passing them to the LLM [cite: 15, 22].
    *   *Analogy:* Standard RAG is a massive, searchable filing cabinet. GraphRAG is a detective's corkboard, with red string explicitly connecting suspects, dates, and locations.
    *   *Relevance to Sidecar:* Sidecars handling upstream ingestion must not simply dump raw text; they should ideally structure and sanitize their outputs to easily map into nodes and edges when entering the Wexler core. 

To manage this complex pipeline, Wexler separates models strictly by task complexity.

| Specification | Worker Models | Reasoning Models |
| :--- | :--- | :--- |
| **Functional Scope** | Initial brute-force extraction, tagging, and structuring of massive document troves. | Higher-order logic, legal reasoning, and final answer/work-product production. |
| **Assigned LLMs** | GPT-4o, Gemini 2.5 Flash. | Claude 4, GPT-5. |
| **Performance Characteristics** | Optimized for extremely high throughput and broad contextual sweeps across thousands of pages. | Optimized for deep, multi-step logical deduction. Evaluations showed Claude 4 is notably more concise than GPT-5 for legal phrasing. |
| **Cost / Latency Tradeoffs**| Lower cost per token, fast latency to accommodate bulk ingestion. | High compute cost and slower latency, strictly reserved for final layer processing to preserve runway. |

Furthermore, the system is strictly sandboxed; it is not permitted to search the external internet, mitigating the risk of introducing fabricated legal citations or exposing confidential client data [cite: 4].

### Lean Engineering and AI-Assisted Productivity
Mostyn is highly conscious of headcount and operational bloat. In an interview, he explicitly referenced a blog post by Ross McNairn (CEO of Wordsmith AI) regarding the use of AI to write software code [cite: 15]. Mostyn stated, *"We're definitely leveraging that to increase productivity in the team without having to hire extensively, which is a really interesting time to be building a startup"* [cite: 15].

**Synthesis for Kaide Labs:** Wexler's core GraphRAG engine is highly sophisticated and heavily guarded. This is where Kaide Labs' **DMZ Rule** (Demilitarized Zone) becomes a massive selling point. Kaide Labs must emphasize that they will *never touch* Madlani's proprietary pipeline. Instead, Kaide Labs will build upstream sidecars—such as secure document ingestion APIs or automated red-teaming scripts—that integrate seamlessly with the core while respecting the team's preference for lean, non-bloated engineering operations.





## 5. Enterprise Integration Surface (KAIDE LABS-SPECIFIC)

Based on the Kaide Labs offer (1-week sprint cycles, upstream/sidecar deployment, strict DMZ rule respecting core IP), the following areas represent the optimal enterprise integration surfaces at Wexler:

### Surface A: Automated Exploit Validation / Security Red-Teaming (The "Founding Security Engineer" Sidecar)
*   **The Problem:** Mostyn demands "continuous penetration testing and exploit validation" to satisfy law firm InfoSec audits and prevent Ransomware 3.0 [cite: 19], but they cannot easily hire a Founding Security Engineer at their current London salary bands [cite: 19]. 
*   **The Sidecar:** An automated, bolt-on red-teaming pipeline that sits outside the core GraphRAG engine. This sidecar systematically bombards the Wexler API with **prompt injection attacks** (malicious user inputs designed to override an AI model's instructions to execute unauthorized actions or leak sensitive data), simulated data exfiltration attempts, and compliance checks, outputting a continuous validation report. It satisfies enterprise InfoSec requirements without touching Wexler's codebase.

### Surface B: "Wexler Real-Time" Audio Ingestion Connectors
*   **The Problem:** Wexler has launched real-time fact-checking for depositions and hearings [cite: 16, 17]. To do this at enterprise scale, they must integrate seamlessly with the fragmented, highly secure A/V software environments used by global law firms (custom Zoom instances, Microsoft Teams, legacy court recording software).
*   **The Sidecar:** A robust, enterprise-grade ingestion API wrapper. Kaide Labs can build secure, latency-optimized sidecars that capture audio streams from these diverse enterprise environments, sanitize the data, and feed it cleanly into Wexler’s fast worker models.

### Surface C: Upstream E-Discovery Connectors (Scaling to Millions)
*   **The Problem:** Moving from 500k to millions of documents [cite: 13, 15] requires moving beyond simple UI uploads. They need direct API integrations with massive, legacy enterprise e-discovery platforms (like Relativity or Everlaw).
*   **The Sidecar:** A data-pipeline sidecar that acts as a secure bridge between legacy e-discovery platforms and Wexler's GraphRAG ingestion layer, handling rate limits, format conversions, and scale-out queueing.

## 6. Recommended Outreach Angle (3 angles, ranked)

The cold pitch must be hyper-specific, referencing Mostyn's public statements and delivering a bespoke artifact (demo) that proves immediate FDE value.

### Rank 1: The "Ransomware 3.0 / Security Validation" Angle (Highest Probability of Success)
*   **Logic:** Directly targets his recent thought leadership on continuous exploit validation [cite: 19, 21] and a painfully open, high-priority job requisition for a Security Engineer. 
*   **The Hook:** *"Greg – read your recent piece on Ransomware 3.0 and the danger of trusting 'green dashboards' over continuous exploit validation. I also noticed you've been trying to hire a Founding Security Engineer for London to tackle exactly this."*
*   **The Pitch:** *"I run a forward-deployed engineering strike team. We don't touch your core GraphRAG IP (strict DMZ rule). Instead, I build bolt-on security sidecars. I saw you need continuous validation to close risk-averse law firms. I’ve built a demo of a continuous red-teaming pipeline that sits upstream of an LLM ingestor, automatically launching prompt injections and generating the exploit validation evidence required for enterprise InfoSec audits."*
*   **The Artifact:** A lightweight demo/video of an automated testing harness continuously probing a dummy RAG API and generating a law-firm-ready "Exploit Validation Report."

### Rank 2: The "Wexler Real-Time" Audio Connector Angle
*   **Logic:** Targets their newest, most vulnerable product feature that relies heavily on messy, low-latency enterprise integrations [cite: 16, 17].
*   **The Hook:** *"Greg – congratulations on the Pear VC round and the launch of Wexler Real-Time. Real-time deposition fact-checking is brilliant, but dealing with custom law-firm Zoom and Teams IT policies to extract that live audio stream without latency is an integration nightmare."*
*   **The Pitch:** *"I operate a strike team that builds enterprise integration sidecars. My DMZ rule means I never touch your core factual intelligence engine. I just build the upstream plumbing. If enterprise audio ingestion is bottlenecking your real-time deployments, I can build the secure API connectors in a 1-week sprint."*
*   **The Artifact:** A demo of a secure, latency-free audio streaming pipeline capturing a live feed from a mock enterprise Teams environment and routing it cleanly to an external endpoint.

### Rank 3: The "Ross McNairn / Lean Scale" Angle
*   **Logic:** Appeals to his specific mention of a peer founder and his explicit desire to scale without "hiring extensively" [cite: 15].
*   **The Hook:** *"Greg – loved your Artificial Lawyer interview. Your point about using Ross McNairn’s AI-assisted coding philosophy to keep the Wexler team lean rather than over-hiring really resonated."*
*   **The Pitch:** *"That exact philosophy is why I built Kaide Labs. We act as productized, bolt-on Forward Deployed Engineers for post-seed AI teams. You mentioned scaling Wexler’s ingestion from 500k to millions of documents. Instead of permanently inflating your engineering payroll to build those enterprise data connectors, I embed for a rapid sprint, build the upstream sidecar to handle the data flow, and hand it over. No long-term overhead."*
*   **The Artifact:** A demonstration of a highly scalable, asynchronous document-queueing sidecar capable of handling 1M+ dummy JSON payloads, designed to sit upstream of a worker model.

## 7. Red Flags / Gaps

When approaching Mostyn and Wexler, Kaide Labs should be acutely aware of the following operational and technical dynamics:

*   **The Missing Cloud Infrastructure Stack (Crucial Gap):** The provided research and public postings do not explicitly confirm Wexler's underlying cloud architecture or primary backend language (e.g., AWS vs. GCP, Python vs. Go). Because Kush Madlani has extensive AWS experience from his tenure at Amazon [cite: 8], it is highly probable they lean heavily on AWS, but this is unconfirmed. **Mitigation:** Before building a sidecar demo, the Kaide Labs founder *must* execute a deep technical reconnaissance (e.g., scanning Madlani's GitHub, analyzing header responses, or looking for specific cloud certifications in Wexler's engineering job postings) to ensure the FDE sidecar artifact is natively compatible with their exact environment.
*   **Non-Technical CEO Gatekeeping:** Because Mostyn relies heavily on Madlani for technical execution, an overly technical pitch might bounce off Mostyn, while an overly commercial pitch might get vetoed by Madlani. **Mitigation:** The cold outreach must lead with the business value (e.g., passing InfoSec audits, saving headcount costs) to hook Mostyn, but the attached artifact/demo must be technically flawless to instantly win over Madlani when Mostyn inevitably forwards the email to him.
*   **Cash Consciousness:** Despite raising $6.7M total [cite: 9], their job postings list engineering roles in London at £70K–£100K [cite: 19]. This is distinctly mid-market for elite AI talent, signaling that the founders are fiercely protective of their runway and highly conservative regarding burn rate. **Mitigation:** Position the £10k/month productized engagement not as an expense, but as a massive cost-saving measure compared to the fully-loaded cost (taxes, equity, benefits, recruitment fees) of a permanent senior engineer. Emphasize the "first month refundable" safety net.
*   **The Core IP "Black Box" Paranoia:** CTOs building complex GraphRAG and neuro-symbolic pipelines are intensely protective of their core architecture. They will naturally resist bringing in external contractors who might break their delicately balanced worker/reasoning model prompts. **Mitigation:** The "DMZ Rule" must be the loudest part of the technical pitch. Reassure Madlani explicitly that Kaide Labs builds *wrappers, connectors, and testing harnesses* on the periphery, never altering the core proprietary reasoning engine.



**Sources:**
1. [geeklawblog.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG2L0kk7jIbYTtY-MOCa4ZRl3H6atZH6h6F6M5JgVoYs1CJxO1CcwAujQe4d_HhdyBfPwmwUlngEx-Xw4fWWyKVt0kAatxXime8pXxYrbddto8uTf_oDY_KM6XVuYcx_StHjadyskYZs7nmZfMyft3uHaKo2aw_QjmLjozU8iX8GP7MWhNZqB2O_03I-VA_nhaOD2__gL1nkQUFgi_aYXgLnP7qRdmh72hE11T5MxWWVQ8JXZtp5yL-njeWecgdylc=)
2. [acast.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHV0xZqs212GYXGT98_MANwgOIazWZIGUYuV34e0D4w42LEe-OdYMR098hHr-PdSKRaIX3-fxB9Evde5ysxlDRJ1OXAXlJiWDvR7O5GoRrJBqn40cVjBBiFl6zvMDOimLQrxm9t62TPoGtazwY=)
3. [wexler.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFd0IJaxQRl78B5_cBtDItq8FzPWCdNBhNdTbL1b2l8DOaLwHf-zKVkS5C6gR0YcOGOuHfV8i8x85_GBXbEizHGTCDNqwmakfA4cDC80-w1739zCPaMVOkBtCDluthYEp9mURT5vRErXBTtv0_U5mb5XZdCaa3ndDLOHf0PLHXYHGGjnTrDvQ-Y2qL9LkhcsSrKpfTlhc4UbhkVFSA=)
4. [apple.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF10qBvIXTX_SnBRbHRr4gKTVnk7tKwbD5FhWjCRnCvS2QXZhHbiujE9SiPrw54VSkktFFJkIGYFvCtqkzM0DixuO55xvTpG8_fszW21GeyR-31aWTSrZC8M1-EmDP3el4cJ1u8MXKQyaEhTUHN5gP4oX-BC4WvfZXNqYXrYH0JRZzPhuSOBJVnEU5ILuFyZVrAPK-AOk1xAvY8gE6jkQjicVNduAY6RQfKWmikf9kCZZ2euEB-OF3YIw==)
5. [moviemeter.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHUnTSHmr5QDllgf64IYrQYCzUYWhjnvGlaSSTokApk3cb9yrNvxk6ttqqHQEt6-8pSyoOhwOxwvoi3a7r373N7oMCpqUabmhVwkM-6CGxjx8RTQNPaKX9UBa6pOAoPKXPyTB2ouVPPA11qWwR-6sE=)
6. [betaseries.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE51_dMIsMOtweqOf15kQjOCJYG8G3xtmSwcdXlYV1woep1QRrTweJKe0257LkXvTSRytawIdKN7BOINF7IgoVYxhQDhnivovqbaEbu4SxhyEsV9Po6V_NVTHvu6Ff_XrE=)
7. [substack.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHI3F0EZmUYbIzJtRH3KO_4LEBEj6qAhaOb9iifT91uuOEIoBNzEo1LLqI15GRDDKz4PMlTMGFUGI3W6AXmZZz5s8wXZPVAVC8gxR5s0KJ276nXA5pwX--XzPNK4ja68QsHfqT0UAjVkc26ojOlel-R04-gNg==)
8. [highperformr.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFoIdVL-SRJxf9WdD8JN61iDRy7mvYt2rJ58fGzEBDR3SF9p-j4HFQk3RkAwCJx4-wrWdynMaXUtpehOWSdv2GMqBDgqYa8A3GGqMGNUkxAublCwLNTBxzr9ImsdN2JLEYqGF-Bai_JHkmXDl3J)
9. [prospeo.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7YIc0bPFVC3hXx63daH3hjv_YGux-VI2-DOKyd0qg-67QzVk2KGSSyNgAQYfUMzffSp2r0f-uwPljRn_UnCjqvo4QoUOLiGiS7OTPVUlA-g==)
10. [legaltechnology.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEsrZwOdbpjcD6eV92rpOLbJfi50lPEQfjoVOhAPQXRAU7iTdFGkMkE5NmLI4OxNtnzMzHG24aYU8FoPUj8tlYXtj62mPKRSZRHrT-Kb25vwM5re3vKWQcWS1xCQSdmDBt3hR2a7UaTXFmjaVpf7U8Lvy1hNiyT972fgkyY9IghYgpuHNBBilCwKgX_dkuQYkmJOh9P2g==)
11. [wexler.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHkxOXATCIrrE89tubVaaiqTQN7QaxW7klVXx2BskcR4_P-5CNrNhzx1H2Xk9zxC3BG0jgnNsSeStZOPlfJ3iJGDfJKobCI2HYYcF2X9M17WL_Wk84WySyu1A4NVWfhyz0pbz1fmjJGfjzdDGp-ws=)
12. [legaltech-talk.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEi-PBrCFImY27hbUtGTsQq2LhKW3FkH4U0NCQXHAKB61Ht6lbB6sbKyJn2U4N-2vVpjh-rZ3P65MoeMliOCTxJpNs0zortBfpPcvgQbn0dfGZsSmSkvXz3ukhKE5TgaVt-yNafs_qZ-awgiIUXkeIbx5mFMs4CLSo2Ca2i6-6AueWk0j2ZkFtyRj205NxV2t5qE8Tg8iTEoHXEd6tnsXODGg3q9KD3_ukvW4lbrWjn3PAZWZSsc5WMrahY4Kl5qIwEMe1lZrNQUg==)
13. [seedcamp.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_ePfDo8l7fmNnKdDBkbP9aKrPgxCnadaCG2oTOxdRAxe4evJTtLV1CBMvQKJvvuTjXEmQ2O9SyHQSiqf_VQlDYpzSP7kHP1bxtxY87T0I3DAvbpjER7G90AG4FjoH5VfzuPtJqXmGWv0P_ONxT4MDe0PsYIdn9ngkHE_XKte8DOsJAg==)
14. [legaltech.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGBsVPIhCmOKl392K-WGV4PkfnlgJmxECarxbGNF2N0SHuBotYGCTp_ctcKZ-_HXiOtZ4EPnv-v7nmMVkB0QBkGPY52ZYR5P2YCcuMWhNuSOTxSw08jYNXJVhIdv8qNkp0pgPr7JhB7ImgBKI6R)
15. [artificiallawyer.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE-2QYW9Rq88-lqoaJsBOWdfgNd_Cqr4q_dkDDYAkIjsY5kKDo-JRl5hDqJqbLTZEUCxSdLMm6dcu33fgSrSTJ7rkbTGtgAiqBEIEsCcosF330-RLk0gOkP4eocG4T_m8Ew5F6dGabs9fJ8rMTz26F1tdraQG9L2TVuSBIVI4POcdu-9RZ_CETXJ_-mMUG0hCARDx8O)
16. [wexler.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHAKpqoHI9y4SBjy7sL20DNPQkZP9orXJX-LaOFS0tLM8h_dKclioP3Qjosk4VPBPlbcywjkTIuSSUDnQA8Hl1YLLUtDkn_QYOPQvvxZn0IhZA--swJCUCTfJ_hhoIMhsTFGUYHy7M07qUJ6rJ-C9YyRKPvgf_y7JCAEvgPrZCS1AONYedWwyXqWD99Lu-E7eTs9B9M_B8=)
17. [tech.eu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEA_Dl5XZhPHmOkTq6a8zU9XsJSwheqNXOUPO-3ESKcrizR9kr2dT-BmEpuD-CPsKUZNI4FgGhrJYHLhSFksMiJ411L7sVf5pw0abHPkmeycpNqXdK22r1ocExfD_CAa4p2F3YopN-6FUzWHrEiPoLi7TZxLMSv5nFAc3B-Wg1mc19XGuN7JIl2AISemu7XD7VAPNEb)
18. [artificiallawyer.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHE6YPWIElR9parDeFwi58_O8xQfnPKsDEaZeKk5K3ZJpuAGYj9vc04A5YjAz35flccPsvJvWbhsL_QPOJYc8IuqfnpM2IvSgijxYd8mpyBALH5JM1mGRFj59DD-Mbu0a26pBwFO-looXw3OhhJT2audg0h5rqeb_EMlZr4RnX7CcyvVnR97Yac71dDr-mMepHjkCl7jn5NUZYt)
19. [interface.media](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGYBkMiY1yfnnSEJrVSdEBJCpBtQEcmS4zZG15GwR9pHvHhIA31te9xU8CgmgGvBtVT_MeXo8Y-0vyowV4_prFD54EZRoobNbU6gNkB-jHFPPrOz0NulXCXGYxsw_XshPSAnabHEQ==)
20. [fintechstrategy.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHep45_ePJcA0dBndt14W2VnCWkUYjfYu7PxIKa6GInw3BFsWa1FRWjwU4I-OCslxQhzynPYcKgULElizNHvhjG0hI4Lp9GNVBF1mvXw1pfaVolbeztKxbtQJEGnNAgxB-eLjJ6HZjAztMr9JZk)
21. [interface.media](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF8LEE_ukWWA_GSr7leHGbfltT7QOGpHuq6o3kuiwJrYtHF2lFYa_-qO51s3MxSj8plVGsv1U5tf9g0XbLAJqgUAiKMuu7vu-Iq59AOMEQGhqK1fnn6MaRlh04YAvDucfk=)
22. [tipranks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHRKzhJy0z_c_85Az43VJDi9yA2KIGWeTplM08Xb7yRjB3cHETER3eastNM11_TJohIlvwnsLtEfeQp0PysRK-ANI0kgmtvPYdSvtPsmbP0MWi8AR0id2erlvLfAGBkZNcqfB_AIDiy5HDMZe5sSjWxoSAjeixvAbg9xPXbBWqzkwL3t7IiemRVccNeUStBk57jrWNwjXrt3m9ImSVm92uUMCc4usnZiAXD4xXKTlChaINM_dTBzZcADJ5jqFzW)


