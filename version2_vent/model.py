import numpy as np

VIDE = 0
ARBRE = 1
FEU = 2
CENDRE = 3

def generer_foret(n, densite):
    """Génère une grille n x n."""
    foret = np.zeros((n, n), dtype=int)
    arbres = np.random.random((n, n)) < densite
    foret[arbres] = ARBRE
    return foret

def allumer_feu(foret):
    """Met le feu à toute la première ligne."""
    foret[0, :] = np.where(foret[0, :] == ARBRE, FEU, VIDE)
    return foret

def etape_propagation(foret, vent_nord=False):
    """
    Calcule l'état t+1.
    Si vent_nord est True, le feu ne se propage PAS vers le haut.
    """
    future_foret = foret.copy()
    masque_feu = (foret == FEU)
    
    if not np.any(masque_feu):
        return future_foret, False

    future_foret[masque_feu] = CENDRE
    masque_arbres = (foret == ARBRE)
    propagation = np.zeros_like(foret, dtype=bool)

    # 1. Vers le BAS (Toujours)
    propagation[1:, :] |= (masque_feu[:-1, :] & masque_arbres[1:, :])
    
    # 2. Vers la DROITE (Toujours)
    propagation[:, 1:] |= (masque_feu[:, :-1] & masque_arbres[:, 1:])
    
    # 3. Vers la GAUCHE (Toujours)
    propagation[:, :-1] |= (masque_feu[:, 1:] & masque_arbres[:, :-1])

    # 4. Vers le HAUT (Conditionnel : seulement si pas de vent)
    if not vent_nord:
        propagation[:-1, :] |= (masque_feu[1:, :] & masque_arbres[:-1, :])

    future_foret[propagation] = FEU
    
    return future_foret, True