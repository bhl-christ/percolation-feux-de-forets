import numpy as np
import model

def simuler_feu_avec_stats(foret_depart):
    """Simule le feu et retourne le % d'arbres brûlés."""
    foret = foret_depart.copy()
    foret = model.allumer_feu(foret)
    
    # Compter les arbres AVANT le feu
    nb_arbres_initial = np.sum(foret == model.ARBRE) + np.sum(foret == model.FEU)
    if nb_arbres_initial == 0: return 0.0 # Évite division par zéro
    
    actif = True
    while actif:
        foret, actif = model.etape_propagation(foret)
        
    # Compter les cendres (arbres brûlés)
    nb_brules = np.sum(foret == model.CENDRE) + np.sum(foret == model.FEU)
    
    return (nb_brules / nb_arbres_initial) * 100 # Pourcentage de destruction

def comparer_strategies(n, densite):
    """Compare Coupe Aléatoire vs Tranchée Verticale."""
    # 1. Forêt dense de base (ex: 0.8, très inflammable)
    foret_base = model.generer_foret(n, densite)
    
    # STRATÉGIE A : On coupe 10% des arbres au hasard
    foret_A = model.appliquer_coupe_feu_aleatoire(foret_base, 0.10)
    degats_A = simuler_feu_avec_stats(foret_A)
    
    # STRATÉGIE B : On fait une tranchée (équivalent à ~10% de surface)
    largeur = int(n * 0.10)
    foret_B = model.appliquer_coupe_feu_vertical(foret_base, largeur)
    degats_B = simuler_feu_avec_stats(foret_B)
    
    return degats_A, degats_B