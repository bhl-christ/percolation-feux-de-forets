"""
PROJET : Modélisation Mathématique - Percolation (Feux de Forêt)
VERSION : 3 (OPTIMISATION & INGÉNIERIE (Stratégies de Coupe-Feu)
AUTEURS : Semih ASLAN, Rodanim GANABA, Christ BAHOUASSILA
Hypothèse : Une coupe géométrique (tranchée) est-elle meilleure qu'une coupe aléatoire ?
"""
import model
import simulation
import visualisation
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("--- VERSION 3 : STRATÉGIES DE DÉFENSE ---")
    print("Comparaison : Éclaircissement Aléatoire vs Tranchée Verticale")
    
    # Paramètres : Une forêt TRÈS dense (0.80) qui brûlerait à 100% normalement
    n = 100
    d = 0.6
    
    print(f"\nGénération d'une forêt dense (d={d})...")
    foret_ref = model.generer_foret(n, d)
    
    # --- Visualisation des 2 stratégies ---
    print("Préparation des forêts modifiées...")
    
    # Stratégie 1 : Enlever 5% des arbres au hasard
    foret_alea = model.appliquer_coupe_feu_aleatoire(foret_ref, 0.05)
    
    # Stratégie 2 : Tranchée de 5% de la largeur
    largeur = max(1, int(n * 0.05))
    foret_tran = model.appliquer_coupe_feu_vertical(foret_ref, largeur)
    
    print("\nLancement des simulations comparatives...")
    
    degats_alea = simulation.simuler_feu_avec_stats(foret_alea)
    degats_tran = simulation.simuler_feu_avec_stats(foret_tran)
    
    print(f"\n--- RÉSULTATS (Pour 5% d'arbres coupés préventivement) ---")
    print(f"1. Coupe Aléatoire : {degats_alea:.2f}% de la forêt restante a brûlé.")
    print(f"2. Tranchée Coupe-Feu : {degats_tran:.2f}% de la forêt restante a brûlé.")
    
    if degats_tran < degats_alea:
        print(">> CONCLUSION : La tranchée est plus efficace (stoppe la propagation).")
    else:
        print(">> CONCLUSION : L'aléatoire est plus efficace (réduit la densité globale).")
        
    # Petit bonus visuel : montrer la forêt à tranchée
    print("\nAffichage de la stratégie Tranchée...")
    foret_feu = model.allumer_feu(foret_tran)
    visualisation.animer_feu(foret_feu, model.etape_propagation)

if __name__ == "__main__":
    main()