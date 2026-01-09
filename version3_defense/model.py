import numpy as np

VIDE = 0
ARBRE = 1
FEU = 2
CENDRE = 3

def generer_foret(n, densite):
    """Génère la forêt de base."""
    foret = np.zeros((n, n), dtype=int)
    arbres = np.random.random((n, n)) < densite
    foret[arbres] = ARBRE
    return foret

def appliquer_coupe_feu_aleatoire(foret, pourcentage_coupe):
    """Retire X% des arbres existants au hasard."""
    foret_modifiee = foret.copy()
    masque_arbres = (foret_modifiee == ARBRE)
    
    # Parmi les arbres, on en choisit certains à supprimer (Devenir VIDE)
    nb_arbres = np.sum(masque_arbres)
    nb_a_couper = int(nb_arbres * pourcentage_coupe)
    
    # Astuce pour choisir aléatoirement sans boucle
    indices = np.where(masque_arbres) # Liste des (x, y) des arbres
    # On choisit des indices au hasard
    choix = np.random.choice(len(indices[0]), nb_a_couper, replace=False)
    
    # On vide les arbres choisis
    foret_modifiee[indices[0][choix], indices[1][choix]] = VIDE
    return foret_modifiee

def appliquer_coupe_feu_vertical(foret, largeur):
    """Crée une tranchée verticale vide au milieu."""
    foret_modifiee = foret.copy()
    n = foret.shape[1]
    centre = n // 2
    # On vide une bande verticale
    foret_modifiee[:, centre : centre + largeur] = VIDE
    return foret_modifiee

def allumer_feu(foret):
    """Met le feu à gauche (Standard)."""
    foret[0, :] = np.where(foret[0, :] == ARBRE, FEU, VIDE)
    return foret

def etape_propagation(foret):
    """Propagation standard (Isotrope V1)."""
    future_foret = foret.copy()
    masque_feu = (foret == FEU)
    if not np.any(masque_feu): return future_foret, False

    future_foret[masque_feu] = CENDRE
    masque_arbres = (foret == ARBRE)
    prop = np.zeros_like(foret, dtype=bool)

    prop[1:, :] |= (masque_feu[:-1, :] & masque_arbres[1:, :]) # Bas
    prop[:-1, :] |= (masque_feu[1:, :] & masque_arbres[:-1, :]) # Haut
    prop[:, 1:] |= (masque_feu[:, :-1] & masque_arbres[:, 1:]) # Droite
    prop[:, :-1] |= (masque_feu[:, 1:] & masque_arbres[:, :-1]) # Gauche

    future_foret[prop] = FEU
    return future_foret, True