#!/usr/bin/env python3
import csv
import json
import argparse
from datetime import datetime
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Automated RBAC & Least Privilege Access Audit CLI")
    parser.add_argument("-i", "--input", required=True, help="Path to input IAM CSV file")
    parser.add_argument("-o", "--output", default="audit_evidence.json", help="Path to output JSON evidence file")
    return parser.parse_args()

def check_stale_account(last_login_str):
    try:
        last_login = datetime.strptime(last_login_str, "%Y-%m-%d")
        diff = (datetime.now() - last_login).days
        if diff > 90:
            return f"Last login was {diff} days ago (>90 threshold)."
    except ValueError:
        return "Invalid date format."
    return None

def check_sod(roles):
    if "Developer" in roles and "Production Deployer" in roles:
        return "Holds both Developer and Production Deployer roles."
    return None

def check_excessive_admin(is_admin, dept):
    if is_admin.upper() == "TRUE" and dept not in ["IT", "Engineering"]:
        return f"Admin rights assigned to non-technical Department ({dept})."
    return None

def run_audit(input_file):
    findings = []
    total_audited = 0
    
    try:
        with open(input_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_audited += 1
                emp_id = row.get("EmployeeID", "Unknown")
                roles = [r.strip() for r in row.get("Roles", "").split("|")]
                
                # Run checks
                stale_err = check_stale_account(row.get("LastLoginDate", ""))
                sod_err = check_sod(roles)
                admin_err = check_excessive_admin(row.get("IsAdmin", "FALSE"), row.get("Department", ""))
                
                violations = []
                if stale_err: violations.append({"type": "Stale Account", "detail": stale_err})
                if sod_err: violations.append({"type": "SoD Violation", "detail": sod_err})
                if admin_err: violations.append({"type": "Excessive Privilege", "detail": admin_err})
                
                if violations:
                    findings.append({
                        "employee_id": emp_id,
                        "name": row.get("Name", "Unknown"),
                        "department": row.get("Department", "Unknown"),
                        "violations": violations
                    })
    except FileNotFoundError:
        print(f"Error: Could not find file {input_file}")
        sys.exit(1)
        
    return total_audited, findings

def print_summary(total, findings, output_file):
    print("\n" + "="*50)
    print(" 🛡️  IAM RBAC & LEAST PRIVILEGE AUDIT REPORT")
    print("="*50)
    print(f"Total Identities Audited : {total}")
    print(f"Identities with Flags    : {len(findings)}")
    risk_score = round((len(findings) / total * 100), 2) if total > 0 else 0
    print(f"Overall Risk Score       : {risk_score}%\n")
    
    if not findings:
        print("✅ No violations found. Audit passed successfully.")
    else:
        print("🚨 VIOLATIONS FOUND:")
        for f in findings:
            print(f"  - [{f['employee_id']}] {f['name']} ({f['department']})")
            for v in f['violations']:
                print(f"      -> {v['type']}: {v['detail']}")
                
    print("\n" + "-"*50)
    
    # Export evidence
    with open(output_file, 'w', encoding='utf-8') as out:
        json.dump({"total_audited": total, "risk_score": risk_score, "findings": findings}, out, indent=4)
    print(f"📄 Detailed audit evidence saved to: {output_file}\n")

if __name__ == "__main__":
    args = parse_args()
    total, findings = run_audit(args.input)
    print_summary(total, findings, args.output)
