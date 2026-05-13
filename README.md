
# Signalhunt
Signalhunt est un outil d'OSINT (Open Source Intelligence) moderne qui combine la puissance de l'investigation numérique avec une interface web intuitive. Fini les lignes de commande complexes : centralisez vos recherches et visualisez vos données en quelques clics.

## Installation & Deployment 
Suivez ces étapes pour installer et lancer SignalHunt sur votre machine locale.

1. Clonage du projet

```bash
git clone git@github.com:norvoxx/SignalHunt.git
cd SignalHunt
```
2. Configuration du Backend (Python)
```bash
# Création de l'environnement virtuel
python -m venv .venv

# Activation (Linux/macOS)
source .venv/bin/activate

# Installation des dépendances
pip install -r requirements.txt

# Lancement API 
cd SignalHunt
uvicorn main:app --reload
```
3. Configuration du Frontend (React)

```bash
cd web/
npm install
npm run dev 
```

## Sources & Plateformes
    
Cette section répertorie les capacités de SignalHunt pour chaque plateforme. 
L'outil utilise différentes techniques (Scraping, APIs officielles, ou requêtes de statut)pour récupérer des informations selon les entrées fournies.

| Website   | operational | Usenrame | Email | key |
|:----------|:-----------:|:--------:|:-----:|----:|
| Github    |      ✅      |    ✅     |   ❌   |   ❌ |
| Instagram |      ✅      |    ✅     |   ❌   |   ❌ |
| Pinterest |      ✅      |    ✅     |   ❌   |   ❌ |
| Reddit    |      ✅      |    ✅     |   ❌   |   ❌ |
| tiktok    |      ✅      |    ✅     |   ❌   |   ❌ |

## Évolution du Projet
SignalHunt n'est pas un outil figé. Mon objectif est de le faire évoluer continuellement pour en faire une suite OSINT complète et indispensable. 
Le projet a pour but de s'enrichir régulièrement de nouveaux outils et de fonctionnalités innovantes pour faciliter vos investigations.

Ce qui arrive prochainement :
 - Multi-Sources : Intégration de nouvelles plateformes (LinkedIn, Twitter/X, Snapchat).
 - Visualisation de Graphes : Créer des liens visuels entre les différents comptes trouvés.
 - analyse approfondie des différents profils

> [!TIP]
> ###  Un projet en pleine croissance
> **SignalHunt** est conçu pour devenir une plateforme d'OSINT de référence. Mon ambition est de fournir des outils de plus en plus puissants et variés au fil des mises à jour. 
> 
> Vous avez une idée d'outil intéressant ? Contribuez à l'évolution du projet en ouvrant une **Issue** !