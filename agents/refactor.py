#!/usr/bin/env python3
import os
import re

def run_refactor(html_path, charter_path):
    print("=== [AGENT REFACTOR] Initiating Automated Code Refactoring ===")
    
    if not os.path.exists(html_path):
        return {"error": "index.html not found"}
        
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()

    refactored_actions = []

    # 1. Inject missing SEO & OpenGraph tags if they do not exist
    missing_seo_tags = []
    
    # Check general description
    if not re.search(r'<meta[^>]*name=["\']description["\']', html, re.IGNORECASE):
        missing_seo_tags.append('<meta name="description" content="Portfolio de Gil Kante - Développeur Fullstack React / NestJS. Solutions numériques robustes du code à la production.">')
        refactored_actions.append("SEO: Injected general meta description")

    # Check og:title
    if not re.search(r'<meta[^>]*property=["\']og:title["\']', html, re.IGNORECASE):
        missing_seo_tags.append('<meta property="og:title" content="Gil Kante | Développeur Fullstack React / NestJS">')
        refactored_actions.append("Social: Injected og:title meta tag")

    # Check og:description
    if not re.search(r'<meta[^>]*property=["\']og:description["\']', html, re.IGNORECASE):
        missing_seo_tags.append('<meta property="og:description" content="Découvrez le portfolio \'Cyber-Urban Afrofuturism\' de Gil Kante. Des applications performantes et créatives de bout en bout.">')
        refactored_actions.append("Social: Injected og:description meta tag")

    # Check og:image
    if not re.search(r'<meta[^>]*property=["\']og:image["\']', html, re.IGNORECASE):
        missing_seo_tags.append('<meta property="og:image" content="profile.jpg">')
        refactored_actions.append("Social: Injected og:image meta tag")

    # Check og:url
    if not re.search(r'<meta[^>]*property=["\']og:url["\']', html, re.IGNORECASE):
        missing_seo_tags.append('<meta property="og:url" content="https://github.com/misterkante">')
        refactored_actions.append("Social: Injected og:url meta tag")

    # Check twitter:card
    if not re.search(r'<meta[^>]*name=["\']twitter:card["\']', html, re.IGNORECASE):
        missing_seo_tags.append('<meta name="twitter:card" content="summary_large_image">')
        refactored_actions.append("Social: Injected twitter:card meta tag")

    # Check favicon
    if not re.search(r'<link[^>]*rel=["\'](shortcut )?icon["\']', html, re.IGNORECASE):
        missing_seo_tags.append('<link rel="icon" type="image/x-icon" href="profile.jpg">') # using profile.jpg as placeholder icon if none exists
        refactored_actions.append("Identity: Injected icon favicon reference link")

    if missing_seo_tags:
        # Construct the injection block
        injection_text = "\n  <!-- Added by Agent Refactor for Silicon Valley & Social Media Compliance -->\n  " + "\n  ".join(missing_seo_tags) + "\n"
        
        # Inject right after <head> or before first meta tag
        head_match = re.search(r'<head[^>]*>', html, re.IGNORECASE)
        if head_match:
            pos = head_match.end()
            html = html[:pos] + injection_text + html[pos:]
            refactored_actions.append("Integrations: Injected custom SEO/OG block to <head>")
        else:
            refactored_actions.append("Warning: <head> tag not found; could not inject SEO/OG block automatically")

    # 2. Write the modified index.html back
    if refactored_actions:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"[AGENT REFACTOR] index.html successfully updated with {len(refactored_actions)} improvements.")
    else:
        print("[AGENT REFACTOR] No refactoring modifications needed for index.html.")

    # 3. Update the Design Rules (charte_design_portfolio.md)
    charter_updated = False
    if os.path.exists(charter_path):
        with open(charter_path, 'r', encoding='utf-8') as f:
            charter_content = f.read()

        # Check if audit rule section already exists
        if "## 7. Règles d'Audit & Conformité Technique" not in charter_content:
            compliance_rules = """
---

## 7. Règles d'Audit & Conformité Technique (Silicon Valley Standards)

*Ajouté par l'Agent Refactor lors de la phase de polissage.*

### A. Métadonnées Sociales obligatoires (SEO/OpenGraph) :
Chaque page doit comporter des balises `og:title`, `og:description`, `og:image`, `og:url` et `twitter:card` pour assurer un rendu parfait lors de partages professionnels sur LinkedIn, Twitter et Slack.

### B. Accessibilité Standard (A11y) :
* Tous les éléments interactifs (`a`, `button`, `input`) doivent posséder un attribut `aria-label` descriptif ou un attribut équivalent si le texte n'est pas explicite.
* Les images doivent obligatoirement inclure un attribut `alt`.

### C. Zéro Placeholder en Production :
Les adresses e-mail de type `exemple.com` et profils sociaux fictifs doivent être formellement proscrits au profit de profils vérifiés (GitHub `misterkante` et email `gilchrist.kante@epitech.eu`).
"""
            with open(charter_path, 'a', encoding='utf-8') as f:
                f.write(compliance_rules)
            refactored_actions.append("Design System: Appended Section 7 'Régles d'Audit & Conformité' to charte_design_portfolio.md")
            charter_updated = True

    # 4. Generate Refactoring Log Report
    log_content = f"""# Log de Réfactorisation (Refactoring Log)

Ce document retrace les corrections et les améliorations automatiques apportées par l'Agent Refactor suite aux analyses de conformité.

## 🛠️ Actions de Réfactorisation Appliquées

{chr(10).join(f"- [x] {a}" for a in refactored_actions) if refactored_actions else "Aucune correction n'a été nécessaire. Le code est déjà conforme."}

---
*Généré par l'Agent Refactor le {os.popen('date').read().strip()}*
"""
    
    os.makedirs("artifacts", exist_ok=True)
    log_path = "artifacts/refactoring_log.md"
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(log_content)

    print(f"[AGENT REFACTOR] Refactoring log successfully written to {log_path}")
    return {"actions": len(refactored_actions), "charter_updated": charter_updated}

if __name__ == "__main__":
    run_refactor("index.html", "charte_design_portfolio.md")
