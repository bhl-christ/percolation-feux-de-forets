import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np

def afficher_foret(foret, titre="Forêt"):
    """
    Affiche la grille avec les couleurs spécifiques demandées :
    0: Vide (white), 1: Arbre (green), 2: Feu (red), 3: Cendre (black)
    """
    plt.figure(figsize=(8, 8))

    # 1. Définition des couleurs personnalisées 
    liste_couleurs = ['white', 'green', 'red', 'black']
    cmap_perso = colors.ListedColormap(liste_couleurs)

    # 2. Définition des frontières (Norme) 
    # Pour être sûr que l'entier 0 tombe sur 'white', 1 sur 'green', etc.,
    # on définit des bornes entre les entiers : [-0.5, 0.5, 1.5, 2.5, 3.5]
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
    norm = colors.BoundaryNorm(bounds, cmap_perso.N)

    #  3. Affichage 
    # On passe 'cmap' et 'norm' à imshow
    im = plt.imshow(foret, interpolation='nearest', cmap=cmap_perso, norm=norm)

    #  4. Barre de légende ajustée 
    # On place les ticks exactement sur 0, 1, 2, 3
    cbar = plt.colorbar(im, ticks=[0, 1, 2, 3], shrink=0.8)
    cbar.ax.set_yticklabels(['Vide (0)', 'Arbre (1)', 'Feu (2)', 'Cendre (3)'])

    plt.title(titre, fontsize=14)
    plt.axis('off') # On cache les axes chiffrés
    plt.tight_layout()
    plt.show()

def afficher_courbe_percolation(densites, probabilites):
    """Affiche la courbe de transition de phase."""
    plt.figure(figsize=(10, 6))
    plt.plot(densites, probabilites, 'o-', color='royalblue', linewidth=2, label='Simulation Monte Carlo')
    
    # Ligne théorique verticale
    plt.axvline(x=0.5927, color='crimson', linestyle='--', linewidth=2, label='Seuil théorique (0.5927)')
    
    # Ajout d'une zone grisée pour montrer la transition brutale
    plt.axvspan(0.55, 0.65, alpha=0.2, color='gray', label='Zone de transition')

    plt.grid(True, linestyle=':', alpha=0.7)
    plt.xlabel("Densité initiale d'arbres (p)", fontsize=12)
    plt.ylabel("Probabilité de percolation", fontsize=12)
    plt.title("Transition de Phase - Percolation de Site 2D", fontsize=14)
    plt.legend(fontsize=10)
    plt.show()