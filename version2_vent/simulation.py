import numpy as np
import model

def simuler_feu_complet(n, densite, vent_nord=False):
    """Simule jusqu'à extinction avec option vent."""
    foret = model.generer_foret(n, densite)
    foret = model.allumer_feu(foret)
    
    feu_actif = True
    while feu_actif:
        foret, feu_actif = model.etape_propagation(foret, vent_nord=vent_nord)
    
    derniere_ligne = foret[-1, :]
    a_percole = np.any((derniere_ligne == model.FEU) | (derniere_ligne == model.CENDRE))
    
    return a_percole, foret

def etude_percolation(n, nb_simulations=50, vent_nord=False):
    """Calcule la courbe de probabilité."""
    densites = np.linspace(0, 1, 50)
    probabilites = []
    
    # Petit message de statut
    mode = "AVEC VENT" if vent_nord else "SANS VENT"
    print(f"   -> Calcul série {mode} ({nb_simulations} sims/point)...")
    
    for d in densites:
        succes = 0
        for _ in range(nb_simulations):
            percole, _ = simuler_feu_complet(n, d, vent_nord=vent_nord)
            if percole:
                succes += 1
        probabilites.append(succes / nb_simulations)
        
    return densites, probabilites

def trouver_seuil_critique(densites, probabilites):
    """Interpolation linéaire pour trouver p_c à 0.5"""
    x = np.array(densites)
    y = np.array(probabilites)
    indices_sup = np.where(y >= 0.5)[0]
    
    if len(indices_sup) == 0 or indices_sup[0] == 0:
        return None 
    
    idx = indices_sup[0]
    x1, y1 = x[idx-1], y[idx-1]
    x2, y2 = x[idx], y[idx]
    
    if y2 == y1: return x1
    return x1 + (0.5 - y1) * (x2 - x1) / (y2 - y1)