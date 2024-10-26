
# Simulation d'un Système de Réservation de Vols - Projet Python

## Présentation

Ce projet est un programme Python de Simulation d'un Système de Réservation de Vols en ligne de commande où les utilisateurs peuvent réserver
ou annuler des sièges sur différents vols, avec la gestion de la disponibilité des sièges et la
persistance des informations dans un fichier

##  Prérequis

- Python 3.x installé sur votre machine. Vous pouvez la vérifier à l'aide de la commande :
    ```bash
    python3 --version
    ```
- Un environnement de développement python

## Installation

1. Clonez le dépôt ou télécharger directement le fichier :
    ```bash
   git clone https://github.com/...
   ```
2. Aller dans le répertoire où se trouve le projet :
    ```bash
    cd projet
   ```
3. Créez un environnement virtuel :
   ```bash
   python -m venv myvenv
   
   source myvenv/bin/activate # Sur Linux/Mac
   myvenv\Scripts\activate # Sur Windows
   ```
## Utilisation

Pour exécuter le programme, utilisez la commande :
```bash
python main.py
```

Pour exécuter le test unitaire, utilisez la commande :
```bash
python -m unittest ./test/fbs_test.py
```