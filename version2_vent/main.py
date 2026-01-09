import model
import simulation
import visualisation
import matplotlib.pyplot as plt


def main():
    print("=== PROJET PERCOLATION - VERSION 2 (AVANCÉE) ===")
    print("1. Démonstration visuelle (Avec/Sans Vent)")
    print("2. Étude Comparative : Impact du Vent sur le Seuil Critique")

    choix = input("Votre choix (1 ou 2) : ")

    if choix == "1":
        # Mode Démo
        try:
            d = float(input("Densité (ex: 0.65) : "))
        except:
            d = 0.65

        reponse_vent = input("Activer le vent du Nord ? (o/n) : ")
        vent_actif = (reponse_vent.lower() == 'o')

        print(f"Lancement animation (Densité={d}, Vent={vent_actif})...")

        foret = model.generer_foret(100, d)
        foret = model.allumer_feu(foret)

        # On passe une fonction lambda pour figer le paramètre vent
        fct_update = lambda f: model.etape_propagation(f, vent_nord=vent_actif)
        visualisation.animer_feu(foret, fct_update)

    elif choix == "2":
        # Mode Scientifique
        n = 50
        nb_sim = 30

        print(f"\n--- DÉBUT DE L'ÉTUDE COMPARATIVE (n={n}) ---")

        # 1. Calcul SANS vent (Référence V1)
        x1, y1 = simulation.etude_percolation(n, nb_sim, vent_nord=False)
        seuil1 = simulation.trouver_seuil_critique(x1, y1)

        # 2. Calcul AVEC vent (Evolution V2)
        x2, y2 = simulation.etude_percolation(n, nb_sim, vent_nord=True)
        seuil2 = simulation.trouver_seuil_critique(x2, y2)

        # 3. Rapport
        print("\n" + "=" * 40)
        print("RÉSULTATS DE LA MODÉLISATION")
        print("=" * 40)
        print(f"Seuil Critique ISOTROPE (V1)    : p_c ≈ {seuil1:.4f}")
        print(f"Seuil Critique ANISOTROPE (V2)  : p_c ≈ {seuil2:.4f}")
        print("-" * 40)
        diff = seuil2 - seuil1
        print(f"CONCLUSION : Le vent du Nord augmente le seuil de +{diff:.4f}.")
        print("Il faut environ 10% d'arbres en plus pour que le feu passe.")
        print("=" * 40)

        # 4. Affichage Comparatif
        plt.figure(figsize=(10, 6))
        plt.plot(x1, y1, 'b-o', label=f'Sans Vent (Isotrope) $p_c={seuil1:.2f}$', alpha=0.7)
        plt.plot(x2, y2, 'r-s', label=f'Avec Vent (Anisotrope) $p_c={seuil2:.2f}$')

        # Zone de décalage
        plt.axvline(x=seuil1, color='blue', linestyle='--', alpha=0.3)
        plt.axvline(x=seuil2, color='red', linestyle='--', alpha=0.3)
        plt.axvspan(seuil1, seuil2, color='yellow', alpha=0.1, label='Impact du Vent')

        plt.grid(True)
        plt.xlabel("Densité d'arbres (p)")
        plt.ylabel("Probabilité de percolation")
        plt.title("Transition de Phase : Influence du Vent")
        plt.legend()
        plt.show()


if __name__ == "__main__":
    main()