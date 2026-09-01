# Automated RBAC & Least Privilege Access Audit Tool

[![Live Demo](https://img.shields.io/badge/Live_Demo-Click_Here-blue.svg)](https://governance.jainamcgregor.com/projects/rbac-audit-tool/)
[![Frameworks](https://img.shields.io/badge/Compliance-SOC2_CC6.1_%7C_ISO27001_A.9.2-green.svg)](#)

## Overview
This toolkit automates the auditing of Identity and Access Management (IAM) configurations. It analyzes raw user access logs to identify critical security risks, outputting actionable evidence for security teams and compliance auditors.

## Supported Compliance Frameworks
* **SOC 2 (CC6.1 - Logical Access):** Automatically detects inappropriate access configurations, failure to implement least privilege, and inactive accounts that pose a security risk.
* **ISO 27001 (A.9.2 - User Access Management):** Validates the lifecycle of user access, specifically highlighting excessive privileges and Separation of Duties (SoD) conflicts.

## Diagnostic Checks Engine
1. **Separation of Duties (SoD):** Flags toxic combinations of roles (e.g., users holding both `Developer` and `Production Deployer` permissions).
2. **Stale Accounts:** Identifies identities that have not authenticated in >90 days.
3. **Excessive Admin Privileges:** Flags accounts possessing administrative permissions outside of designated technical departments (IT/Engineering).

## Usage Instructions

### Web Dashboard
Navigate to the Live Demo link above. Click **"Run Audit on Demo Data"** to see the diagnostic engine instantly flag violations, or upload your own CSV following the `sample_access_report.csv` schema.

### CLI Utility
Requires Python 3.x (No external dependencies).
```bash
python3 audit_iam.py -i sample_access_report.csv -o evidence.json
