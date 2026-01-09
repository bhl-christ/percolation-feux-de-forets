import numpy as np

# Constantes d'état (pour rendre le code lisible)
VIDE = 0
ARBRE = 1
FEU = 2
CENDRE = 3

def generer_foret(n, densite):
    """
    Génère une grille n x n.
    0: Vide, 1: Arbre.
    """
    foret = np.zeros((n, n), dtype=int)
    # Masque aléatoire : True si un nombre aléatoire < densite
    arbres = np.random.random((n, n)) < densite
    foret[arbres] = ARBRE
    return foret

def allumer_feu(foret):
    """Met le feu à toute la première ligne."""
    # On met le feu (2) là où il y a des arbres (1) sur la ligne 0
    foret[0, :] = np.where(foret[0, :] == ARBRE, FEU, VIDE)
    return foret

def etape_propagation(foret):
    """
    Calcule l'état t+1 de la forêt.
    Utilise numpy pour éviter les boucles lentes.
    Retourne : (nouvelle_foret, feu_actif_bool)
    """
    future_foret = foret.copy()
    masque_feu = (foret == FEU)
    
    # Si plus de feu, on arrête
    if not np.any(masque_feu):
        return future_foret, False

    # 1. Le feu actuel devient cendre
    future_foret[masque_feu] = CENDRE

    # 2. Propagation aux 4 voisins
    masque_arbres = (foret == ARBRE)
    propagation = np.zeros_like(foret, dtype=bool)

    # Décalages (Slicing) pour voir les voisins sans boucle
    # Vers le BAS
    propagation[1:, :] |= (masque_feu[:-1, :] & masque_arbres[1:, :])
    # Vers le HAUT
    propagation[:-1, :] |= (masque_feu[1:, :] & masque_arbres[:-1, :])
    # Vers la DROITE
    propagation[:, 1:] |= (masque_feu[:, :-1] & masque_arbres[:, 1:])
    # Vers la GAUCHE
    propagation[:, :-1] |= (masque_feu[:, 1:] & masque_arbres[:, :-1])

    # Appliquer le nouveau feu
    future_foret[propagation] = FEU
    
    return future_foret, True