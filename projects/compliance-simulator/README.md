# Continuous Compliance & Audit Readiness Simulator

A lightweight, browser-based utility designed to simulate automated telemetry polling and continuous controls monitoring (CCM) for SOC 2 Type II and ISO/IEC 27001 compliance frameworks.

## Why This Exists

Conducting initial audit preparation and verifying evidence collection pipelines is often manual, repetitive, and fragmented across static checklists. Compliance leads and GRC teams need a fast, standardized way to verify control postures, test coverage gaps, and inspect evidence payloads before committing resources to formal third-party audits.

This application provides an instant baseline evaluation. It translates high-level infrastructure telemetry toggles into immediate posture scores, execution log streams, and verifiable audit evidence ledgers.

## How the Rule Logic Works

The evaluation engine uses a client-side decision matrix to poll simulated scopes and assign compliance statuses:

1. **Posture Score Calculation**
   The simulator evaluates four core infrastructure controls (Cloudflare WAF, IdP MFA, IAM Least Privilege, and Database Encryption). The posture score is calculated dynamically as a percentage of active controls (`(Active Controls / 4) * 100`).

2. **Status Determination**
   * **PASS:** Triggered when all 100% of selected infrastructure controls are verified active and operational.
   * **REVIEW REQUIRED:** Triggered during partial control configurations, highlighting gaps where telemetry is disabled or unmonitored.
   * **FAIL:** Triggered when zero controls are active, indicating a critical security posture breakdown.

## Technical Architecture

* **Zero Infrastructure:** Built as a single-page web app using HTML5, Tailwind CSS via CDN, and plain JavaScript. No backend server, databases, or build steps required.
* **Data Privacy by Design:** All calculations, telemetry checks, and mock API polling happen locally within the user browser. No infrastructure configuration data is ever sent to an external server.
* **Artifact Generation:** Allows auditors and engineers to export the final cryptographic evidence ledger directly from the interface as structured JSON for database ingestion or GRC platform tracking.

## Quick Start

1. Clone or download this repository.
2. Open index.html in any modern web browser.
3. Configure the target framework and telemetry toggles on the left.
4. Click **Run Automated Telemetry Audit** to execute the polling simulation.

## User Guide & Input Requirements

To generate an automated telemetry audit and evidence ledger, the tool utilizes the following configuration parameters:

* **Target Framework:** Selects the governing compliance standard (SOC 2 Trust Services Criteria or ISO/IEC 27001 Controls).
* **Simulated Infrastructure Scope:** Checkbox toggles representing active telemetry pipelines:
  * *Cloudflare Edge Access Logs & WAF*
  * *Identity Provider (Okta/Entra) MFA Enforcements*
  * *IAM Least Privilege & Role Reviews*
  * *Database Encryption at Rest (AES-256)*

## Operating the Engine

1. Select your target framework and adjust the infrastructure scope checkboxes in the **Controls Monitoring Setup** panel.
2. Click **Run Automated Telemetry Audit**.
3. Watch the real-time execution stream populate in the terminal view on the right.
4. Review the final calculated posture score, audit status badge, and cryptographic hash.
5. Export the structured evidence log using the **Download Audit JSON** button for downstream GRC workflows.
