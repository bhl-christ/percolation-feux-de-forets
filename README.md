# Modélisation Mathématique : La Percolation et les Feux de Forêt

**Auteurs :** Semih ASLAN, Rodanim GANABA, Christ BAHOUASSILA
**Cadre :** Cours de Modélisation Mathématique
**Langage :** Python 3 (Numpy, Matplotlib)

---

## Présentation du Projet

Ce projet étudie le phénomène de **percolation de site** appliqué à la propagation des feux de forêt. L'objectif est de déterminer expérimentalement le **seuil critique de percolation** ($p_c$) au-delà duquel un feu traverse intégralement une forêt.

Nous avons développé trois versions du modèle pour illustrer une démarche scientifique progressive : de la validation théorique à la modélisation de contraintes physiques (le vent) et de stratégies d'ingénierie (coupe-feu).

---

## Architecture du Projet

Le projet est structuré en trois dossiers correspondants aux évolutions du modèle :

### 1. version1 (Modèle Classique Isotrope)
Il s'agit de la mise en œuvre standard de la percolation de site.
* **Propagation :** Le feu se propage dans les 4 directions (Nord, Sud, Est, Ouest) de manière uniforme.
* **Objectif :** Vérifier le seuil théorique de percolation ($p_c \approx 0.59$) via une méthode de Monte Carlo.

### 2. version2_vent (Modèle avec Vent)
Introduction d'une contrainte physique : le vent.
* **Propagation :** Un "Vent du Nord" empêche le feu de remonter vers le haut. Le feu ne peut se propager que vers le Bas, la Gauche et la Droite.
* **Objectif :** Étudier l'impact de l'anisotropie sur le seuil critique.

### 3. version3_defense (Stratégies de Défense)
Comparaison de méthodes pour stopper un feu dans une forêt dense.
* **Stratégies comparées :**
    * **Coupe Aléatoire :** On retire un pourcentage d'arbres au hasard.
    * **Tranchée Coupe-Feu :** On retire une bande verticale représentant la même surface.
* **Objectif :** Déterminer quelle stratégie minimise la surface brûlée.

### Fichiers Communs
Dans chaque dossier, le code est organisé de manière modulaire :
* `main.py` : Point d'entrée pour lancer les simulations et les menus.
* `model.py` : Logique matricielle (Numpy) et règles de propagation.
* `simulation.py` : Moteur statistique et calculs de seuils.
* `visualisation.py` : Gestion des graphiques et animations.

---

## Installation

### Prérequis
Installer les dépendances nécessaires listées dans le fichier `requirements.txt` :

```bash
pip install -r requirements.txt


## Utilisation

Chaque version possède son propre fichier principal.

### Lancer la Version 1
```bash
cd version1
python main.py

### Lancer la Version 2
cd version2_vent
python main.py

### Lancer la Version 3
cd version3_defense
python main.py

Lance automatiquement une comparaison entre la coupe aléatoire et la tranchée sur une forêt dense, puis affiche les résultats et une animation.
```

## Résultats Attendus
Version 1 : Le seuil critique expérimental se situe autour de 0.59.

Version 2 : Avec le vent du Nord, le seuil augmente (environ 0.62 - 0.65), car le feu a moins de possibilités de contournement.

Version 3 : La tranchée coupe-feu est généralement plus efficace pour bloquer la propagation qu'une coupe aléatoire de même surface.