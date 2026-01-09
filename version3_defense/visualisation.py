import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.animation import FuncAnimation
import numpy as np


def configurer_graphique(ax, titre="Forêt"):
    """Configure le style du graphique (couleurs, légende, etc.)"""
    # 1. Couleurs : 0=Blanc, 1=Vert, 2=Rouge, 3=Noir
    liste_couleurs = ['white', 'green', 'red', 'black']
    cmap_perso = colors.ListedColormap(liste_couleurs)

    # 2. Bornes pour les valeurs 0, 1, 2, 3
    bounds = [-0.5, 0.5, 1.5, 2.5, 3.5]
    norm = colors.BoundaryNorm(bounds, cmap_perso.N)

    # 3. Configuration des axes
    ax.set_title(titre, fontsize=14)
    ax.axis('off')

    return cmap_perso, norm


def afficher_foret(foret, titre="Forêt"):
    """Affiche une image statique (fonction utilitaire)."""
    fig, ax = plt.subplots(figsize=(8, 8))
    cmap, norm = configurer_graphique(ax, titre)

    im = ax.imshow(foret, interpolation='nearest', cmap=cmap, norm=norm)

    cbar = plt.colorbar(im, ticks=[0, 1, 2, 3], shrink=0.8)
    cbar.ax.set_yticklabels(['Vide', 'Arbre', 'Feu', 'Cendre'])
    plt.tight_layout()
    plt.show()


def animer_feu(foret_initiale, fonction_update):
    """
    Lance une animation pas-à-pas de la propagation.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    cmap, norm = configurer_graphique(ax, "Simulation de propagation du feu")

    # Image initiale
    im = ax.imshow(foret_initiale, interpolation='nearest', cmap=cmap, norm=norm)

    cbar = plt.colorbar(im, ticks=[0, 1, 2, 3], shrink=0.8)
    cbar.ax.set_yticklabels(['Vide', 'Arbre', 'Feu', 'Cendre'])

    def generateur_etapes():
        foret = foret_initiale.copy()
        actif = True
        while actif:
            yield foret
            foret, actif = fonction_update(foret)
        yield foret  # Dernier état

    def update_frame(foret_etat):
        im.set_data(foret_etat)
        return [im]

    ani = FuncAnimation(fig, update_frame, frames=generateur_etapes,
                        interval=50, blit=False, repeat=False, save_count=200)
    plt.show()


def afficher_courbe_percolation(densites, probabilites):
    """Affiche la courbe de transition de phase."""
    plt.figure(figsize=(10, 6))

    # Tracer la courbe obtenue par simulation
    plt.plot(densites, probabilites, 'o-', color='royalblue', linewidth=2, label='Simulation Monte Carlo')

    # Tracer la ligne théorique verticale
    plt.axvline(x=0.5927, color='crimson', linestyle='--', linewidth=2, label='Seuil théorique (0.5927)')

    # Zone de transition grisée pour l'esthétique
    plt.axvspan(0.55, 0.65, alpha=0.2, color='gray', label='Zone de transition')

    plt.grid(True, linestyle=':', alpha=0.7)
    plt.xlabel("Densité initiale d'arbres (p)", fontsize=12)
    plt.ylabel("Probabilité de percolation", fontsize=12)
    plt.title("Transition de Phase - Percolation de Site 2D", fontsize=14)
    plt.legend(fontsize=10)
    plt.show()