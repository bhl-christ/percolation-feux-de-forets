import numpy as np

VIDE = 0
ARBRE = 1
FEU = 2
CENDRE = 3


def generer_foret(n, densite):
    """Génère une forêt uniforme (Classique)."""
    foret = np.zeros((n, n), dtype=int)
    arbres = np.random.random((n, n)) < densite
    foret[arbres] = ARBRE
    return foret


def generer_foret_gradient(n, d_haut, d_bas):
    """
    Génère une forêt avec une densité variable (Gradient).
    d_haut : densité en haut de la grille (ligne 0)
    d_bas : densité en bas de la grille (ligne n-1)
    """
    foret = np.zeros((n, n), dtype=int)
    # On crée une matrice de probabilités qui change ligne par ligne
    gradient = np.linspace(d_haut, d_bas, n).reshape(n, 1)
    # On étend ce vecteur colonne à toute la matrice
    proba_matrice = np.repeat(gradient, n, axis=1)

    arbres = np.random.random((n, n)) < proba_matrice
    foret[arbres] = ARBRE
    return foret


def appliquer_coupe_feu_vertical(foret, largeur):
    """Crée une tranchée verticale vide au milieu."""
    foret_modifiee = foret.copy()
    n = foret.shape[1]
    centre = n // 2
    demi_l = largeur // 2
    foret_modifiee[:, centre - demi_l: centre + demi_l] = VIDE
    return foret_modifiee


def allumer_feu(foret):
    """Met le feu à toute la ligne du haut."""
    foret[0, :] = np.where(foret[0, :] == ARBRE, FEU, VIDE)
    return foret


def etape_propagation(foret, vent_nord=False, inflammabilite=1.0):
    """
    Propagation avancée avec Vent et Humidité.
    - inflammabilite (0.0 à 1.0) : Probabilité qu'un arbre voisin prenne feu.
      Si < 1.0, cela simule l'humidité ou un bois difficile à brûler.
    """
    future_foret = foret.copy()
    masque_feu = (foret == FEU)

    if not np.any(masque_feu):
        return future_foret, False

    future_foret[masque_feu] = CENDRE
    masque_arbres = (foret == ARBRE)

    # Masque des zones potentiellement touchées (voisins du feu)
    propagation_potentielle = np.zeros_like(foret, dtype=bool)

    # 1. Propagation géométrique (Qui touche le feu ?)
    propagation_potentielle[1:, :] |= masque_feu[:-1, :]  # Bas
    propagation_potentielle[:, 1:] |= masque_feu[:, :-1]  # Droite
    propagation_potentielle[:, :-1] |= masque_feu[:, 1:]  # Gauche

    if not vent_nord:
        propagation_potentielle[:-1, :] |= masque_feu[1:, :]  # Haut

    # 2. Intersection avec les arbres existants
    arbres_touches = (propagation_potentielle & masque_arbres)

    # 3. Application de l'INFLAMMABILITÉ (Probabilité)
    # Même si l'arbre est touché, il ne brûle qu'avec une probabilité p
    if inflammabilite < 1.0:
        # On génère un nombre aléatoire pour chaque arbre touché
        alea = np.random.random(foret.shape)
        # Il brûle si : Il est touché ET (nb_alea < inflammabilite)
        arbres_qui_brulent = arbres_touches & (alea < inflammabilite)
    else:
        arbres_qui_brulent = arbres_touches

    future_foret[arbres_qui_brulent] = FEU

    # On retourne True si de nouveaux feux sont apparus
    feu_actif = np.any(arbres_qui_brulent)
    return future_foret, feu_actif