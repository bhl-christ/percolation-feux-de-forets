import numpy as np
import model


def simuler_feu_complet(n, densite):
    """
    Lance une simulation jusqu'à extinction.
    Retourne : (a_percole (bool), foret_finale (array))
    """
    # 1. Init
    foret = model.generer_foret(n, densite)
    foret = model.allumer_feu(foret)

    # 2. Boucle de propagation
    feu_actif = True
    while feu_actif:
        foret, feu_actif = model.etape_propagation(foret)

    # 3. Vérification Percolation
    # Y a-t-il du feu (2) ou des cendres (3) sur la dernière ligne ?
    derniere_ligne = foret[-1, :]
    a_percole = np.any((derniere_ligne == model.FEU) | (derniere_ligne == model.CENDRE))

    return a_percole, foret


def etude_percolation(n, nb_simulations=50):
    """
    Fait varier la densité de 0 à 1 et calcule la probabilité de percolation.
    """
    densites = np.linspace(0, 1, 50)
    probabilites = []

    print(f"Lancement de l'étude statistique ({nb_simulations} sims par point)...")

    for d in densites:
        succes = 0
        for _ in range(nb_simulations):
            percole, _ = simuler_feu_complet(n, d)
            if percole:
                succes += 1
        probabilites.append(succes / nb_simulations)

    return densites, probabilites


def trouver_seuil_critique(densites, probabilites):
    """
    Cherche la valeur de densité p pour laquelle la probabilité de percolation est de 0.5 (50%).
    Utilise une interpolation linéaire entre les deux points encadrant 0.5.
    """
    x = np.array(densites)
    y = np.array(probabilites)

    # On cherche les indices où la probabilité dépasse ou est égale 0.5
    indices_sup = np.where(y >= 0.5)[0]

    # Si la courbe ne monte jamais (ex: max 0.1) ou commence trop haut
    if len(indices_sup) == 0 or indices_sup[0] == 0:
        return None

        # idx est l'index du premier point au-dessus de 0.5
    idx = indices_sup[0]

    # On récupère les coordonnées du point avant (x1, y1) et après (x2, y2)
    x1, y1 = x[idx - 1], y[idx - 1]
    x2, y2 = x[idx], y[idx]

    # Formule d'interpolation linéaire pour trouver x quand y = 0.5
    # x = x1 + (target_y - y1) * (pente_inverse)
    if y2 == y1: return x1  # Évite la division par zéro

    p_critique = x1 + (0.5 - y1) * (x2 - x1) / (y2 - y1)

    return p_critique