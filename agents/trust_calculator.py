#!/usr/bin/env python3
import os
import re

def calculate_trust_score(html_path):
    print("=== [TRUST-SCORE-AGENT] Starting B2B Trust Assessment ===")
    
    if not os.path.exists(html_path):
        return {"error": "index.html not found"}
        
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Criteria 1: Reliability & Production-ready deliverables (30 pts)
    reliability_pts = 0
    # Check if there are valid live links (minds3o.com is live)
    if "minds3o.com" in html:
        reliability_pts += 15
    if "En ligne" in html or "déployé" in html.lower():
        reliability_pts += 15

    # Criteria 2: Risk Management & Security (25 pts)
    security_pts = 0
    security_keywords = ["jwt", "chiffrement", "rôles", "sécurité", "authentification", "validation"]
    found_security = [kw for kw in security_keywords if kw.lower() in html.lower()]
    security_pts = min(25, len(found_security) * 5)

    # Criteria 3: Teamwork & Leadership (25 pts)
    teamwork_pts = 0
    teamwork_keywords = ["team lead", "sprints", "coordination", "code review", "collaborateurs", "trello"]
    found_teamwork = [kw for kw in teamwork_keywords if kw.lower() in html.lower()]
    teamwork_pts = min(25, len(found_teamwork) * 5)

    # Criteria 4: Technical Communication Clarity (20 pts)
    comm_pts = 0
    if len(html) > 50000: # detailed documentation
        comm_pts += 10
    if "IBM Plex Mono" in html: # professional typography
        comm_pts += 10

    total_score = reliability_pts + security_pts + teamwork_pts + comm_pts

    # Determine risk level
    if total_score >= 85:
        risk_level = "Faible"
    elif total_score >= 60:
        risk_level = "Modéré"
    else:
        risk_level = "Élevé"

    # Commercial analysis points
    strengths = []
    barriers = []
    recommendation = ""

    if reliability_pts >= 25:
        strengths.append("Projets réels et physiques déployés en production (Système NFC et Plateforme Minds3o).")
    else:
        barriers.append("Manque de projets de production vérifiables publiquement.")

    if security_pts >= 15:
        strengths.append("Prise en compte des mécanismes d'authentification sécurisés (JWT, rôles, Supabase).")
    else:
        barriers.append("Faible mention des mécanismes de chiffrement et de conformité des données (RGPD).")

    if teamwork_pts >= 15:
        strengths.append("Profil hybride démontrant des compétences de leadership (Team Lead, code reviews, coordination agile).")
    else:
        barriers.append("Absence de preuve de travail en environnement d'équipe structuré ou CI/CD.")

    # Custom recommendation
    if total_score < 90:
        recommendation = "Ajouter des mentions explicites sur l'automatisation de l'infrastructure (pipelines CI/CD, GitHub Actions) et la sécurité (conformité HIPAA/RGPD, chiffrement au repos)."
    else:
        recommendation = "Mettre en avant le ROI financier ou le gain de productivité apporté aux clients précédents (ex: réduction des coûts de gestion des frais de 30%)."

    report_content = f"""### [Indice de Confiance B2B & Partenariat]
* **Score Global :** `{total_score} / 100`
* **Niveau de Risque :** {risk_level}

### Ventilation des Notes :
* *Livrables Réels :* {reliability_pts}/30
* *Sécurité & Risque :* {security_pts}/25
* *Leadership & Équipe :* {teamwork_pts}/25
* *Communication :* {comm_pts}/20

### Analyse Commerciale :
* **Ce qui inspire confiance :**
{chr(10).join(f"  - {s}" for s in strengths)}
* **Ce qui freine la vente :**
{chr(10).join(f"  - {b}" for b in barriers) if barriers else "  - Aucun frein commercial majeur détecté."}
* **Recommandation pour maximiser le ROI du Portfolio :**
  {recommendation}
"""

    os.makedirs("artifacts", exist_ok=True)
    report_path = "artifacts/trust_score.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)

    print(f"[TRUST-SCORE-AGENT] Scoring assessment complete. Score: {total_score}/100. Written to {report_path}")
    return total_score

if __name__ == "__main__":
    calculate_trust_score("index.html")
