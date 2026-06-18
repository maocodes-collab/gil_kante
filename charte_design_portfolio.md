# Charte Graphique & Spécifications de Design : "Cyber-Urban Afrofuturism"

Ce document sert de guide et de prompt d'ingénierie système pour le redesign complet d'un portfolio web. L'objectif absolu est de reproduire l'identité visuelle, l'atmosphère et l'impact de l'œuvre d'art de référence : un panneau "STOP" détourné, mêlant art urbain africain, cybernétique, structures de circuits imprimés et esthétique glitch/liquide.

---

## 1. Identité Visuelle & Philosophie du Design

L'esthétique globale repose sur le contraste saisissant entre l'**organique/traditionnel** et le **numérique/futuriste** (Afrofuturisme Cybernétique), ancré dans un environnement urbain.

### Règles Fondamentales de l'Expérience Utilisateur (UX) :
* **Contraste Brut & Impact Massif :** Pas de demi-teintes subtiles ou de dégradés doux. Les transitions entre les blocs doivent imiter le découpage net d'un pochoir de street art ou les contours d'un panneau de signalisation.
* **Dualité Technologique :** Coexistence d'éléments cybernétiques stricts (lignes de circuits imprimés à 90°/45°, micro-puces, pixels parfaits) et de formes liquides/destructurées (motifs de coulures de peinture, érosion urbaine).
* **Immersion Urbaine :** Le site doit donner l'impression de naviguer sur une œuvre d'art public numérique, pas sur un site SaaS classique.

---

## 2. Palette de Couleurs Spécifique (Strict-Hex)

La palette est ultra-restreinte, fidèle à la sérigraphie et au pochoir à trois tons de l'image.

| Élément / Rôle | Code Hex | Description Visuelle & Utilisation |
| :--- | :--- | :--- |
| **Bleu Cobalt Urbain** | `#0B46B9` | La couleur maîtresse (dominante à 60%). Teinte saturée des panneaux de signalisation. Utilisée pour les arrière-plans principaux, les overlays massifs et les grands blocs d'identité. |
| **Bleu Nuit Profond** | `#041A4E` | Utilisé pour les ombres portées nettes, les textures de fond imbriquées, et les lignes de démarcation du visage/des cheveux (contrastes sombres). |
| **Blanc Signalétique Pur** | `#FFFFFF` | Utilisé pour les typographies majeures (le texte doit "frapper" l'œil), les tracés de circuits imprimés et les rehauts de lumière nets (lignes blanches de la silhouette). |
| **Gris Béton Urbain (Fond)** | `#E2E8F0` | Couleur optionnelle de structure extérieure ou d'arrière-plan global, simulant le béton d'arrière-plan ou l'acier galvanisé des poteaux de rue. |

---

## 3. Typographie Spécifique

L'impact typographique doit être instantané, évoquant l'affichage urbain et la signalisation routière.

### Titres Majeurs (H1, H2, Noms de Sections)
* **Police :** Une sans-serif ultra-géométrique, bold, condensée et massive. (Exemples Google Fonts : `Anton`, `Impact`, `Oswald` ou `Barlow Condensed` en Black).
* **Style :** Majuscules obligatoires (`text-transform: uppercase`), espacement des lettres légèrement resserré (`letter-spacing: -0.05em`) pour mimer le texte **"STOP"** de l'image.
* **Couleur :** Blanc Pur (`#FFFFFF`) sur fond Bleu Cobalt.

### Corps de Texte & Données Techniques
* **Police :** Une police monospace ou sans-serif technique très lisible (Exemples : `JetBrains Mono`, `Space Mono`, ou `Roboto Mono`).
* **Style :** Épuré, évoquant le code source ou la documentation d'une puce électronique.

---

## 4. Effets Visuels Clés (À Implémenter en CSS/SVG)

Pour obtenir *exactement* le même effet, le site doit intégrer quatre modules d'effets graphiques précis :

### A. L'Effet Octogonal "Sign" (Layout & Clip-path)
L'élément principal du portfolio (l'en-tête ou le conteneur du profil) ne doit pas être un rectangle ou un cercle standard, mais un **octogone régulier**.

```css
.hero-container {
  clip-path: polygon(30% 0%, 70% 0%, 100% 30%, 100% 70%, 70% 100%, 30% 100%, 0% 70%, 0% 30%);
  background-color: #0B46B9;
  border: 12px solid #FFFFFF; /* Rappelle la bordure blanche du panneau */
}
```

### B. Les Lignes de Circuits Imprimés (Cybernetic Traces)

* **Visuel :** Des lignes blanches fines interconnectées à angles droits (90°) et à 45°, se terminant par des cercles pleins ou menant à un carré noir central (la puce/processeur oculaire).
* **Technique :** Intégration de tracés SVG en arrière-plan des sections ou en overlay sur la photo du profil. Ces lignes doivent s'animer subtilement au survol (effet de courant électrique qui traverse le tracé via un `stroke-dashoffset`).

### C. Le Glitch Pixelisé (Digital Decay)

* **Visuel :** Sur le côté gauche de la chevelure/silhouette, les formes organiques se décomposent en carrés de tailles variées (pixels informatiques).
* **Application Web :** Les transitions entre les sections ou les contours de certaines cartes de projets ne doivent pas être lisses, mais adopter un effet d'escalier ou de "pixel-art blocks" en CSS (`image-rendering: pixelated` ou masques SVG de blocs carrés).

### D. L'Effet de Coulure Liquide (Melting Street Art)

* **Visuel :** Le bas de la silhouette se transforme en une structure liquide qui coule vers le bas, s'affranchissant des limites du panneau.
* **Application Web :** Le pied de page (Footer) ou la transition du Hero banner vers les sections inférieures doit utiliser un séparateur de shape (Shape Divider) SVG imitant des coulures de peinture ou des draperies fluides de couleur Bleu Cobalt et Blanc.

---

## 5. Structure du Portfolio & Règles d'Intégration

### Section 1 : Le Hero (L'Impact Panneau)

* **Composant Central :** Un énorme octogone (`.hero-container`) centré. À l'intérieur, une photo du développeur traitée en **Bichromie/Trichromie** (Bleu Cobalt, Bleu Nuit, Blanc) via un filtre CSS de type SVG duotone.
* **Détail Cyber :** Un overlay SVG place la puce carrée sur un œil ou une zone clé, avec les circuits imprimés qui se déploient sur le reste du visage.
* **Texte :** Un grand titre en arrière-plan ou au-dessus de l'octogone, écrit en lettres capitales blanches massives (ex: "CODE", "TECH LEAD").

### Section 2 : Les Projets (Les Cartes "Circuits")

* Les cartes de projet utilisent un fond Bleu Nuit (`#041A4E`).
* Les bordures s'activent au survol sous forme de lignes de circuits imprimés qui s'allument en Blanc Pur.
* Les badges de technologies (React, NestJS, etc.) ont un look de puces électroniques ou de mini-blocs de pixels.

### Section 3 : À Propos (L'Hybride Organique/Pixel)

* Mise en page asymétrique. Un côté présente du texte technique très structuré (Monospace).
* L'autre côté affiche un artéfact visuel (comme le motif de cheveux afro pixelisé sur la gauche) qui réagit au défilement (Scroll Interactivity), où les pixels se dispersent ou se rassemblent.

---

## 6. Instructions Précises pour l'IA de Redesign (Prompt Système)

Copiez-collez ce bloc pour configurer l'agent chargé du code :

> "Agis en tant que développeur Creative Front-End de haut niveau. Redessine mon portfolio en appliquant strictement la charte 'Cyber-Urban Afrofuturism'. Tu dois respecter une palette trichrome exclusive : Bleu Cobalt (#0B46B9), Bleu Nuit (#041A4E) et Blanc (#FFFFFF). Utilise une typographie de signalisation routière (ex: Anton ou Oswald) pour les titres en majuscules. Bannis les arrondis standards (border-radius classiques) : utilise des formes octogonales complexes via clip-path. Intègre des tracés de circuits imprimés en SVG et des cassures de pixels asymétriques pour les bordures. Le bas des sections majeures doit se terminer par un effet de coulure liquide ou de peinture qui dégouline. Le résultat final doit être brutal, technologique et artistique, sans compromis corporate poli."
