# Founder Dossier: James He (Artificial Societies)

**Disclaimer:** This document is for informational purposes only and does not constitute legal, ethical, or professional regulatory advice. Given the nature of scraping human psychological profiles, simulating public policy, and processing confidential Fortune 100 strategy data (such as the Teneo engagement), all data handling and outreach strategies must rigorously adhere to GDPR compliance, data privacy laws, and strict ethical boundaries regarding the simulation of synthetic human populations.

## Executive Summary

*   **Founder Background:** James He is a Cambridge-educated computational behavioral scientist who historically declined early funding and PhD offers to prioritize building machine learning systems before launching his own highly academic venture.
*   **Company Snapshot:** Artificial Societies is a YC-backed startup offering generative AI market research via simulated networks, recently raising $5.35M but facing intense operational competition from workflow-embedded platforms like Ditto.
*   **Stated Pain Points and Bottlenecks:** The company suffers from acute frontend development constraints, lacking in-house design leadership and public APIs, which actively harms user experience and delays enterprise scaling.
*   **Technical Decisions and Preferences:** The platform relies on complex, multi-agent LLM simulations to model social graphs, an architecture that requires up to two minutes to run and therefore necessitates careful asynchronous queueing for external integrations.
*   **Enterprise Integration Surface:** Kaide Labs can build bolt-on Figma plugins, data ingestion pipelines, or white-labeled reporting dashboards that securely feed data into and out of the AI engine without touching their core proprietary multi-agent code.
*   **Recommended Outreach Angle:** The highest-converting cold pitch directly leverages their public vulnerability against their primary competitor (Ditto) by offering to build a Figma plugin sidecar in a one-week sprint for £10k/month to match Ditto's design-tool workflow dominance.
*   **Red Flags / Gaps:** Potential friction points include He's strong ideological resistance to defense use cases, the un-audited nature of their internal accuracy claims, and the technical risk that their backend is not yet modular enough to expose stable staging APIs.

The following comprehensive dossier provides a strategic overview of James He, Founder and CEO of Artificial Societies. This report is tailored specifically for Kaide Labs, synthesizing the founder's background, current business trajectory, technical stack, and enterprise bottlenecks to inform a hyper-personalized, forward-deployed engineering (FDE) cold outreach campaign. 

*   **Exceptional Intellectual Pedigree:** James He is a highly driven computational social scientist who declined a $600k seed investment at age 16 to study at Cambridge, later turning down a PhD to build machine learning systems for a fintech startup before founding Artificial Societies. 
*   **Rapid Enterprise Scaling:** Artificial Societies (YC W25) recently secured $5.35M in seed funding and is transitioning from bespoke consulting engagements to an enterprise SaaS model, serving Fortune 100 clients.
*   **Clear Integration Bottlenecks:** The company boasts a world-class core simulation engine but suffers from a lack of standard enterprise integrations, public APIs, and design tool plugins—areas where their primary competitor, Ditto, is currently winning.
*   **Kaide Labs Alignment:** The startup's small team size (six employees), massive enterprise client demands, and open "Founding Designer" role present an ideal surface area for a Kaide Labs sidecar to build enterprise wrappers without touching the core intellectual property.

This dossier translates James He’s public footprint, academic history, and technical philosophy into actionable leverage points. By mapping the competitive landscape and Artificial Societies’ specific go-to-market friction, this document structures three highly specific, artifact-driven outreach angles designed to convert.

## 1. Founder Background

To successfully pitch James He, one must understand his unorthodox trajectory. He is not a traditional software engineer; he is a computational behavioral scientist who utilizes code as a mechanism to understand human societal dynamics. 

### Academic and Early Career Trajectory
James He’s background is characterized by high-agency decision-making and a consistent prioritization of intellectual curiosity over immediate financial capitalization. At the age of 16, he was offered a $600,000 investment for an ed-tech startup but declined the capital to attend the University of Cambridge [cite: 1]. At Cambridge, he read Psychological and Behavioural Sciences at Selwyn College, graduating with First Class Honours and a Distinction on his dissertation [cite: 2]. His academic focus centered on the intersection of data science, evolution, personality psychology, and social dynamics [cite: 2]. 

Following his undergraduate studies, He was offered a fully funded Natural Language Processing (NLP) PhD Studentship at Cambridge [cite: 3]. In a highly characteristic move, he turned down the PhD to enter industry, joining Yonder—a UK credit card startup—as their first and sole Data Scientist [cite: 2, 3]. During his two years at Yonder, he built the entirety of their lending machine learning systems [cite: 1]. He maintained a bridge to academia by reserving 20% of his capacity for social scientific research, co-authoring papers on topics ranging from Twitter climate discourse to adaptive sampling algorithms for drug trials [cite: 3, 4].

### The Genesis of Artificial Societies
The conceptual foundation for Artificial Societies was laid during He's spare time while employed at Yonder. He authored the first large-scale academic study on artificial intelligence societies, specifically observing how 33,000 AI chatbots interact, which was subsequently published in the *British Journal of Psychology* [cite: 1, 2]. The transition from academic theory to commercial product occurred rapidly. In early 2024, He utilized a simulation to recreate a market research experiment that his future co-founder, Patrick Sharpe (an applied behavioral scientist), had spent two months executing; the AI completed it in ten minutes [cite: 1]. He formally departed Yonder in December 2024, securing a position in Y Combinator's Winter 2025 batch [cite: 5].

### Psychological Profile and Personal Quirks
He’s personal writings reveal a founder who is deeply philosophical, intensely driven, and aesthetically minded. He rejects the standard "heroic" startup founder narrative, instead framing his ambition around "self-sovereignty" and making an irreplaceable contribution to the world [cite: 6]. 

Several key personal attributes provide excellent material for hyper-personalized rapport-building:
*   **Interdisciplinary Philanthropy:** Upon receiving his first paycheck from Yonder, a 21-year-old He pledged 10% of his disposable income to establish the James K. He Scholarship at Cambridge to fund interdisciplinary undergraduate research [cite: 2].
*   **Classical and Traditional Arts:** He plays the Guqin (a traditional Chinese instrument), posting experimental covers of modern pop culture and classical music—including *Game of Thrones*, Mahler's Symphony No. 5, and Shostakovich—on his Instagram [cite: 6]. He is also a practitioner of Tai Chi, drawing on its philosophies (e.g., focusing on one's "own centre-of-weight" rather than the opponent) during the grueling venture capital fundraising process [cite: 5].
*   **Physical Routines:** He captained a rowing boat at Cambridge, was the president of the table tennis society, and is an avid road cyclist who completes 100km+ rides [cite: 6]. He values daily morning runs and weekly cycling to anchor himself in a physical rhythm [cite: 6].

Understanding this profile is critical: James He is driven by the mission of creating a "Societal World Model" to end the era of policymakers and enterprises taking "blind bets" on human consequences. Grounding this grand vision of a "Societal World Model" requires massive operational constraints: it necessitates immense concurrent compute requirements to process millions of interacting agents, rigorous data freshness dependencies (pulling real-time social media data to prevent the model from reflecting outdated cultural zeitgeists), and robust ethical firewalls to ensure simulations do not inadvertently generate or ingest harmful societal biases.

## 2. Company Snapshot

Artificial Societies is positioned at the intersection of generative AI, market research, and behavioral modeling. The company is transitioning from a highly specialized, founder-led consulting tool into a scalable enterprise SaaS platform.

### Market Positioning and Product Offering
The core premise of Artificial Societies is the replacement of traditional, slow, and expensive human focus groups with networks of interacting AI personas. Unlike standard survey tools, Artificial Societies maps personas onto an interactive social network graph, allowing the AI agents to influence one another, thereby simulating virality, echo chambers, and public sentiment shifts [cite: 7, 8]. 

The company's flagship enterprise offering is called **Radiant**. Radiant allows marketing and strategic communications teams to build bespoke AI simulations of high-value, difficult-to-reach audiences—such as Fortune 100 investors, specialized buyer committees, and Washington D.C. policymakers [cite: 1, 9]. The platform boasts a database of over 2.5 million AI personas grounded in real-world demographic and psychographic data (often ingested via social listening tools like Pulsar) [cite: 1, 10].

### Commercial Traction and Capitalization
Despite being founded in late 2024, the company has achieved remarkable early traction. 
*   **Funding:** The company raised a total of $5.35 million across pre-seed and seed rounds. The $3.35M seed round was led by Point72 Ventures, with participation from angels associated with Google DeepMind, Sequoia Scout, and Strava [cite: 11, 12].
*   **Enterprise Adoption:** The platform has already delivered over 18 million simulated responses to global Fortune 100 enterprises [cite: 1]. A flagship public case study involves the strategic communications consultancy Teneo, which utilized the platform to simulate 180,000+ human perspectives to test a confidential technology strategy for a major US company [cite: 9, 10].
*   **Team Composition:** The company currently operates with a lean team of roughly six individuals split between London and San Francisco. Key personnel include James He (CEO), Patrick Sharpe (CPO), and Tom Whittle (Founding Engineer and CTO) [cite: 1, 10, 11]. 
*   **Product Pricing Logic:** While the self-serve platform operates at an aggressive price point of $40/month for unlimited simulations, the Radiant enterprise product requires a customized Statement of Work [cite: 7, 13, 14]. Given the stated impact of shaping "$100 million dollars’ worth of decisions" [cite: 1] and competitors like Ditto commanding $50,000 to $75,000 annually [cite: 7], Radiant’s customized engagements likely carry a $50k+ to $250k+ Annual Contract Value (ACV) [cite: 1, 7, 14].

### The Competitive Landscape
Artificial Societies is operating in a rapidly crowding market of "synthetic research" platforms, and its primary rival is a company called **Ditto**. The philosophical divide between the two defines the market: Artificial Societies models the *crowd* (social graph simulation), while Ditto models the *individual* (isolated, census-grounded demographic polling) [cite: 7]. 

To clearly outline this gap, the following table summarizes the operational and technical divergence between the two platforms:

| Feature / Specification | Artificial Societies | Ditto (Primary Competitor) |
| :--- | :--- | :--- |
| **Core Methodology** | Networks of personas modeling crowd social graph dynamics (virality, echo chambers) [cite: 7]. | Isolated, individual population-grounded personas built breadth-first [cite: 7, 15]. |
| **Base Pricing** | Free tier (3 credits); Pro tier at $40/month; Enterprise 'Radiant' (custom) [cite: 7, 13]. | Enterprise pricing typically ranging from $50,000 to $75,000 per year [cite: 7]. |
| **Panel Size & Sourcing** | 500k to 2.5 million AI personas, primarily sourced from social media behaviors [cite: 1, 16]. | 300,000+ personas grounded in census, demographic, and psychographic data [cite: 15, 16, 17]. |
| **Integration Capabilities** | No design tool integrations publicly available [cite: 16]. | Native design tool integrations with Figma, Canva, and Framer [cite: 7, 16]. |
| **API Availability** | No public API documented [cite: 16]. | Full REST API, including a native Claude Code integration for developers [cite: 16, 18]. |
| **Validation/Audit Status** | Self-reported 95% human self-replication accuracy based on IC2S2 2024 academic methodology [cite: 7]. | 92% overlap with traditional focus groups, independently audited by EY across 50+ studies [cite: 7, 15, 17]. |
| **Geographic Coverage** | Global (contingent upon available public social media data) [cite: 7]. | 50+ countries with state-level filtering available for US markets [cite: 7, 17]. |

While Artificial Societies possesses a highly sophisticated academic backing, Ditto currently dominates the enterprise software integration space. Ditto boasts native integrations with major design tools like Figma, Canva, and Framer, allowing product teams to run synthetic feedback directly within their workflows [cite: 16]. Furthermore, Ditto offers a full REST API (Representational State Transfer Application Programming Interface, a standard architecture allowing different software systems to communicate over the internet), whereas Artificial Societies currently has no documented public API or design tool integrations [cite: 16]. This specific feature gap is Artificial Societies' most vulnerable flank.

## 3. Stated Pain Points and Bottlenecks

A hyper-personalized FDE pitch must anchor onto public, undeniable bottlenecks. An analysis of James He’s public statements, Hacker News (HN) interactions, and the company’s hiring pages reveals three distinct friction points.

### Bottleneck A: The Frontend and UX Design Deficit
Artificial Societies is currently constrained by its lack of in-house design leadership. The company is actively recruiting for a "Founding Designer" in London, offering £100k–£150k to someone who can "own our product design end-to-end" [query]. 

This gap actively causes public friction. During the company's Y Combinator "Launch HN" post on Hacker News, a user pointed out functional issues with the website. James He replied: *"so sorry about this! fixing it now. we simulated how our content would land, but alas couldn't test the site before it was built :`)"* [query]. This self-deprecating admission perfectly illustrates the pain point of a highly technical, backend-heavy founding team that lacks the front-end engineering and design velocity to match their core AI engine.

### Bottleneck B: The API and Enterprise Integration Gap
As highlighted by industry analysts, Artificial Societies is losing the "workflow" battle to competitors. Startups like Ditto have gained massive traction by embedding synthetic users directly into software that enterprises already use, such as Figma [cite: 16, 19]. 

Artificial Societies requires a user to enter their proprietary dashboard to run simulations [cite: 8]. They currently lack a public API, meaning enterprise clients cannot programmatically trigger simulations from their own Customer Relationship Management (CRM) tools or internal data pipelines [cite: 16]. To scale their Teneo success story, they must allow consulting firms to white-label or integrate the simulation engine seamlessly into existing corporate tech stacks. Building these REST APIs and middleware wrappers takes time away from optimizing their core Large Language Model (LLM) graph engine.

### Bottleneck C: The Validation and Audit Burden
The enterprise market demands objective proof that synthetic personas are accurate. Artificial Societies claims a 95% accuracy rate based on He's academic methodologies [cite: 7]. However, market analysts explicitly call out that this is self-reported, comparing it unfavorably to Ditto, which utilized the global accounting firm EY to independently audit and verify their 92% correlation to human focus groups [cite: 7, 17]. 

While Kaide Labs cannot provide a Big Four accounting audit, this pressure indicates that Artificial Societies must constantly prove its value via highly polished, customized enterprise dashboards that clearly map simulation results to real-world return on investment (ROI) for specific clients.

## 4. Technical Decisions and Preferences

A successful FDE embedded sidecar must harmonize with the target's existing technical ecosystem and methodologies.

### The Stack and Infrastructure
*   **LLM Agent Framework:** Artificial Societies relies heavily on multi-agent architectures to run its simulations. They utilize GPT-4 and the LangChain framework to govern the interactions between their AI personas [cite: 20]. 
*   **Frontend/Scripting:** CTO Tom Whittle’s public GitHub repositories indicate a strong preference for TypeScript and JavaScript ecosystems [cite: 21]. It is highly probable that their core dashboard and web application are built on a modern JavaScript framework (e.g., React or Next.js).
*   **Performance Metrics:** Their simulations require heavy parallel processing. He notes that multi-agent simulations of personas reacting and interacting take between "30s to 2 minutes to run" [query].

### Architectural Philosophy
James He explicitly differentiates his platform from simple LLM wrappers. The platform's architecture is a "Social Graph Simulation" rather than individual persona querying. This requires a three-part understanding: 
**1. Core Definition:** Unlike static polling, it models how opinions propagate through a network of interacting AI nodes over time, capturing echo chambers, virality, and cascade effects [cite: 7, 8]. 
**2. Analogy:** Think of it as a digital ant farm—instead of asking a single isolated ant how it feels about a piece of food, the system drops the food into the colony and observes the cascading behavioral reactions of the entire swarm. 
**3. Relevance to Kaide Labs:** Because the value lies in the dynamic *interaction* of the swarm, the core engine is computationally heavy and delicate; Kaide Labs must strictly build pipes to deliver the 'food' (inputs) and cameras to watch the 'farm' (dashboards), without ever touching the ants themselves. They construct networks where agents read, react to, and reshare content based on behavioral heuristics, forming "echo chambers, cascades of reposts, or shifts in public opinion" [cite: 7, 8].

### Concurrency and Asynchronous Queueing Architecture
With multi-agent simulations taking "30s to 2 minutes to run," the next logical question arises: *If the core engine requires up to 2 minutes per run, how does a proposed API sidecar handle the compute latency and concurrency limits if a Fortune 100 client pings it 1,000 times an hour?*
To bypass this latency bottleneck, any Kaide Labs sidecar must implement an asynchronous queueing architecture (such as an AWS SQS or Redis-based task queue). When an enterprise designer triggers a simulation via a Figma plugin, the sidecar immediately returns a "Simulation Processing" state, offloads the request to the queue, and uses WebSockets or long-polling to push the sentiment scores back to the UI once the backend AI engine completes the 2-minute computation. This prevents the API from timing out and protects the core LangChain engine from being overwhelmed by simultaneous requests.

**Kaide Labs Rule of Engagement (The DMZ):** Because the social graph engine and the LangChain multi-agent interaction prompts are Artificial Societies' core intellectual property, Kaide Labs must *never* propose touching this engine. Instead, the focus must be entirely on the data flowing *into* the engine (data ingestion APIs) and the data flowing *out* of the engine (enterprise reporting dashboards and integrations).





## 5. Enterprise Integration Surface (KAIDE LABS-SPECIFIC)

Kaide Labs operates under a strict "DMZ rule"—solving specific integration bottlenecks upstream or alongside the core product. For Artificial Societies, the path to closing more Fortune 100 deals (like the Teneo engagement) lies in removing the friction of deploying their sophisticated simulation engine into archaic corporate environments.

Here are the specific, actionable integration surfaces Kaide Labs can target:

### Surface 1: The "Design-to-Simulation" Middleware
**The Problem:** Competitor Ditto allows users to test Figma prototypes instantly. Artificial Societies requires users to manually extract messaging or visuals and input them into the Societies dashboard.
**The Sidecar Solution:** A bespoke Figma or Canva plugin that interfaces with Artificial Societies' internal endpoints. This sidecar would allow a designer at an enterprise client to highlight a frame in Figma, click a button, and automatically send that visual to the Artificial Societies engine for a 2-minute audience simulation, pulling the sentiment scores back directly into the Figma interface. 

### Surface 2: The Enterprise Audience Ingestion Pipeline
**The Problem:** To build the 5,000 AI personas for the Teneo project, Artificial Societies had to rely on demographic data "informed by social listening and deep qualitative research" [cite: 9]. Partnering with tools like Pulsar [cite: 10] requires heavy data engineering (e.g., an estimated 40+ hours of manual data wrangling and transformation per client) to transform raw social listening data into structured persona attributes for the LangChain engine.
**The Sidecar Solution:** A dedicated data-ingestion pipeline sidecar. Kaide Labs can build an integration layer that automatically pulls data from standard enterprise social listening tools (Meltwater, Brandwatch, or client CRMs), sanitizes the data, formats it into the specific JSON/YAML (JavaScript Object Notation / YAML Ain't Markup Language, standard lightweight formats for storing and transporting data) structures required by Artificial Societies' persona generator, and updates the AI graph dynamically. 

### Surface 3: White-Labeled Consulting Dashboards
**The Problem:** Management consultancies like Teneo are highly protective of their brand. Delivering Artificial Societies' insights via a standard startup dashboard is less appealing than a seamlessly integrated, white-labeled reporting suite. Furthermore, the founding team is currently lacking a Founding Designer to polish these interfaces.
**The Sidecar Solution:** A standalone, white-labeled reporting sidecar. When the Artificial Societies engine finishes a simulation, it dumps the raw JSON payload to this sidecar. The sidecar generates highly polished, Teneo-branded interactive web reports featuring sentiment analysis, network graph visualizations, and verbatim export capabilities. This removes the UI/UX (User Interface and User Experience, encompassing the visual layout and user journey of a product) burden from Tom Whittle and James He, allowing them to focus entirely on the backend AI heuristics.

## 6. Recommended Outreach Angle (3 angles, ranked)

The cold pitch must act as a delivery mechanism for a custom-built artifact demonstrating immediate FDE value. The following angles are ranked by their likelihood to cut through the noise, leveraging James He’s stated public bottlenecks.

### Rank 1: The "Figma/Competitor Parity" Angle (Highest Probability of Conversion)
This angle directly attacks the public vulnerability highlighted by industry analysts (the lack of design integrations compared to Ditto) and provides a tangible, immediate fix without touching their core codebase.

*   **The Hook:** Reference the specific industry critique comparing Artificial Societies to Ditto. Acknowledge that while his Cambridge-backed social graph methodology is vastly superior to Ditto's basic demographic polling, Ditto is winning enterprise deals purely because they have a Figma integration. 
*   **The Artifact:** A lightweight Figma plugin (built as a sidecar prototype) that sends a text string or image frame to a dummy API, returning a simulated "Artificial Societies Sentiment Score" directly inside Figma.
*   **The Message Logic:** *"James - I saw the recent analyst breakdown comparing your graph simulation to Ditto. Your underlying Cambridge methodology is obviously superior to their static polling, but they are capturing product teams purely because they have a Figma plugin. You shouldn't have to pull Tom off the core LangChain engine to build generic enterprise integrations. I run a forward-deployed engineering strike team. I spent the weekend building this Figma plugin sidecar that sits upstream of your core engine. It allows enterprise designers to ping your API without leaving their canvas. We build these enterprise wrappers in 1-week sprints for £10k/month, and we never touch your core IP."*

### Rank 2: The "Launch HN / Frontend Velocity" Angle 
This angle leverages He's self-deprecating admission on Hacker News regarding their website deployment, combined with their current struggle to hire a Founding Designer.

*   **The Hook:** Quote his exact Hacker News reply regarding the website testing failure. Map this to the fact that they have a £150k open requisition for a Founding Designer.
*   **The Artifact:** A fully coded, high-fidelity interactive React component (perhaps a network graph data visualization or a dashboard widget) that represents how a Fortune 100 client would interact with Radiant's data.
*   **The Message Logic:** *"James - I laughed at your Launch HN comment about simulating your content but failing to test the actual website before it was built. I see you're currently trying to hire a Founding Designer to fix exactly this UX/frontend bottleneck. Hiring that role takes months, but Teneo and your F100 clients need polished dashboards today. My FDE strike team builds bolt-on frontend sidecars for B2B AI startups. I built this interactive sentiment-graph component as an example of what we can bolt onto your backend JSON outputs in a one-week sprint. We act as your interim frontend/integration team while you take your time finding the right full-time design hire."*

### Rank 3: The "Teneo Data Ingestion" Angle
This angle focuses on the operational scaling challenges of their biggest public case study.

*   **The Hook:** Reference the Teneo case study where they simulated 180,000+ responses using Pulsar data. Acknowledge that custom data ingestion for every new enterprise client is a massive drag on engineering resources.
*   **The Artifact:** A Python/TypeScript middleware script that takes a raw, messy CSV of simulated qualitative data and automatically structures it into clean persona prompts for a standard LLM.
*   **The Message Logic:** *"James - The Teneo case study simulating 180k perspectives is incredible. But from the outside, translating raw Pulsar social listening data into structured personas for your core engine looks like a heavy data-engineering lift for every new client. That kind of bespoke integration slows down sales cycles. We build upstream data-ingestion sidecars that automate the cleaning and formatting of enterprise data before it hits your core API. Here is a prototype ingestion script we built that normalizes standard CRM data into AI persona templates. We can build and maintain these client-specific data bridges so Tom doesn't have to."*

## 7. Red Flags / Gaps

While Artificial Societies is an ideal target for Kaide Labs, the following organizational risks and gaps should be monitored during engagement:

*   **Philosophical Rigidity vs. Commercial Reality:** He has drawn strict ethical lines, explicitly stating they have "made it a rule to never touch defence use cases" and emphasizing the desire to build a "consumer product that anyone can use, rather than going after bigger budgets" [query]. However, their actual traction (and Point72 funding) is coming from massive enterprise budgets (e.g., $50k to $250k+ ACV contracts) via Radiant [cite: 1, 7, 14]. If Kaide Labs pushes an exclusively hyper-capitalist enterprise angle, it may clash with He's academic, democratized-access ideology. Outreach must balance enterprise ROI with his mission of "collective innovation" [cite: 5].
*   **The Ethical Backlash:** AI simulation platforms face skepticism. On Hacker News, users actively criticized the idea of local governments using synthetic personas instead of real citizens for policy feedback, calling it "alarming" [cite: 22]. If a sidecar project involves government or public policy data, expect heavy internal scrutiny from the founding team regarding data ethics and optics.
*   **API Readiness:** While we are pitching an API integration sidecar, there is a risk that Artificial Societies' backend architecture is not currently modular enough to expose internal APIs, even to a contracted FDE team. If their simulation engine is a monolithic script tightly coupled to their proprietary dashboard, spinning up a sidecar will require them to first untangle their own backend—a task that violates the Kaide Labs "1-week rapid sprint" model. During the discovery call, the primary qualification question must be: *"Do you have a staging environment or internal endpoints that our sidecars can securely ping today?"*



**Sources:**
1. [ycombinator.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2zigBjgV04K5yRjdSXickVFwNYQmKGoEYtX0OKi1follXnh1qq_Zl_USKFay7p9JbAVK154tLBdP6-PDMt-0Gs1_q30UDjaYrf6rN-hyJJT11faht5mzes5XmEe27h23bbYCyshX--riIeHcI4aEc)
2. [james-k-he.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE1A8wufxANpipZHv6MbW1sPMZTnmm_AwwZkPSzQgzLr9wSrffoqTFyMhku2C9TGwklFUrd-Yoc3G70yOwmm1mj1Pl7wRFT3YOiwSK1mOxHAY8=)
3. [james-k-he.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFAnA_Yb6RxXna_21UA9eUAKcJuv7puEA-YUBzV4vXkH8YFmBYCju3QbsG3p-gUNmINhZBd-UfMbNQnzdxEJbE-g2U4A2ZlpOpiHSR3slqhgB1wlnVs)
4. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGUWE-TNxtpYpBQmgAbLuu6CAV5govfP19p6Q55bCL-T9p8ao1qO6j0LgNgDTC1AbGZOOCFGwkwXIeHbIAPcd6exfCKeA1kqzvwdw38C-RyhHnzJE0rbnVBOiRnpS-SQ-a5)
5. [james-k-he.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGEXfxubHaEDLCYJ2WlSWq-MmeLJbRjAR0VMUJDveJHNNtyMH5gEefWTZXWze_JsYv1HzPE-xuBVQVUt4mJBQNfK30cVqh9_b8TBxpvILsgzud53gEE)
6. [james-k-he.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE3SMD9F1ZeVl4uLGFcR4fm0CVKm2ZtnWygHu9ua-nwpIlrnJJOhF8a0FceLWcfQJ9WSJdIQ1oTUN1OCyN6Y9d-nbp8tOej9YUqOL-W5vM1a0TwUXe5)
7. [fish.dog](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGMi1W_vSx2HIiRiHoTd2z8igvxNMqqtoff-EuqyWWZw0QSxtN6leEKkGakc843n8ot_FRalc7JJL9Pc3uWc4mNsGD7hjpacOSKvnC07ZBim38PpbzQHkTIHrHndS3Gsnj8B5GbbDRrYPolH3Lj_kmTRgY9C-Lg6W8AIz9t8PuJXQpXl-UXSe6d)
8. [aimultiple.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHnbn3YmcGca0A6t_553ep5O6oUhyZ5-JiH97rnzS9Ac_etuoHLjMKCVvoiGYlCoDutYLXj6T6WPYJhOGULbbcw7Ub_MOfdneYuHiUhDTILFCbupZle-BPllgyAYnSsVO8=)
9. [societies.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYTvaC59i2e5MczK3RyETWlGdp-467_ItH6cqI4M8VJMRkxTg0QAxQBZTovXiXcnV12juW22uUvY9Yr5FIyOSufmu4sPSUa1wkh3Dod-HQdpriA_wT8w_7Yj8WT50=)
10. [societies.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHwmvbIRej6UlkzxkBBCU_rQn057I0c6t7Dl5UNiYidyZ0GGwLVfbLf1ISG5IRBrnXsvRk1eEfbT2J6wj_YnEi18ZsfHs4UDCviSRY=)
11. [unite.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6IjWxOkW5IxUZYWtohwkoQW5J47950PtAuHOU2-6dOPVdEX9-ZAGoQp_esCZqj7Nkowf9N0e8eK4o20rHUQOrs1H0TlfE9Gz-k_cDPUFsDd-YLVRrNqfWzSWflR2rSBpZcY5vUFRxdEuxVH1pX345RHP0JD0vfekeyEzU1opxijQCAcR7LEA3UrMUv-MYm_Xp5nENSAmAr7tZMO4e3XsyNOIYm6tUlnJ5fg==)
12. [businessinsider.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy5NiKp1dmjfw-Z3bB8Quz6v_n_skDVeMWFjuDH61x-VInyIfppakXH8yxFSwlmkbEWXk9xTbGtY3ZZrJs-oMH0_HhoJKH3PQYvJwy82s8CDBuT2jvJH4lA5HTdi1TiB3bPbQg9j_In0ZRTqNdT2zB9La49-o3G2Se_yUiYPJmuo81ZaFRhVfIVrNR_2HRMl4PEtaMbaA=)
13. [fish.dog](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGns5L_zvzP6FGqKSfEHVAt3DbCIip1aEI-wYnwbhU2ZDjxcJ_HVv-e5mPNSXuKQbUPHfR-CgEfo22Y3dmPTEN40QE8i5dgnoSO5GSZiqYyEDy7f0Za8Q6cxRN5ToWLM6dkyJ-t0a8hY1cF_9ehCAdHkcsDVIsQLY4Xk-LWGZMBug==)
14. [societies.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJ2JcqiRyNhxefbINgkiuRiG76BE-lcdpZb1_rU4UC8i17ctJvEGqoZjg3Tj5d9HyjR6pHIe76neYP04JYxs6qGo7A3EUl0NF1putGZvomLVA8a5yhoD7xBQ2Y)
15. [fish.dog](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEc31Ij1o__V7T2onVNvSlCbtluXYbdjsRIbipQarRhfr5x0khECcI3RTy1dNr3RxyjeC0DsYHP0YsLBcPkpa6DtCMBzRVuty2wxyQLOlsuuYcot261fECoeScSb2POT8G29ENo_TJ2stv4d4vsBEmGdysycDfJMy3clA==)
16. [fish.dog](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFuowoFLskOfbRiQ7WxzLyOlHhJtyfcCMhYIIR2B6S-RCeEGojZPPzd-PCz1NOkluK-VDjjvvnahBUM5IPWeqoGe9YGYQ4Lpc69Lnf9yfxYn-kvl3Csg4L_f4LK1wkDDJetwFZBwvT7-YBF5l3vGu-7FDxXxKJ2Htk6shre1-_9ANZYGnU8_KtxkEkorj0KsftphWrW_rj2UPTIwbuxy45q-0Hw2uE=)
17. [fish.dog](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFmihJiybX6-gm6A_JPJLDaoy44ilFqL_6X1nwL1FX4VWUprUMBOrpBUax-VWvt2LX-tzV4kRRSOJMyfogSus0s2cvoAa1TQN6aypWdJT81LTDQrlqbU0B7A2FNRrfvDtJ4bdLoprb7f3_4t5wNOjGA_W5s38G8Wy1yG77iUg2kfogGDO4BbKrv8A==)
18. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFIAFLAPbGhmuNFqALAkI58HlkE4pnnKI-xNSu0BOwWqKVPYElZawacc4OQN4dQUCCCFjaD7_do6C8DscoJoSOwf9c9aw0D8AQxoUGOMpcDBhTyGSkDed_6QrpPrfxJiNrTpsCJuhKfcCbCLQMuXOY=)
19. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2fJAbRrrYKd2Ip2vh6afNySCKT2j6r5MyQsYM_Hddep1AFX1m1O1ok7uQRC6fosbBRaV3-_anNRuLoBStwrJ0g9FtwyAevIMY6j63UI4pV4URj974l-IASbB2RZhDCRYr1OxFWU6ErHSKxBEFw7ldTvHSAJVralAK6qgzLZkUwHnLv46XCEK7T76TZleQgVVwerOuUgEuOlyK0QSeEnf3KXTgHqnrDjsmmXA=)
20. [aitinkerers.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHDGgmr-GmIrJbJLD_3BpM_Bmh94ynR13IORz66yUwlvn0V1c6FvoBnE1MWo0nlWtXDfJsEi-Mz5SHctJNCh3ZQeeu5O41kMoXbwDPEka7BhlNvYZokC1-qflv5F1VQpeYS1Z6DtmzgoqJB6bSv)
21. [github.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH696MUJ_e5KXyO9-gTlyuNwsklfMOsnKjqTSUOrHZN_xwrf-xcWhZ5XZZWntkzouIe4b8PD1YCDp3dYXR0b2OcfOXwJqi5hdF54yWNhBahFG8=)
22. [ycombinator.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFwO4W5BK-3StPcVCVMpxPowtBH-lnDp4fQmNawEe_-Qg8KTZA19r_mw9SEkBjC33hGZdeQbeURWDgDyJ63ebR-qUwFqvqRVFAcNEb5_ttPVjOYtHCq_YPurZrKP3sWyyLPjCM=)


