# VARIABLES GLOBALES
N = 190  # Somme cible (1€90 en centimes)
# Système de l'euro (C), trié par ordre décroissant
C = [200, 100, 50, 20, 10, 5, 2, 1]
n = len(C)

def rlmmo_prog_dynamique(cible, pieces):
    nb_pieces = len(pieces)
    
    # 1. INITIALISATION DE LA MATRICE NBP
    # Création d'une matrice (nb_pieces + 1) x (cible + 1) remplie de l'infini
    # float('inf') représente +infini en Python
    NBP = [[float('inf')] * (cible + 1) for _ in range(nb_pieces + 1)]
    
    # Si la cible est 0, il faut 0 pièce (pour toutes les lignes)
    for i in range(nb_pieces + 1):
        NBP[i][0] = 0

    # 2. REMPLISSAGE DU TABLEAU (bottom-up)
    for i in range(1, nb_pieces + 1):
        valeur_piece = pieces[i - 1] # l'index 0 de 'pieces' correspond à i=1
        
        for j in range(1, cible + 1):
            if j < valeur_piece:
                # La pièce est trop grosse, on reprend la valeur de la ligne du dessus
                NBP[i][j] = NBP[i - 1][j]
            else:
                # On prend le minimum entre : ne pas utiliser la pièce, ou l'utiliser
                NBP[i][j] = min(NBP[i - 1][j], 1 + NBP[i][j - valeur_piece])

    # 3. RETROUVER LES PIÈCES UTILISÉES (Chemin inverse)
    quantites = [0] * nb_pieces
    i = nb_pieces
    j = cible
    
    while i > 0 and j > 0:
        if NBP[i][j] == NBP[i - 1][j]:
            # La pièce n'a pas été utilisée pour former cette somme
            i = i - 1
        else:
            # La pièce a été utilisée 
            quantites[i - 1] += 1
            j = j - pieces[i - 1]
            # Note : on ne décrémente pas i car on a le droit de réutiliser la même pièce

    return NBP[nb_pieces][cible], quantites

# PROGRAMME PRINCIPAL
if __name__ == "__main__":
    print(f"Calcul (Prog. Dyn.) de la monnaie optimale pour {N} centimes...")
    
    minimum_pieces, detail_pieces = rlmmo_prog_dynamique(N, C)
    
    print("\n--- RÉSULTAT ---")
    print(f"Nombre minimal de pièces : {minimum_pieces}")
    
    print("\nDétail des pièces à rendre :")
    for index, qte in enumerate(detail_pieces):
        if qte > 0:
            print(f"- {qte} pièce(s) de {C[index]} centimes")

