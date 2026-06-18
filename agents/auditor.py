#!/usr/bin/env python3
import os
import re

def run_audit(html_path, charter_path):
    print("=== [SV-AUDIT-AGENT] Starting Silicon Valley Technical Assessment ===")
    
    if not os.path.exists(html_path):
        return {"status": "NO-GO", "error": "index.html not found"}
        
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Evaluate Metrics-First (Numbers with % or units)
    metrics = re.findall(r'\b\d+(?:[\.,]\d+)?\s*(?:%|ms|users|utilisateurs|requêtes|req/s|Go|Mo|kb/s|s\b)', html, re.IGNORECASE)
    has_metrics = len(metrics) > 0

    # 2. Evaluate Depth of the Stack (advanced patterns)
    stack_keywords = ["react", "nestjs", "supabase", "prisma", "jwt", "postgresql"]
    found_stack = [kw for kw in stack_keywords if kw.lower() in html.lower()]
    stack_score = len(found_stack)

    # 3. Evaluate Quality of Architecture (TDD, CI/CD, modularity)
    arch_keywords = ["tdd", "jest", "tests", "maintenabilité", "ci/cd", "modulaire", "clean code"]
    found_arch = [kw for kw in arch_keywords if kw.lower() in html.lower()]
    arch_score = len(found_arch)

    # 4. Evaluate System Complexity (NFC, sync, offline-first, hardware)
    complex_keywords = ["nfc", "sync", "synchronisation", "temps réel", "offline-first", "analytics"]
    found_complex = [kw for kw in complex_keywords if kw.lower() in html.lower()]
    complex_score = len(found_complex)

    # Determine Global Status
    if not has_metrics or arch_score == 0:
        global_status = "À AMÉLIORER"
    elif stack_score >= 4 and complex_score >= 3 and has_metrics:
        global_status = "GO"
    else:
        global_status = "À AMÉLIORER"

    # Analyze strengths and weaknesses
    strengths = []
    weaknesses = []
    plan_action = []

    if stack_score >= 4:
        strengths.append(f"Excellente largeur de la stack technique moderne (React, NestJS, Supabase/PostgreSql).")
    else:
        weaknesses.append("Stack technique trop superficielle ou manque d'outils avancés.")

    if found_complex:
        strengths.append(f"Preuve d'intégration matérielle et de complexité système réelle (NFC/Scan, profiles dynamiques).")
    else:
        weaknesses.append("Projets à faible complexité algorithmique ou système (ressemble à des clones d'école).")

    if has_metrics:
        strengths.append(f"Preuves d'impact quantifiables détectées ({len(metrics)} métriques trouvées).")
    else:
        weaknesses.append("Absence de métriques chiffrées (pas de preuves d'optimisation de latence, de taux de réussite, ou d'uptime).")
        plan_action.append("Ajouter des métriques de performance chiffrées pour le projet minds3o (ex: 'Réduction de 40% du temps de chargement initial').")

    if arch_score == 0:
        weaknesses.append("Aucune mention de tests automatisés (TDD, Jest), de workflows CI/CD ou d'architecture modulaire.")
        plan_action.append("Spécifier l'utilisation du TDD (Jest) et l'intégration de pipelines CI/CD dans le descriptif de l'application Notes de Frais.")

    # Fill default actions if empty
    if not plan_action:
        plan_action.append("Ajouter des détails sur la gestion du cache Redis pour optimiser les appels API NestJS.")
        plan_action.append("Détailler l'architecture Event-Driven (Websockets) utilisée dans la synchronisation NFC.")
    if len(plan_action) < 3:
        plan_action.append("Détailler l'implémentation de la conformité RGPD/chiffrement dans la base Supabase/PostgreSQL.")

    report_content = f"""### [Rapport d'Audit - Candidature Silicon Valley]
* **Statut Global :** {global_status}
* **Points Forts (Hard Tech) :**
{chr(10).join(f"  - {s}" for s in strengths)}
* **Faiblesses Critiques (Bloquants SV) :**
{chr(10).join(f"  - {w}" for w in weaknesses) if weaknesses else "  - Aucune faiblesse bloquante identifiée."}
* **Plan d'Action Immédiat :**
{chr(10).join(f"  - {p}" for p in plan_action)}
"""

    os.makedirs("artifacts", exist_ok=True)
    report_path = "artifacts/audit_report.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"[SV-AUDIT-AGENT] Assessment complete. Status: {global_status}. Written to {report_path}")
    return {"status": global_status, "strengths": strengths, "weaknesses": weaknesses, "plan_action": plan_action}

if __name__ == "__main__":
    run_audit("index.html", "charte_design_portfolio.md")
