*Disclaimer: This document is an operational reconnaissance dossier designed strictly for informational and strategic outreach purposes. It does not constitute certified legal, compliance, security, or financial advice.*

# Founder Dossier: Kush Madlani (Wexler)

Wexler operates at the absolute frontier of generative AI and high-stakes legal dispute resolution, a domain entirely intolerant of hallucination and latency. Co-Founder and CTO Kush Madlani is the architect bridging complex machine learning theory with strict enterprise realities.

By mapping Madlani’s technical background against Wexler’s publicly stated bottlenecks, this dossier provides highly actionable, artifact-driven outreach angles. The goal is to position Kaide Labs as the ideal rapid-sprint solution to unblock Wexler's enterprise sales cycles without interfering with their core proprietary fact-finding pipeline.

## Executive Summary
*   **1. Founder Background:** Kush Madlani combines a rigorous financial trading background at J.P. Morgan with deep academic and applied expertise in Machine Learning (ML), notably as an Applied Researcher at Tractable. He is uniquely positioned as a technical co-founder capable of managing complex enterprise requirements and rigorous logic gates.
*   **2. Company Snapshot:** Wexler recently secured a $5.3M Seed round to scale its litigation fact-finding platform. The company is actively in a rapid scaling phase, evidenced by a 20x increase in Annual Recurring Revenue (ARR), 2x month-over-month query growth, and headcount expansion to approximately 21 employees as of early 2026. The platform has achieved deep adoption across elite global law firms.
*   **3. Stated Pain Points:** Public job descriptions and product announcements reveal critical tensions: pushing ingestion limits from 500,000 to "millions" of documents per upload, managing massive Large Language Model (LLM) token limits and API costs, localizing for multilingual regions, and maintaining ultra-low latency for their "Wexler Real-Time" feature.
*   **4. Technical Decisions:** Madlani has engineered an iterative multi-LLM architecture (combining models from OpenAI, Anthropic, and Meta) paired with a deliberate 10-15% "over-extraction" philosophy. This ensures comprehensive legal fact-finding but directly exacerbates the token limit and latency bottlenecks mentioned above.
*   **5. Enterprise Integration Surface:** High fit. Wexler's aggressive enterprise expansion requires numerous upstream integrations that perfectly suit a Kaide Labs sidecar under the Demilitarized Zone (DMZ) rule. Prime targets include a live-transcript API middleware, pre-ingestion semantic chunking, and localized PII anonymization wrappers.
*   **6. Recommended Outreach Angles:** The primary recommendation (Rank 1) is the **"Token & Latency" Cost-Reduction Artifact**. Pitching an upstream pre-processor delivered via a locked Loom video directly addresses Madlani’s publicly advertised technical headaches surrounding unit economics and pipeline scale. 
*   **7. Red Flags / Gaps:** Hyper-sensitivity to enterprise data security frameworks (SOC 2/ISO 27001) and resistance to any "black box" summarization tools that might accidentally discard critical case facts. Outreach must aggressively highlight the DMZ rule and deterministic logic.

## 1. Founder Background

Kush Madlani’s trajectory into legal technology is rooted in a blend of high-stakes financial trading, academic machine learning research, and applied artificial intelligence (AI). Understanding his background is critical for calibrating the technical depth of the outreach.

**Early Career and Transition to Engineering**
Madlani began his career at J.P. Morgan, where he worked as an Associate in Equity Derivatives Trading from 2015 to 2019 [cite: 1, 2]. Operating in a high-pressure, data-intensive environment, he began automating manual trading workflows using Python [cite: 2, 3]. This self-directed engineering work eventually catalyzed a career pivot. In 2019, Madlani left banking to travel South America before formally transitioning into computer science [cite: 4]. 

**Academic and Applied AI Research**
Madlani formalized his technical expertise by completing a Master’s degree in Machine Learning at University College London (UCL) in 2020 [cite: 2, 3]. His academic footprint from this era reveals a deep focus on predictive modeling and natural language processing (NLP). His public GitHub repositories contain advanced work on implicit graph convolutional matrix completion (`implicit-gcmc`), word embedding evaluation (`embedtrics`), and word-level Generative Pre-trained Transformers (GPT) trained on arXiv datasets (`arxiv_minGPT`) [cite: 5]. 

Following his degree, Madlani joined Tractable, an AI company focused on visual damage appraisal, as an Applied Researcher (2020–2022) [cite: 1, 2]. At Tractable, he built fraud-detection models and engineered systems for continuous model improvement, granting him critical experience in deploying machine learning architectures in production environments [cite: 2, 3].

**The Genesis of Wexler**
In 2022, Madlani joined Entrepreneur First (EF), a prominent London-based incubator (cohort LD19), where he met his future co-founder, Gregory Mostyn [cite: 1, 2, 3]. Mostyn, the son of a high court judge, brought deep domain expertise regarding the severe inefficiencies in litigation document review [cite: 3, 6, 7]. The partnership leveraged Mostyn's commercial and legal insights with Madlani's scientific background, leading to the incorporation of Wexler (initially known as GLO AI LTD) in 2023 [cite: 2, 8].

*Note on Data Discrepancies:* Certain automated data scrapers falsely attribute periods of employment at Google, Amazon, and Morgan Stanley to Madlani [cite: 1]. These claims conflict directly with the verified timeline established by his academic records, GitHub commit history, and Wexler's official press releases [cite: 2, 3, 4, 5]. Outreach should entirely ignore the Google/Amazon narrative.

## 2. Company Snapshot

Wexler operates at the intersection of generative AI and high-stakes legal dispute resolution. The company positions itself as a "Fact Intelligence Platform" designed specifically to think and process information like a litigator [cite: 5, 9]. 

**Market Position and Value Proposition**
Unlike generalized legal tech wrappers that merely organize eDiscovery files, Wexler is purpose-built to extract facts, verify chronologies, map key actors, and identify evidentiary inconsistencies across massive, unstructured datasets [cite: 3, 5, 10]. The core product acts as an active partner in case strategy, generating verified outputs linked directly to source documents to prevent AI hallucinations—a critical requirement in a field where fabricated citations can result in professional sanctions [cite: 3, 6].

**Recent Financing and Growth Metrics**
Wexler is currently experiencing a rapid scaling phase, evidenced by a 20x increase in Annual Recurring Revenue (ARR) since its $1.4M pre-seed round, a 2x month-over-month query growth, and an overall headcount expansion to approximately 21 employees as of early 2026 [cite: 2, 9, 11, 12, 13, 14]. Precise real-time revenue figures are closely guarded; however, in September 2025, Wexler successfully raised a $5.3M (reported by some outlets as $5.4M) Seed round led by Pear VC, with participation from Seedcamp, The LegalTech Fund, and Myriad Venture Partners [cite: 9, 11, 15, 16]. 

**Enterprise Adoption**
The platform has achieved significant traction within elite, global law firms operating in the "AmLaw 100" (the top 100 highest-grossing law firms in the United States) and the "Magic Circle" (the five most prestigious London-based multinational law firms). Publicly announced clients showcase deep integration:
*   **Clifford Chance:** Has embedded the platform entirely across its dispute resolution practice [cite: 9, 11, 15, 17].
*   **HSF Kramer:** Partner Charlie Morgan stated the firm uses the platform to get an understanding of facts more quickly and effectively, directly improving case strategies [cite: 9, 10, 11, 15].
*   **Goodwin Procter:** Partner Sarah McAtominey reported that associates are thrilled to use the tool, noting it has improved how they tackle cases from the very outset through to trial [cite: 9, 10, 11, 15].
*   **Addleshaw Goddard:** Is already using the tool to actively transform litigation workflows [cite: 9, 11, 15, 17].
*   **Burges Salmon:** Has officially adopted the platform to enhance its overarching legal workflows and explore advanced dispute resolution use cases [cite: 2, 9, 11, 15, 17].

Currently, over 70% of Wexler’s user base is located in the United States, driving a strategic push to expand US operations and localize the platform for multinational deployments [cite: 9, 18]. 

## 3. Stated Pain Points and Bottlenecks

Through a close analysis of CEO interviews, product launch announcements, and engineering job descriptions, several highly specific bottlenecks emerge. These pain points represent ideal vectors for Kaide Labs' FDE interventions.

**Bottleneck 1: Scaling Document Ingestion Limits**
Wexler currently possesses the capacity to process up to 500,000 documents per upload [cite: 9, 11]. However, complex litigation often involves vastly larger datasets. For context, the average civil case in the U.S. contains around 130 gigabytes (GB) or 6.5 million pages of data gathered from 10 to 15 custodians. Complex, multi-billion dollar litigation can easily span multiple terabytes, with a single gigabyte yielding anywhere from 7,500 to 18,750 individual documents depending on the mix of emails and loose files [cite: 19, 20, 21, 22, 23]. In the wake of their Seed funding, the company publicly stated that a primary goal is to "increase the scale of documents to millions per upload" [cite: 9, 11, 24]. Moving from 500k to multi-million document ingestion introduces severe architectural strain on data chunking, vector database indexing, and memory management.

**Bottleneck 2: Managing Token Limits, Latency, and Costs**
This is perhaps the most explicit, technical bottleneck available. An active job posting for an AI Engineer at Wexler lists the following as a mandatory technical requirement: *"Ability to juggle token limits, cost and latency while delivering structured outputs"* [cite: 25, 26]. Because Wexler relies heavily on iterative LLM calls to map complex legal narratives, they are highly exposed to API token bloat. 

Furthermore, their new flagship feature, "Wexler Real-Time"—which flags inconsistent testimony during live depositions—demands ultra-low latency. In the realm of real-time court reporting, this strictly requires sub-second processing. Systems must achieve a latency of less than 300 milliseconds for initial partial tokens and under 800 milliseconds for final transcript generation to maintain real-time conversational pacing without lagging behind the spoken word [cite: 9, 27, 28, 29, 30, 31]. Managing these thresholds makes token and latency management a critical existential challenge for the engineering team.

**Bottleneck 3: Integrating with Legacy Live-Transcript Feeds**
The "Wexler Real-Time" feature requires plugging into live court reporting systems to catch contradictions. *Illustrative Case Study:* In a live deposition, if a witness states on the stand, "I never authorized the payment to Vendor X," the Wexler Real-Time system must instantly cross-reference millions of documents and immediately flag a 2023 email where that specific witness explicitly wrote, "Please proceed with paying Vendor X." 

To facilitate this, Wexler notes that in the US, "real-time transcript feeds are standard, letting Wexler plug straight in," whereas in the UK, "only authorised providers can supply transcripts" due to CPR 39.9 (the UK Civil Procedure Rule that dictates only authorized providers can record and transcribe court hearings) [cite: 27]. Integrating with a fragmented ecosystem of proprietary court-reporting APIs is a massive, unglamorous integration bottleneck that slows down the deployment of their most advanced feature.

**Bottleneck 4: Multilingual and Region-Specific Deployments**
As Wexler attempts to capture more of the global enterprise market, they are forced to adapt their product to different regional legal frameworks and languages. Their recent funding announcements explicitly highlight the goal to "scale multilingual, region-specific deployments" [cite: 9, 11, 24]. Expanding into non-English documents requires upstream OCR (Optical Character Recognition) and translation layers that must reliably normalize data before it hits Wexler's core English-optimized LLM logic.

## 4. Technical Decisions and Preferences

Kush Madlani has engineered Wexler to prioritize extreme accuracy and traceability over general-purpose chat capabilities. His technical decisions reflect his background in applied machine learning and finance.

**The "Iterative" Multi-LLM Architecture**
Rather than relying on a single foundation model, Madlani has designed an architecture that sequences multiple LLMs. CEO Gregory Mostyn revealed that the platform uses OpenAI, Anthropic's Claude, and Meta's LLaMA [cite: 32]. While the exact model versions remain proprietary or undisclosed, industry standard deployments for robust medical and legal reasoning typically utilize top-tier models such as OpenAI's GPT-4o or o1, Anthropic's Claude 3.5 Sonnet or 3.7 Sonnet, and Meta's LLaMA 3 70B [cite: 33, 34, 35, 36]. Madlani joined these models "to operate in sequence in what Mostyn called an 'iterative' process" to create a rigorous fact-extraction pipeline [cite: 7]. This multi-model approach suggests Madlani values model-agnostic infrastructure and routing mechanisms that optimize for specific tasks.

**Deliberate "Over-Extraction" Logic**
To prevent the AI from missing subtle but critical legal facts, Madlani programmed the system to deliberately extract 10-15% more items into the case "fact-bank" than a human reviewer typically would [cite: 7]. While this guarantees comprehensiveness, it actively exacerbates the "token limit and compute cost" bottleneck mentioned earlier, requiring highly optimized Retrieval-Augmented Generation (RAG) pipelines to filter this expanded fact-bank downstream.

**Infrastructure and Security Stack**
Because Wexler handles highly sensitive, privileged legal data, the engineering team has enforced a strict enterprise security posture. The platform utilizes user-specific encryption keys, data masking, and complies with SOC 2 Type II (an auditing standard verifying a company securely manages data to protect organizational interests and client privacy over a sustained period), ISO 27001 (the international standard for information security management systems), GDPR, and AWS Cloud Security standards [cite: 2, 9, 11]. Any technical intervention by an external party must respect these boundaries. 

**Engineering Environment**
Based on open roles, the Wexler backend is heavily Python-centric, requiring "clean, modular Python back-end code for data-intensive systems" [cite: 25]. Madlani's personal GitHub further underscores his preference for Python, specifically using PyTorch and PyTorch Geometric for complex modeling [cite: 5].

## 5. Enterprise Integration Surface (KAIDE LABS-SPECIFIC)

Kaide Labs operates under a strict "DMZ rule"—never touching the client's core product, Intellectual Property (IP), or primary codebase. Wexler’s architecture and current bottlenecks provide several pristine integration surfaces where Kaide Labs can build upstream "sidecars" to unblock enterprise sales.

### The Technical "Handshake" Mechanics
To strictly enforce the DMZ rule while requiring zero custom code from Wexler's engineering team, Kaide Labs sidecars connect to the core infrastructure via standard integration patterns. Outputs from the sidecar are formatted as clean, structured JSON payloads and pushed directly to Wexler’s existing secure RESTful webhooks or dropped into isolated AWS S3 buckets that Wexler's ingestion pipelines already monitor. This completely decoupled handshake ensures Wexler absorbs the processed data organically, just as it would from a native client upload.





### Sidecar 1: The Pre-Ingestion Token Optimization & Chunking Engine
To achieve their goal of uploading "millions of documents" per case [cite: 9], Wexler faces massive token cost constraints [cite: 25]. 
*   **Functional Scope:** An upstream document pre-processor. Before documents enter Wexler's iterative LLM pipeline, a Kaide Labs sidecar can execute deterministic deduplication, metadata extraction, and semantic chunking (the process of breaking text into smaller, meaningful segments based on context—akin to cutting a movie into scenes based on plot shifts, rather than chopping it blindly every 5 minutes) using cheaper, localized embedding models. 
*   **Current Price/Cost:** £10k/month productized engagement, 50% upfront, first month refundable.
*   **Availability:** Rapid sprint cycle (typical: 1-week delivery).
*   **Real-World Context:** *Ideal profile:* Mid-sized cases where legal boilerplate redundantly bloats token costs without adding evidentiary value. *Anti-use case:* Small, highly specific email threads where every single word must be natively processed by the top-tier LLM for nuance.

### Sidecar 2: The Live-Transcript API Middleware
Wexler Real-Time relies on continuous feeds of live audio and text from depositions and hearings [cite: 15, 27]. Because court reporting software is highly fragmented, building bespoke API connectors for every new enterprise client drains core engineering resources. 
*   **Functional Scope:** A bolt-on middleware sidecar that sits upstream of Wexler. This sidecar securely connects to legacy court-reporting APIs, standardizes the raw incoming text stream into a unified, clean JSON format, and feeds it into Wexler's ingestion webhook. 
*   **Current Price/Cost:** £10k/month productized engagement, 50% upfront, first month refundable.
*   **Availability:** Rapid sprint cycle (typical: 1-week delivery).
*   **Real-World Context:** *Ideal profile:* Enterprise deployments relying on older court reporting software or highly specific CPR 39.9 authorized providers in the UK. *Anti-use case:* Courts utilizing modern, standardized digital streams that natively push JSON webhooks.

### Sidecar 3: PII Anonymization and Region-Specific Localization Wrapper
Wexler is aggressively pursuing multilingual, region-specific deployments [cite: 9, 11]. Enterprise clients in Europe often require Personal Identifiable Information (PII) to be scrubbed before touching any cloud-based LLM.
*   **Functional Scope:** A localized, on-premise or edge-deployed sidecar that performs multilingual OCR and aggressive entity masking (scrubbing names, SSNs, and financial data) using local, lightweight models. It passes a secure, anonymized payload to Wexler’s core cloud engine. Once Wexler returns the analysis, the sidecar de-anonymizes the data for the end-user.
*   **Current Price/Cost:** £10k/month productized engagement, 50% upfront, first month refundable.
*   **Availability:** Rapid sprint cycle (typical: 1-week delivery).
*   **Real-World Context:** *Ideal profile:* Multi-national firms dealing in GDPR-heavy jurisdictions like the EU. *Anti-use case:* Domestic US matters already cleared for cloud ingestion under standard protective orders.

## 6. Recommended Outreach Angle (3 angles, ranked)

The cold pitch must act as a delivery mechanism for a specific artifact that proves Kaide Labs can solve a known Wexler bottleneck on a rapid sprint cycle. 

| Rank | Target Pain Point | Proposed Artifact | Technical Effort to Build |
| :--- | :--- | :--- | :--- |
| **1** | Scaling & Token Economics | Pre-Ingestion Semantic Chunker (stripping boilerplate locally to save API costs). | **Low/Medium:** Requires a local embedding model script parsing dummy legal PDFs. |
| **2** | Wexler Real-Time Integrations | Live-Transcript Middleware connector (XML/Legacy API to JSON Webhook converter). | **Medium:** Requires mocking a legacy court XML feed and building a robust normalizer. |
| **3** | Geographic Expansion & GDPR | Localized PII Masking and OCR pipeline. | **High:** Requires deploying a local edge container for masking/de-masking logic. |

**Rank 1: The "Token & Latency" Cost-Reduction Artifact**
*   **The Logic:** Kush is actively hiring for an AI Engineer explicitly to handle the problem of juggling "token limits, cost and latency" while delivering structured outputs [cite: 25]. This is a severe, publicly stated technical headache directly impacting their unit economics.
*   **The Pitch Angle:** "Kush — noticed in your recent engineering JD that managing token bloat and latency is a core bottleneck for your iterative pipeline, especially as you scale from 500k to millions of documents per upload. At Kaide Labs, we build upstream sidecars for AI startups to solve exactly this. I built a lightweight, deterministic document pre-processor that strips redundant legal boilerplate and chunks text using local embeddings *before* it hits your Claude/OpenAI calls, cutting token usage by ~30% without touching your core IP. Here's a demo of how it formats the output."
*   **Logistical Delivery Mechanism:** A locked Loom video showcasing the text processing speed, alongside a sanitized GitHub repository containing the pre-processing logic for his independent technical review.

**Rank 2: The "Wexler Real-Time" Transcript API Connector**
*   **The Logic:** Wexler Real-Time is their new flagship feature, but it relies on plugging into a fragmented market of US court transcript feeds and heavily regulated UK authorized providers under CPR 39.9 [cite: 27]. Integrating these legacy systems is a massive time-sink for a lean startup team.
*   **The Pitch Angle:** "Kush — congrats on the $5.3M Seed and the launch of Wexler Real-Time. I read that dealing with the fragmented APIs of US real-time transcript feeds and UK CPR 39.9 providers is a barrier to onboarding new enterprise clients. I run a forward-deployed strike team that builds these exact unglamorous upstream integrations. I’ve built a middleware sidecar that standardizes legacy court-reporting XML/API feeds into a clean, low-latency JSON stream formatted specifically for your ingestion webhook. Here’s a sandbox demo."
*   **Logistical Delivery Mechanism:** An ephemeral, password-protected staging URL where Kush can drop sample XML files and watch the JSON stream convert and display in real-time.

**Rank 3: The Multilingual OCR / GDPR Anonymization Wrapper**
*   **The Logic:** The recent Seed funding is specifically earmarked to "scale multilingual, region-specific deployments" [cite: 9, 11]. Global law firms will demand rigorous data sovereignty and PII protection.
*   **The Pitch Angle:** "Kush — as you expand Wexler's deployments into non-English speaking regions, passing multilingual evidence through standard LLM APIs often triggers massive GDPR/ISO 27001 procurement roadblocks. Kaide Labs builds isolated integration sidecars that sit upstream of core products. I've built a localization sidecar that performs local multilingual OCR and PII masking *before* sending the payload to your core fact-bank, automatically de-anonymizing the output for the client."
*   **Logistical Delivery Mechanism:** A brief, high-resolution demonstration video securely sent via an expiring link, ensuring no sensitive data is transmitted or retained.

## 7. Red Flags / Gaps

While Kush Madlani and Wexler present an excellent target profile for Kaide Labs, several risk factors must be navigated during outreach and potential engagement.

*   **Hyper-Sensitivity to Security:** Wexler handles some of the most sensitive corporate data in the world (active litigation and internal investigations). They market themselves on being ISO 27001 and SOC 2 Type II compliant with user-specific encryption keys [cite: 9, 11, 37]. Pitching a "bolt-on sidecar" might trigger immediate security reflex objections. *Mitigation:* The outreach must heavily emphasize Kaide Labs' DMZ rule, explicitly stating that sidecars can be deployed within Wexler's own secure AWS perimeter as stateless microservices.
*   **The "Over-Extraction" Philosophy:** Madlani explicitly designed the system to over-extract facts by 10-15% to ensure absolute thoroughness [cite: 7]. If pitching an upstream tool that filters or summarizes text (Angle 1), it is vital to assure him that the sidecar only removes true noise (e.g., formatting metadata, standard court headers) and does not perform semantic summarization that could accidentally discard a critical case fact.
*   **Team Maturity vs. FDE Need:** Wexler recently raised over $5M and is actively expanding its engineering team [cite: 9, 11, 38]. While they fit the "post-seed" profile, they may feel they have the capital to simply hire full-time engineers rather than contract an FDE. *Mitigation:* Frame the £10k/month productized sprint as a way to unblock an immediate enterprise deal *this week*, bridging the gap while they spend the next 60-90 days recruiting, hiring, and onboarding a full-time engineer.



**Sources:**
1. [highperformr.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpqbKXSRfMPgE_1NhABap7L1avqBbyI7GArv8O3IxBvEE8JPsBAhwnmadOhWN7201P0dphE00qE3BTLK9c9y5LaOXa8cTUyVmx4AQfvlRzCx6upr64vNruNlhMVtKee8biR3hcQAlIZKZFOWZuIA==)
2. [prnewswire.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2xs9TKNogpuvjIdkf9mHOYQGbTmIqqIGZg2d-VtX1IQFFJBP-qzDFouiTWNWhZbrYat9lhCC6Cmld1j1wtj8AX67UkDsP8MDpuCbpvzRKgXFKJTWDTBfEDX6ISoXLeMU40GFzUQjoowgKUy8IdTMYwwxrsSFpS4tLgvnoRNhZTFt79IyU29LvAFa-81euXgGfnNQT3MBDprp3iflzA4zLVwsM2-XHemmem-_y0VIMSkJnAXAMph8Oq2MYaiiyTpjTfabgFUZIofwm4yBMmmW5XRNuETaltOZneseJN7K3V6i31TtZVHxmCIUJgg==)
3. [wexler.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF5ni66yIkVoxMku-2AC30H34OFcty9-DfvDCgVWrVjPlBNvw7ZPxofbk9BBhHgqBNfBPPbWOj7nW0QZCo_tgrBYF_lITwitK0cflN4JkC7IaJDlONT273wgzcUqAqDd_wdINN-buK_S9SZNWm_kqSA2Sk3UAlTIchmdQWFManbHrb4YfAn8SAZ7sZMoM086m8S_ZRaUNS_-Kc6bM6W)
4. [cam.ac.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlUxR3eqTJgb1RBA4zTDAWtnvrvuZJmOutir0MX8fmfAVZLXkLkqxwiCvh4vnNqxodhcIK0P5VywKKhHU1tGE2QwJfLfXJNzd2dbiFtQiNn-7HZKj2xf85jagrFDKt4vFEJoPwX7o-_Qsv6TjAU1VDjWTwE7pBOX_2BMbTBM-ZHtXUeQ==)
5. [prospeo.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHR8LrQAq0EeMTO4JXk_NGqc4IcN1wzNsA_scyE1oLYgVsHFesIU1hebsDt-I0Vn6m6ZbZKqMMMk9O64w6-n8YByxvOhKGJlklThZyhUGNKBTk=)
6. [geeklawblog.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHdxfWBqRtZAdQFqJ_OSI_-0NLr3XAMWEpOuH0RXAkAlKGTHJfEgthIoEnb0EwRTSHgEHnmU3Dkr5xuNaw00h_skiuAb7yD-U-0VfGLTIUTBtBssI8aV6fod9hSyanPvy3b7nTALhA2dZPgnKmxFs8K5XRK0JU8e5X0dXGz4rbD3zHgvSZmBMeBd0y57ac4b58UZwXD7vKpBPC6UHPGV2ou4EA9MDxHmvNdTuQgZ4aA0drwSdtlaqBB3k_jIWooSYGP)
7. [legalbusiness.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGuKmF-lhxaQlBTkHCqLBbCXGko96ynwzlUsJEIzDIxHgLyUQ8mtsR0O7CdzHH-mU-dq4Ulk_HxeCWLwuYFQByjhouR1drwvpflp0cREUX0CIo455-I9ZZtH1OuBFNTna_o6_jrFtIXUoK9moiUqKLkNTlXUYrfCwfRYA_i2x--tw6Rrz_Oo5U_WPmGZe7bhrRAOR3CjGlAesUnMprRMtNXKcmC3RaBhhddLX14nhM4lHSeszDINr2brScSLmGSp8E-WVQ=)
8. [preqin.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH4oKwSlmE9TnZkEzI8QFsZZr9rS3oJiabKdArWZDtZ6fbaUNqzhPb7BYzcTTXkAMqgdT-mBRNWy6eYT4zPYyxu42qmI9OnLv4Daom6d1lVez6LenGw0VAXTlZ4W_g4Xk0NOW9c2PpbMTSS-WP-vWXt)
9. [seedcamp.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEjWnbjSxKYI20LZ46OuJApWWiS3LpIbS8-Oe7fmWkg4HVNiruo6botNzhUPTY9kCPwvJtWd7NzTV09WcLghIjOGLaOJbDpBeY9tXREPiq4kHbXiZLAAaCP0TbxuVvyWUH8rEpnmcegxCDEXkryoUOiSib9Px3ZBb5bC0wB6NaydPqoxsY=)
10. [nonbillable.co.uk](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGIN56xyFndH7Z0UD1Hz9OQLCdWfXbdTB5dyMKehShrtSf3_HoFXv7mKPE-7RWx4DcFiIZosKonKcjPeD1saKUlpJouLgGdrLYtLWg3V6iKnAOmJlQ7uWDlQSjSrvcMN7iUQmNNFWZk3dLS)
11. [wexler.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGy7zchW9WXSdbThmMD1eTyQqSYH3YAohOHqLqz6eu4HGVVNTUQpe7tq7QLVOHJlURiFZSh6y7j7rt6Ib3SVP_K8R1vYztN5WmcxLJTfIkDeMMWN47sdOdHpGhS3aNZjkG-DzAf11Bj16eAGl7_kws1XbracWYyQ2DbtDkz5T6yFr-dA3uQhnROfd0DQ8p60ErBjveHs6USIVxM453ZFFWGWrga5XWSWbyjKiTTI_ljUYN1U5fY4K6t1c4T1ghYPlWA-mnNvKrHIg==)
12. [tracxn.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFayeRYagyqFmwFGeX7lOA0iXydLN7RpSqZFzTvmiA7cBK95iyFz6OUeIIpyFZU1ARFjsl2D2RRjyE2Hyt3K9RxpGvx9DRu7m190qITC_E7byr-Z89zUY78kmg6gQpSEyhBPpMmTuBJHaUmMORbH1wyTxWgtWdkgwRRX9oVuRqcxvU-IBQeeIL9mE2tfJ24Oo6p7HMBDJ0l6RtzZQn7KW7Uu7QIyA==)
13. [tracxn.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQER3q_SbWZeRD8XB_1dZms1fcU0ePM-DwIxSw8U0YJe0_jiYmn4Sq9lgeC5I_iug_8HnLmGC-Sfuh6xqzCP-LKRRnKchNinA4Qk5o1WYGIDPVFG0ilQoHgUr1jswapkHylniEGTr7AvaBr1ICyGAxJFyDcWTro87L_hp_jgo896n-_odDwrrOqmVQ==)
14. [startuphub.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFYFTr80JnvBn8UPd-b75EwEvu7JPh1HkcUY2EK6Rx44QA1ZYfwVIEMovbN_8SHPWM9VEL0jlT885KxJhfazqwrIh_OUItJIYmIoGVCXU8fbt8m8qjeQesva-2uc3Ey7_F2vPZIwzPL1Eyk9cHexsotBghx3ALqhIGzZLP_Sc69FR7LIE4UR7K-zGKVkd2rVafgcXxpUyRQjy10G-v54CQoW_yX6E36-_8=)
15. [artificiallawyer.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFLQLSHBJSvvhynvkZaZL31p8kL8hB5RWoFGYAsrKq6FI-82JgmHuil8dJex4xUS8jCHacW6pPT1tnBUzeX4kEYpW0-0tc6mHCIh41I_hTrLsKZtYabhFPs3eTNu--sV-lJDarcH7bBjL0jNgot9_bvNDaeWc0pPI5lxUjbN46N6gMdor2VCbOEh8oRqDS8v9ulI-aSGg==)
16. [echopointglobal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHL-m8x5FTNEmHYr8PBNjJeYVMntuCB__sz5VD0GRYO5k2AmzJisLex1DVbsBJ9KI2AiCcVYxvdl_odX_RoH03db3gbmYbDTMxAOw3Yc2Q0qzS8_Sqsm9u15C8_jvOO0Zj0lN87wQsV2qtRdDwdZMTPI_SFrZW-S8dvjNAvWNmfqclCMYFc7bPpop9wJ4e6M2B7oywA7zYSb6RP2WRZHnE=)
17. [prnewswire.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH-seXytE3rnBJgEx2QN2rSXPy75GoZ3kYzWSnrOWgwEBusv3z4undxSFdz5_K6BL1zwD8euAYFlvopxOMA4igMFVzvfPJ1bzGPIrBFfeQca11n8HqGKx2sJKFNAQCCHqqtTH_QOM1iwBhEuuun3aTiVHezNv9RWMUXHK1zrkp_QW6c8nRbmjs9K8J1Nu7K9vHFhoRViB1H2KZeNq6Qb3iEjQ-T6HAKaDTWcwX-fjSepIRA_dkDWw8rBzXj1p7vkXTz0w_c1ft7LdvQ-Y3u2EfYaMN77U5VsuSdAn5g2enmUA==)
18. [pulse2.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEAuDGhRytYHINxkCIMWog25MOBsLWOuf3MtirWNk5uC70ycXmebLlF49w29DbEHhsbuiXaOk1BbsmEG5zuLWzmPzoWdGuoOkskYb_Wn3CRV8eJLwxzag7Dn99MXRiEApJo3aB2HnB6UpstzdhgOycXYAHwNJA-7MOt8-jMTHpBXp4p04rZuyiHUZUvdev-oXE=)
19. [cloudnine.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG3aHN98L-3t6MY9Iee3zVIHd_YHHDT5PHAr_PYVca6Uhw96ENF0404TXaDDb5aS0x-YhAjSmLia22xl6E_y4gwB0kBvnXH5Enz2luUPaIyWiwYmzMBhwnaiD4OGTDbLi4arj5DnVLyzWX094vyH54iefZDMvFEjOXvQ4WbqEb149dbk3b222D8O77Htqpr5llP9nFpzqeqGacuyI4=)
20. [logikcull.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEZUbxybFYmkGFs83jXFibZcZBrkG-nFKqY2WVPLwxym3n89ITV3zQilXyKyheE7Oc7UTdIVlm7Q9btSVtU2CaQQdaI8cCpvCTkwiUwgMncNBi1w0hF5GFhOIlcxf9EexqisCzFMccB5sLm7Brd2pLTYKqQHVf0l-sqRXTfHQ==)
21. [v7labs.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFjZpLhCSMtEg2yWSuGu1pzcrcAwlKiXl3CZIQE9vHqkQamLmfbXpGBg9MQxS-GpHQnCqv-kZN4xJxkCbJB-VCTAtnWaHCPRzTFk2v0obtc-UW-HUCybyEtkd-Pq3DphTsDkdZk4Y5iHyX_)
22. [ktlitsmart.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGAjajT3ydHg0dGy6xN_VnNDZRWbQ8iM4xNGipBAgz2aaV2-b9ZneAThf3wL3FYuPNChdqN0RjJ9b4PgqO6XruBILlNI1HcFlSCsiKezabuiAB61J8OwI4852av1s0_a32uiGJLJZRZ7aiNFfON83L2PDWHgpUZepqaLbuqXabX2Vj9MCSIcruHNfMfFTdJ8FH4EIXzU9XFzkJ-239nVS-K6SsNOFt8fQV8j6YJoj5OO0E=)
23. [digitalwarroom.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHbcuQtKbhvwQH4xFphDpvWLoxh9gIuYbTiXlES6029TBYzp-iy1n4d-2Ct_NnBFC6vCmkL0yHu1jU6Y5wW5w16kAtAt9H_a3RBaxL3DVZAvPUhKNmnUIGj30aWTt_ZARzFTGo4qEeR-OiNr06oI-RsLpi8IbYISGSIgVTJeqsLcyMEdlAdjirvmQWJzGL1zvpmWdonu4xEehQ=)
24. [legaltech-talk.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEIC872QhpigW8GwVy9xxOXCIGLfHaHYUarom9RyYMx3oZWhsyNXdjYiSF5J2-HAsTPAZKvlh76ZGaf2YeFbA0WOMxP63flifhKXp8wY-1R2UO0lchtZRujxuevlKlnSI-XpHkdeQbdistOeS0v1eFHBH5xe59iQff_fk_abK3-gSluUAxxcpfEqxaIecqnSzJbiNi-jkpPFcjH1MGU4RRQiWXIy6ZO-l9kMaAHC11ie42TSyG6Jxl9x4IpPhQdEOBQwamHAsN1o14=)
25. [ashbyhq.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2xrvmnTTZ5tIH9DEn91JmtoTcXKPGNADXPpg-RTQ-97ZAGkfVAhMuTv3BrWe4zAKezL9KjVTJg24xnmFY3-Q17gH1CEqfctKkBq4OYYhjBdYzWC3wy6CMYj06tS4nw0QS7ylcna_uJdokpDCj45_KgWpCpFHTm66-WA4=)
26. [joinef.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoPqHA-njKwnqSCBrhMCmC5YXAHh7zKkVz4um96gM97UjPs8Ljnt8EkpJPObUBU3UpBW64oSozKBrQYjQka2Pxo2r4ldS1KSGo8KsSy9COYTfzrjGeud3TZHuoFsFEOgw6ClDF9yTUbvcjbX3mz88vYao7CBpZVTrtmvyFuBqP2YxmUskzSjLmESGQ3JOYZBxRb2Rfh5tSh7I2HeCpdPoJ2D6TrnJgd1DZEEI=)
27. [wexler.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKuwMCWCIVnuEmMIfw3N66wLyseUX0wF4P84d9M5bybmxBr4I83_ukGAjRqdBeo5aRUg-vELGVVqZA_fg1n_Q0oogXSecqi147Konw2TngIMnY7QwDa6pcICW2DPt1I1ScI535-Ro2adzE0pM6xbql4vDCJ8zKQx-xhH1wN4CQcD7RaGGTADPsKgD4HGqriCEveE-mEK5x)
28. [speechmatics.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHgbGiasdsa31AxBApQYDuBgMUJb5NAyqtczNF1JQN_xjCarrrfqFM8iq-Esvj6YnY-MaY3zZQqzl_cO4OFrMb-cwLeD_zPvQSU0OZS_McV9KVFGDp7-kQ_uu-cRtpGR8jwTBfkbai_JugibdhR2GpP)
29. [picovoice.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHK9tbr1XjfsSUEPAlal3o7v7C_fp7wTBlJlunsH38RVhwTxiuv6famSvHN7WJkwVPcTGso3g_xYg0WDtryNRHOu7T-yYcWQX3WRdVWpiMwZa9csuEOqN-wR6GwqZc_0rf947BMVWNiUuhuBTpvcwhdyuvk4csBFbSXTf0=)
30. [gladia.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBuNLR0YeY7rb9WlJZzDhSNx5hg4Yvz741HJmup5cR91dvN4LAREI_4YL_XwpuHb4gu_7wHzok1iIjLBhpAH7ehgpCUNj4iR1t4JNUu66JDSJXcZRmGL5YG4Bbig5-vn-6uqN3iqWMPyo=)
31. [promwad.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEBL3MRlHVBq3VQSKM1pqdgKMw4c1rd2bFcO0O1RVohNBeVyusIrKESp43r3jyTpwg92UkmJRneyOhaTkjdD80p4thz9JQKYQFlqpPzyn4_squUXWw7OessWud7zVh62texHnOrle2jc3xGXbUsYOBmt_kdd7Cns0eNWjXr)
32. [artificiallawyer.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFEsdMlfzJ7hiIqLViLlS8tvzhPEPLIndsMh9jy_zopJHHzils4jaxEtYBOENdmwcC0xJsTwcj--Om8TO5MjCylNMILiZgARc6_6Erf7rPYzZWQz1Vou8f1iPEdU9W9cmULuzX4l8YoPIBb3Zwytm2UHF9Q_qaIXCoPFsNu33X79wQzMddKm2CPd50-azFcQAfpPeETQg0f67GezQ==)
33. [elifesciences.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFOmyXsODfkaQnVpxev6tK295XkEBo49dIc0BUqrxmRUnf92UWHg5Mt_768UhxrpDaIgYUGQLkyaSIT72JZ6fTk0844VUcPMc_4rcLK_VmQq6nDqG5CiTfgXjwhed3LMGyxtLQ=)
34. [nycourts.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGNAYFf1_qy8VQ4N1XkOrW4VZ_t2fZY6gLGDy_tJwSKbTeAGP6LO8OguhIxvt0ixj-saamI900DKu1BeQgE3asL_bV-wWhITfM6ficaItSbPd3ze1hmQ_iiXNXnCIJunBvbq5120pRjM3IaptPXGOWYnE7TtzXZMypZnp5SDAJlmj4mZMbCs3hQaJeQ)
35. [nih.gov](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUWYhGo2KXU4zpzCJuxgLNcGS6xTsBI3GvPuYbILYSAHUydRIHNEJg0VjSTZAbNBnebhG9qG5kxAbf3zgpC-s3RTyL9_jJpB_3z-wLr9WXnk5hiKVCJjJzw1T3CH6c5cLDy2iyQ3LswQ==)
36. [openreview.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwMbpqU8iikqE3ozFPpXbBsxww25EuFx5_sNMIO6tV5w44c561wzjB8VZ_mIaSTkjBz_zVwBhJexClgK2pcjOoFVEBj_BR5dVNdut-Obd0wY6RMABZOaYY0S0WYbi3)
37. [wexler.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGjYGfqOfUPCE8IiP-4JI95NK76_m0a5xkJQLfHAbZHhELzY7ZogjIHgAzTqNFMKEf-9FNDJ4-EBrHvc9EUUCiglHpY7Yip_n4qtElC)
38. [seedcamp.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHyZHYqTXMTezUsMyVy50KYDXBfTkm6KH1LslVBhm4NmagoaQnTZ2_MS5Fh1xjKNoZIvMAyLoChYrMBIKkA8rFZeI4Lm6rbt17z-p3zTv26dkXXGHkGwtGExrZSclaEBla_sarYyJnhYDGu0vrBS_7Dzsl3Zet-TA1qQYwY0Ru0r9Lt3RgVWSgc367KXPOWR_IGwBpt4fJxxfSaep3JdRv2WfNl_6XlMa2rXv4Lq8Gkbe64)


