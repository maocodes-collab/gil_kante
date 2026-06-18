#!/usr/bin/env python3
import os
import re

def run_audit(html_path, charter_path):
    print("=== [AGENT AUDITOR] Starting Portfolio Audit ===")
    
    if not os.path.exists(html_path):
        return {"error": f"index.html not found at {html_path}"}
        
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    charter_found = os.path.exists(charter_path)
    charter_text = ""
    if charter_found:
        with open(charter_path, 'r', encoding='utf-8') as f:
            charter_text = f.read()

    # Metrics collections
    findings = []
    passed = []
    
    # 1. Silicon Valley standards check
    sv_keywords = ["React", "NestJS", "TypeScript", "Node", "Docker", "Git", "API"]
    found_keywords = [kw for kw in sv_keywords if kw.lower() in html.lower()]
    if len(found_keywords) >= 4:
        passed.append(f"Silicon Valley Tech Stack: Found {len(found_keywords)} key skills ({', '.join(found_keywords)}) in the portfolio.")
    else:
        findings.append(f"Silicon Valley Tech Stack: Missing standard SV keywords (Found only: {', '.join(found_keywords)}). Recommend highlighting React, NestJS, TypeScript more clearly.")

    # 2. SEO & Social Metadata (Critical for SV recruiting)
    og_meta = {
        "og:title": r'<meta[^>]*property=["\']og:title["\']',
        "og:description": r'<meta[^>]*property=["\']og:description["\']',
        "og:image": r'<meta[^>]*property=["\']og:image["\']',
        "og:url": r'<meta[^>]*property=["\']og:url["\']'
    }
    for tag, pattern in og_meta.items():
        if not re.search(pattern, html, re.IGNORECASE):
            findings.append(f"Social Media SEO: Missing {tag} meta tag. SV recruiters share links on Slack, Twitter, and LinkedIn; nice previews are essential.")
        else:
            passed.append(f"Social Media SEO: {tag} is present.")

    # Twitter card tags
    if not re.search(r'<meta[^>]*name=["\']twitter:card["\']', html, re.IGNORECASE):
        findings.append("Social Media SEO: Missing twitter:card metadata.")
    else:
        passed.append("Social Media SEO: twitter:card metadata is present.")

    # Description tag
    if not re.search(r'<meta[^>]*name=["\']description["\']', html, re.IGNORECASE):
        findings.append("SEO: General page meta description is missing.")
    else:
        passed.append("SEO: Meta description tag is present.")

    # 3. Design System Alignment
    # Check color variable references in CSS
    colors = ["#0B46B9", "#041A4E", "#FFFFFF"]
    charter_colors_ok = True
    for c in colors:
        if c.lower() not in html.lower() and c.upper() not in html.lower():
            charter_colors_ok = False
            findings.append(f"Design System: Strict hex color {c} not found in index.html.")
    if charter_colors_ok:
        passed.append("Design System: Strict hex colors match the design charter (#0B46B9, #041A4E, #FFFFFF).")

    # 4. Accessibility (A11y)
    # Check for empty alt attributes or missing aria-labels
    imgs_without_alt = re.findall(r'<img(?!.*?alt=)[^>]*>', html)
    if imgs_without_alt:
        findings.append(f"Accessibility: Found {len(imgs_without_alt)} images missing standard 'alt' tags.")
    else:
        passed.append("Accessibility: All image tags have 'alt' attributes or proper alternative text labels.")
        
    aria_labels = re.findall(r'aria-label=', html)
    if len(aria_labels) < 5:
        findings.append(f"Accessibility: Low usage of aria-labels ({len(aria_labels)} found). SV accessibility rules demand high-fidelity labels on buttons and links.")
    else:
        passed.append(f"Accessibility: Good aria-label coverage ({len(aria_labels)} labels found).")

    # 5. Performance Check
    # Inline style block size check
    style_size = len(re.findall(r'<style>(.*?)</style>', html, re.DOTALL))
    if style_size > 0:
        passed.append("Performance: Single unified index.html style block is active (reducing extra roundtrip network requests).")
    
    # Check for standard SV favicons
    if not re.search(r'<link[^>]*rel=["\'](shortcut )?icon["\']', html, re.IGNORECASE):
        findings.append("Identity: No favicon link defined in document head.")
    else:
        passed.append("Identity: Favicon link found.")

    # Write report
    report_content = f"""# Rapport d'Audit de l'Agent Auditeur

Ce rapport vérifie l'adéquation du portfolio de Gil Kante pour soumission auprès d'entreprises et recruteurs de la Silicon Valley.

## 📊 Résumé Exécutif
- **Statut de conformité** : {"⚠️ AVERTISSEMENT - RECOMMANDÉ D'AJUSTER" if findings else "✅ PRÊT À SOUMETTRE"}
- **Critères Validés** : {len(passed)}
- **Améliorations Requises** : {len(findings)}

---

## 🔍 Points d'Audit Requis / Améliorations

{chr(10).join(f"- [ ] **{f}**" for f in findings) if findings else "Aucun problème détecté. Le portfolio est optimal !"}

---

## ✅ Points Validés avec Succès

{chr(10).join(f"- [x] {p}" for p in passed)}

---
*Généré par l'Agent Profil Auditeur le {os.popen('date').read().strip()}*
"""
    
    os.makedirs("artifacts", exist_ok=True)
    report_path = "artifacts/audit_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"[AGENT AUDITOR] Audit completed successfully. Report written to {report_path}")
    return {"findings": len(findings), "passed": len(passed)}

if __name__ == "__main__":
    run_audit("index.html", "charte_design_portfolio.md")
