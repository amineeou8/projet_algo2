import math

# VARIABLES GLOBALES 
N = 190  # Somme cible à rendre (1€90)
# Système de pièces (l'ensemble C en centimes), trié par ordre décroissant
C = [200, 100, 50, 20, 10, 5, 2, 1] 
n = len(C)

X = [0] * n  # Vecteur candidat en cours de construction
Y = [0] * n  # Vecteur de la meilleure solution trouvée
nb_opt_pieces = float('inf')  # Le record absolu, initialisé à l'infini

def rlmmo_essais_successifs(i, somme_courante, nb_pieces_courant):
    global nb_opt_pieces, Y, X
    
    # Si on a exploré toutes les pièces, on s'arrête
    if i >= n:
        return

    # 1. Calculer l'ensemble S_i (combien de pièces C[i] au maximum ?)
    max_pieces = (N - somme_courante) // C[i]
    
    # On boucle à l'envers (de max_pieces jusqu'à 0).
    # Ça teste les grosses pièces d'abord, on trouve un super record très vite, 
    # et l'élagage coupera 99% de l'arbre ensuite !
    for x_i in range(max_pieces, -1, -1):
        
        # Fonction SATISFAISANT(x_i)
        if somme_courante + (x_i * C[i]) <= N:
            
            # Fonction ENREGISTRER(x_i)
            X[i] = x_i
            nouvelle_somme = somme_courante + (x_i * C[i])
            nouveau_nb_pieces = nb_pieces_courant + x_i
            
            # Fonction SOLTROUVÉE
            if nouvelle_somme == N:
                # Est-ce une "meilleure" solution ?
                if nouveau_nb_pieces < nb_opt_pieces:
                    Y = list(X)  # On copie la solution (MAJVALOPT)
                    nb_opt_pieces = nouveau_nb_pieces
            else:
                # Fonction OPTENCOREPOSSIBLE (Élagage)
                reste = N - nouvelle_somme
                
                # Estimation : combien de pièces minimum pour finir ?
                # On utilise C[0] (la plus grosse pièce du système) pour être sûr.
                estimation_min = math.ceil(reste / C[0])
                
                # Si le total actuel + l'estimation parfaite bat le record, on continue 
                if (i + 1 < n) and (nouveau_nb_pieces + estimation_min < nb_opt_pieces):
                    rlmmo_essais_successifs(i + 1, nouvelle_somme, nouveau_nb_pieces)
            
            # Fonction DÉFAIRE(x_i)
            # X[i] sera écrasé à la prochaine itération, mais on le remet à 0 pour la propreté
            # La somme et le nb de pièces retournent en arrière naturellement 
            # grâce aux variables locales de la fonction).
            X[i] = 0

# PROGRAMME PRINCIPAL
if __name__ == "__main__":
    print(f"Calcul de la monnaie optimale pour {N} centimes...")
    
    # On lance l'algo à l'index 0 (la première pièce), avec une somme de 0 et 0 pièce.
    rlmmo_essais_successifs(0, 0, 0)
    
    print("\n--- RÉSULTAT ---")
    print(f"Meilleure combinaison (Y) : {Y}")
    print(f"Nombre minimal de pièces : {nb_opt_pieces}")
    