import model
import simulation
import visualisation


def main():
    print(" PROJET PERCOLATION ")
    print("1. Démonstration visuelle")
    print("2. Courbe statistique (Transition de Phase)")
    choix = input("Votre choix (1 ou 2) : ")

    if choix == "1":
        try:
            val_d = input("Entrez la densité (ex: 0.60) : ")
            d = float(val_d)
        except ValueError:
            d = 0.60
            print("Valeur incorrecte, utilisation de 0.60 par défaut.")

        n = 100

        print(f"Lancement de l'animation (n={n}, p={d})...")
        print("Fermez la fenêtre du graphique pour quitter.")

        # 1. On prépare la forêt
        foret = model.generer_foret(n, d)
        foret = model.allumer_feu(foret)

        # 2. On lance l'animation
        # On passe la fonction 'etape_propagation' à l'animateur pour qu'il s'en serve
        visualisation.animer_feu(foret, model.etape_propagation)

    elif choix == "2":
        n = 100
        nb_sim = 50

        print(f"Calcul de la courbe statistique en cours (n={n}, {nb_sim} sims/point)...")
        print("Cela peut prendre quelques secondes...")

        # 1. Calcul des données
        x, y = simulation.etude_percolation(n, nb_simulations=nb_sim)

        # 2. Analyse Mathématique
        seuil_calcule = simulation.trouver_seuil_critique(x, y)
        seuil_theorique = 0.592746

        if seuil_calcule is not None:
            print("-" * 40)
            print(f"RÉSULTATS DE L'ANALYSE :")
            print(f"Seuil critique estimé (simulé) : p_c ≈ {seuil_calcule:.4f}")
            print(f"Seuil critique théorique       : p_c = {seuil_theorique}")

            # Calcul de l'erreur relative
            erreur = abs(seuil_calcule - seuil_theorique) / seuil_theorique * 100
            print(f"Erreur relative                : {erreur:.2f}%")
            print("-" * 40)
        else:
            print("Impossible de calculer le seuil (la courbe est incomplète).")

        # 3. Affichage
        visualisation.afficher_courbe_percolation(x, y)


if __name__ == "__main__":
    main()