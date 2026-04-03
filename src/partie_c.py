def rlmmo_glouton(cible, pieces):
    # On s'assure que les pièces sont triées du plus grand au plus petit
    pieces = sorted(pieces, reverse=True)
    nb_pieces_total = 0
    
    print(f"--- Rendu glouton pour la cible : {cible} ---")
    
    for piece in pieces:
        if cible == 0:
            break  # On a fini
            
        quantite = cible // piece  # Combien de fois on peut prendre cette pièce ?
        
        if quantite > 0:
            print(f"- {quantite} pièce(s) de {piece}")
            nb_pieces_total += quantite
            cible = cible % piece  # Mise à jour du reste à payer
            
    if cible > 0:
        print("Attention : Impossible de rendre la monnaie exacte !")
        
    print(f"Total des pièces utilisées : {nb_pieces_total}\n")
    return nb_pieces_total

if __name__ == "__main__":
    # 1. Démonstration de l'échec (Contre-exemple de l'énoncé)
    print("TEST 1 : Le contre-exemple où le glouton échoue")
    pieces_piege = [6, 4, 1]
    # Le glouton va trouver 3 pièces (6+1+1) au lieu de l'optimal qui est 2 pièces (4+4)
    rlmmo_glouton(8, pieces_piege)

    # 2. Vérification expérimentale avec le système de l'Euro
    print("TEST 2 : Vérification avec le système de l'Euro")
    pieces_euro = [200, 100, 50, 20, 10, 5, 2, 1]
    # Doit fonctionner parfaitement (trouver le minimum absolu)
    rlmmo_glouton(190, pieces_euro)
    
    # 3. Test avec le système C' de l'énoncé
    print("TEST 3 : Test avec le système C'")
    pieces_c_prime = [50, 30, 10, 5, 3, 1]
    rlmmo_glouton(190, pieces_c_prime)