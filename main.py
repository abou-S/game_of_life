import pygame
import sys
import numpy as np

pygame.init()

LARGEUR_FENETRE = 490
HAUTEUR_FENETRE = 490
TAILLE_CELLULE = 70  


screen = pygame.display.set_mode((LARGEUR_FENETRE, HAUTEUR_FENETRE))
pygame.display.set_caption("Jeu de la vie")



def compute_number_neighbors(paded_frame, index_line, index_column):
    """
    Cette fonction prend en entrée la matrice avec bordure et
    renvoie le nombre de cellules voisines vivantes.
    """
    haut = paded_frame[index_line-1, index_column]
    bas = paded_frame[index_line+1,index_column]
    droite = paded_frame[index_line, index_column+1]
    gauche = paded_frame[index_line, index_column-1]
    diag_Sup_droit = paded_frame[index_line-1,index_column+1]
    diag_Sup_gauche = paded_frame[index_line-1,index_column-1]
    diag_inf_droit = paded_frame[index_line+1,index_column+1]
    diag_inf_gauche = paded_frame[index_line+1, index_column-1]

    number_neighbors = haut + bas + droite + gauche + diag_Sup_droit + diag_Sup_gauche + diag_inf_droit + diag_inf_gauche

    return number_neighbors
def compute_next_frame(frame):
    paded_frame = np.pad(frame, 1, mode="constant") 
    for i in range(1,len(paded_frame)-1):
        for j in range(1,len(paded_frame[0])-1):

            number_neighbors = compute_number_neighbors(paded_frame,i,j)
            if paded_frame[i,j] == 0 and number_neighbors == 3 :
                frame[i-1,j-1] = 1
                print((i-1,j-1),"a {} neighbors".format(number_neighbors))
            elif paded_frame[i,j]== 1 and (number_neighbors == 2 or number_neighbors == 3):
                pass
            else:
                frame[i-1,j-1] = 0
                
    return frame


def afficher_matrice(frame):
    for i in range(len(frame)):
        for j in range(len(frame[i])):
            
            x = j * TAILLE_CELLULE
            y = i * TAILLE_CELLULE
            
            # Choix de la couleur
            if frame[i][j] == 1:
                couleur = (0, 0, 0)  # Noir pour 1
            else:
                couleur = (255, 255, 255)  # Blanc pour 0
            
            # Dessiner le rectangle correspondant à la cellule
            pygame.draw.rect(screen, couleur, (x, y, TAILLE_CELLULE, TAILLE_CELLULE))
            pygame.draw.rect(screen, (0, 0, 0), (x, y, TAILLE_CELLULE, TAILLE_CELLULE), 1)  # Bordure noire

def main():
    clock = pygame.time.Clock()
    frame =   np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])

    while True:
        screen.fill((255, 255, 255))  # Fond blanc

        # Gestion des événements (comme fermer la fenêtre)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        frame = compute_next_frame(frame)

        # Afficher la matrice
        afficher_matrice(frame)

        # Actualiser l'affichage
        pygame.display.flip()

        # Limiter la fréquence de rafraîchissement (ici à 30 FPS)
        clock.tick(30)

# Lancer le programme
if __name__ == "__main__":
    main()
