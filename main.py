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
        n = 50 
        nb_sim = 20 
        
        print(f"Calcul de la courbe statistique (n={n}, {nb_sim} sims/point)...")
        x, y = simulation.etude_percolation(n, nb_simulations=nb_sim)
        
        visualisation.afficher_courbe_percolation(x, y)
        
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()