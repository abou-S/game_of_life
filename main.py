import numpy as np

frame =   np.array([[0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0]])


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


while True:
    print(frame)
    frame = compute_next_frame(frame)

