# AI Risk Tiering & Governance Engine

A lightweight, browser-based utility designed to streamline preliminary risk assessments for AI systems. This tool evaluates basic model metadata against the risk tiers outlined in the EU AI Act and automatically surfaces applicable control requirements from the NIST AI Risk Management Framework (AI RMF 1.0).

---

## Why This Exists

Conducting initial risk intake for internal AI applications is often manual, repetitive, and fragmented across spreadsheets. Compliance leads and GRC teams need a fast, standardized way to triage incoming requests from engineering and product groups before committing resources to formal assessments.

This application provides an instant baseline assessment. It translates high-level system parameters, such as intended domain, autonomy levels, and data sensitivity, into immediate and actionable regulatory gaps and framework mappings.

---

## How the Rule Logic Works

The evaluation engine uses a simple client-side decision matrix to classify tools and assign safeguards:

### 1. EU AI Act Classification
* **Unacceptable Risk:** Flags prohibited use cases, such as social scoring or untargeted real-time biometrics in public spaces, and advises immediate decommissioning steps.
* **High Risk:** Triggers for high-stakes deployment areas such as employment and recruitment, education, critical infrastructure, and medical evaluation. Highlights mandatory items like human oversight under Article 14, continuous logging under Article 12, and conformity assessments under Article 43.
* **Limited Risk:** Focuses on transparency obligations under Article 52 for customer-facing bots, generative models, and output disclosures.
* **Minimal Risk:** Identifies low-stakes operational software, such as internal text parsers or IT rule engines, requiring only baseline data privacy compliance.

### 2. NIST AI RMF Mapping
Based on the assigned risk tier, the tool maps required governance actions to the four core NIST AI RMF functions:
* **GOVERN:** Framework policies, oversight structures, and decommission workflows.
* **MAP:** Contextual impact analysis, dependency mapping, and third-party risk.
* **MEASURE:** Pre-deployment testing, bias assessments, and model drift checks.
* **MANAGE:** Operational controls, continuous monitoring, and incident response plan execution.

---

## Technical Architecture

* **Zero Infrastructure:** Built as a single-page web app using HTML5, Tailwind CSS via CDN, and plain JavaScript. No backend server, databases, or build steps required.
* **Data Privacy by Design:** All calculations and data evaluations happen locally within the user browser. No intake data or model parameters are ever sent to an external server.
* **Artifact Generation:** Allows auditors and engineers to export the final assessment directly from the interface as structured JSON for database ingestion or formatted Markdown for reporting.

---

## Quick Start

1. Clone or download this repository.
2. Open index.html in any browser.
3. Complete the form parameters on the left and click Execute Automated Risk Tiering.
4. Review the generated gap analysis or export the assessment summary for documentation.

---

## User Guide & Input Requirements

To generate an automated risk evaluation and baseline safeguard mapping, the tool requires six key inputs:

* **System Name:** The internal identifier or official product name of the AI application (e.g., Enterprise CV Screener, SupportBot Gen3).
* **Business Department:** The organizational unit responsible for operating or owning the model (e.g., Human Resources, Customer Experience, IT Operations).
* **System Domain / Use Case:** The intended deployment environment. This selection directly determines the statutory EU AI Act risk tier (e.g., Employment/HR triggers High Risk, Social Scoring triggers Prohibited/Unacceptable Risk).
* **Model Architecture:** The underlying model type (e.g., Predictive Analytics, Generative AI / LLM, Rule-Based Expert System).
* **Data Sensitivity Level:** The highest classification level of data processed by the system (e.g., Public, Internal Operational, PII/PHI).
* **Human-in-the-Loop (HITL) Status:** Indicates whether qualified human oversight approves outputs before execution or if the system runs fully autonomously.

---

## Operating the Engine

1. Select or input the six metadata fields in the **Model Metadata Audit Form**.
2. Click **Execute Automated Risk Tiering**.
3. Review the generated **Automated Gap Analysis** and **NIST AI RMF 1.0 Requirements** panels on the right.
4. Export the final audit report using the top-right control icons:
   * **Document Icon:** Downloads a clean, formatted PDF assessment report suitable for executives, legal counsel, or external auditors.
   * **Code Icon (`</>`):** Downloads the raw structured JSON assessment payload for database ingestion or GRC software integration.
