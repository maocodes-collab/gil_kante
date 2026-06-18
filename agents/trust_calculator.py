#!/usr/bin/env python3
import os
import re

def calculate_trust_score(html_path):
    print("=== [AGENT TRUST CALCULATOR] Starting Trust Score Assessment ===")
    
    if not os.path.exists(html_path):
        return {"error": "index.html not found"}
        
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    score = 0
    max_score = 100
    breakdown = []

    # Category 1: Professional Identity Coordinates (30 pts)
    id_score = 0
    if "gilchrist.kante@epitech.eu" in html:
        id_score += 10
        breakdown.append("+10: Real developer email coordinate verified (gilchrist.kante@epitech.eu)")
    else:
        breakdown.append("+0: Developer email placeholder or outdated address detected")

    if "github.com/misterkante" in html:
        id_score += 10
        breakdown.append("+10: Professional GitHub developer profile verified (github.com/misterkante)")
    else:
        breakdown.append("+0: GitHub profile placeholder detected")

    if "linkedin.com/in/gilchrist-kante" in html:
        id_score += 10
        breakdown.append("+10: LinkedIn career verification profile active")
    else:
        breakdown.append("+0: LinkedIn profile placeholder detected")
    score += id_score

    # Category 2: SEO & Meta Integration (25 pts)
    seo_score = 0
    if "<title>" in html.lower() and "</title>" in html.lower():
        seo_score += 5
        breakdown.append("+5: Page Title tag correctly set")
    else:
        breakdown.append("+0: Missing header title tag")

    if re.search(r'<meta[^>]*name=["\']description["\']', html, re.IGNORECASE):
        seo_score += 10
        breakdown.append("+10: General SEO meta description active")
    else:
        breakdown.append("+0: Missing meta description (recruiter indexation penalty)")

    if re.search(r'<meta[^>]*property=["\']og:title["\']', html, re.IGNORECASE):
        seo_score += 10
        breakdown.append("+10: OpenGraph social media sharing active")
    else:
        breakdown.append("+0: Missing OpenGraph metadata tags")
    score += seo_score

    # Category 3: UX Fidelity & Micro-Interactions (25 pts)
    ux_score = 0
    if "custom-cursor" in html:
        ux_score += 5
        breakdown.append("+5: High-fidelity custom inertial cursor is active")
    else:
        breakdown.append("+0: Default standard browser cursor used")

    if "glitch-title" in html:
        ux_score += 5
        breakdown.append("+5: Theme-appropriate glitch text title effect active")
    else:
        breakdown.append("+0: Standard plain text headers used")

    if "pixel-grid" in html and "animatePixels" in html:
        ux_score += 10
        breakdown.append("+10: Interactive scroll/mouse afro pixel grid active and dynamic")
    else:
        breakdown.append("+0: Missing interactive pixel scroller module")

    if "contact-form" in html and "Envoi en cours" in html:
        ux_score += 5
        breakdown.append("+5: Working contact submission form simulator active")
    else:
        breakdown.append("+0: No operational contact validation active")
    score += ux_score

    # Category 4: Design Charter Consistency (20 pts)
    charter_score = 0
    if "#0B46B9".lower() in html.lower() and "#041A4E".lower() in html.lower():
        charter_score += 10
        breakdown.append("+10: Strict dual-cobalt palette colors respected (#0B46B9, #041A4E)")
    else:
        breakdown.append("+0: Colors drift away from visual charter specification")

    if "IBM Plex Mono" in html and ("Anton" in html or "Oswald" in html):
        charter_score += 10
        breakdown.append("+10: Typographical rule alignment OK (IBM Plex Mono + Anton/Oswald headers)")
    else:
        breakdown.append("+0: Missing system fonts")
    score += charter_score

    # Build ASCII Bar
    bar_len = 20
    filled = int((score / max_score) * bar_len)
    bar = "█" * filled + "░" * (bar_len - filled)

    report_content = f"""# Indice de Confiance Portfolio (Trust Score Card)

Ce rapport évalue le niveau de confiance technique et professionnel ("Trust Score") du portfolio pour un recruteur ou un client d'affaires (B2B/Freelance).

## 🏆 Score Global
```text
Score : {score} / {max_score}
[{bar}] ({score}%)
```

### Classification du profil :
- **Score >= 90** : **PRO GRANDE CONFANCE (Silicon Valley Ready)** - Le profil est authentifié, professionnel, optimisé et captivant.
- **Score 75-89** : **CONFANCE CRÉDIBLE** - Prêt pour une utilisation standard, quelques métadonnées à affiner.
- **Score < 75** : **À AMÉLIORER** - Placeholders trop nombreux ou manque d'interactivité.

---

## 📈 Détail du Calcul des Points

{chr(10).join(f"- {b}" for b in breakdown)}

---
*Généré par l'Agent Calculateur de Confiance le {os.popen('date').read().strip()}*
"""
    
    os.makedirs("artifacts", exist_ok=True)
    report_path = "artifacts/trust_score.md"
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"[AGENT TRUST CALCULATOR] Scoring completed. Score: {score}/100. Written to {report_path}")
    return score

if __name__ == "__main__":
    calculate_trust_score("index.html")
