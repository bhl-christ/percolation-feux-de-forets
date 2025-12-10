from numpy import zeros
from random import randint
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.animation import FuncAnimation


class FeuForet:
    """
    Mapping des couleurs:
        0: sans arbre
        1: arbre
        2: arbre en feu
        3: arbre brûlé
    """
    _cmap = colors.ListedColormap(['white', 'green', 'red', 'black'])
    _bounds = [0, 1, 2, 3, 4]
    _norm = colors.BoundaryNorm(_bounds, _cmap.N)

    def __init__(self, taille=512, densite=0.6, temps=300):
        self._n = taille
        self._foret = zeros((self._n, self._n))

        self.fig, self.ax = plt.subplots(figsize=(6, 6))
        self.ax.axis('off')
        self.ax.set_title("Simulation Feu de Forêt")

        self.image = self.ax.imshow(self._foret, cmap=self._cmap, norm=self._norm)
        for k in range(int(densite * taille * taille)):
            self._foret[randint(0, self._n - 1), randint(0, self._n - 1)] = 1

        self.miseAFeu()
        self.anim = FuncAnimation(self.fig, self.boucle_animation, frames=temps, interval=50, repeat=False)
        plt.show()

    def miseAFeu(self):
        self._foret[0, 0] = 2

    def miseAJour(self):
        matrice = zeros((self._n, self._n))
        for k in range(self._n):
            for l in range(self._n):
                if self._foret[k, l] == 2:
                    matrice[k, l] = 3
                    for (m, p) in ((k - 1, l), (k + 1, l), (k, l + 1), (k, l - 1)):
                        if m in (-1, self._n) or p in (-1, self._n):
                            pass
                        elif self._foret[m, p] == 1:
                            matrice[m, p] = 2
                elif matrice[k, l] == 0:
                    matrice[k, l] = self._foret[k, l]
        self._foret = matrice

    def representeForet(self):
        self.image.set_data(self._foret)

    def boucle_animation(self, frame):
        self.representeForet()
        self.miseAJour()
        return [self.image]


if __name__ == "__main__":
    FeuForet(taille=70, densite=0.8, temps=300)