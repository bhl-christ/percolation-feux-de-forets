# Modélisation Mathématique : La Percolation et les Feux de Forêt

**Auteurs :** Semih ASLAN, Rodanim GANABA, Christ BAHOUASSILA
**Cadre :** Cours de Modélisation Mathématique  
**Langage :** Python 3 (Numpy, Matplotlib)

---

## Présentation du Projet

Ce projet étudie le phénomène de **percolation de site** appliqué à la propagation des feux de forêt. L'objectif est de déterminer expérimentalement le **seuil critique de percolation** ($p_c$) au-delà duquel un feu traverse intégralement une forêt.

Nous avons développé deux versions du modèle pour illustrer une démarche scientifique progressive : de la validation théorique à la modélisation d'une contrainte physique (le vent).

### Architecture du Code
Le projet est structuré de manière modulaire :
* `model.py` : Logique matricielle (Numpy) et règles de propagation.
* `simulation.py` : Moteur statistique (Monte Carlo) et calculs d'interpolation.
* `visualisation.py` : Gestion des graphiques et animations (Matplotlib).

---

## Installation et Lancement

### Prérequis
Installer les dépendances nécessaires :
```bash
pip install -r requirements.txt
``