import simulation
import visualisation

def main():
    print(" PROJET PERCOLATION ")
    choix = input("Voulez-vous lancer :\n1. Une démonstration visuelle unique\n2. La courbe statistique complète\nVotre choix (1 ou 2) : ")
    
    if choix == "1":
        n = 100
        d = float(input("Entrez la densité (ex: 0.60) : "))
        
        print("Simulation en cours...")
        percole, foret_finale = simulation.simuler_feu_complet(n, d)
        
        resultat = "A PERCOLÉ (Le feu a traversé)" if percole else "N'A PAS PERCOLÉ"
        print(f"Résultat : {resultat}")
        
        visualisation.afficher_foret(foret_finale, titre=f"Résultat (d={d}) : {resultat}")
        
    elif choix == "2":
        n = 50
        nb_sim = 20
        
        print("Calcul de la courbe en cours (patience)...")
        x, y = simulation.etude_percolation(n, nb_simulations=nb_sim)
        
        visualisation.afficher_courbe_percolation(x, y)
        
    else:
        print("Choix invalide.")

if __name__ == "__main__":
    main()