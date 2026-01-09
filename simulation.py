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