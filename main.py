# Jeux Morpion

# Importation de la librairie random

import random

# Fonction pour vérifier si un joueur a gagné
def verif_gagne_ligne(grille_jeux):
    for i in range(3):
        premier_element = grille_jeux[i][0]
        for element in grille_jeux[i][1:]:
            if element != premier_element or element == '':
                break
        else:
            return True
    return False

def verif_gagne_colonne(grille_jeux):
    for i in range(3):
        premier_element = grille_jeux[0][i]
        for element in grille_jeux[1][i:]:
            if element != premier_element or element == '':
                break
        else:
            return True
    return False

def verif_gagne_diagonale(grille_jeux):
    premier_element = grille_jeux[0][0]
    for i in range(1, 3):
        if grille_jeux[i][i] != premier_element or grille_jeux[i][i] == '':
            break
    else:
        return True

    premier_element = grille_jeux[0][2]
    for i in range(1, 3):
        if grille_jeux[i][2-i] != premier_element or grille_jeux[i][2-i] == '':
            break
    else:
        return True

def plein(grille_jeux):
    for i in range(3):
        for j in range(3):
            if grille_jeux[i][j] != '':
                return False
    return True

# Initialisation de la grille de jeux
grille_jeux = [['','',''],
               ['','',''],
               ['','','']]

en_jeu = 'y'
# Boucle de jeu
while en_jeu == 'y' or en_jeu == 'Y':



    pion_j1_ligne = input('Donnez la ligne : ')
    pion_j1_colonne = input('Donnez la colonne : ')
    # Vérification de la saisie si c'est un nombre
    while pion_j1_ligne.isdigit() is False or pion_j1_colonne.isdigit() is False:
        print('Impossible, entrer un nombre.')
        pion_j1_ligne = input('Donnez la ligne : ')
        pion_j1_colonne = input('Donnez la colonne : ')

    pion_j1_ligne = int(pion_j1_ligne) - 1
    pion_j1_colonne = int(pion_j1_colonne) - 1
    # Vérification de la saisie si c'est un nombre entre 1 et 3
    while pion_j1_ligne < 1 or pion_j1_ligne > 3 or pion_j1_colonne < 1 or pion_j1_colonne > 3 :
        print('Impossible, la case n\'existe pas .')
        pion_j1_ligne = input('Donnez la ligne : ')
        pion_j1_colonne = input('Donnez la colonne : ')
        print('Impossible, la case n\'existe pas .')



    pion_j2_colonne = random.randint(0,2)
    pion_j2_ligne = random.randint(0,2)

    while grille_jeux[pion_j1_ligne][pion_j1_colonne] != '':
        print('Impossible, une case est déjà occupée par un joueur.')
        pion_j1_ligne = int(input('Donnez la ligne : ')) - 1
        pion_j1_colonne = int(input('Donnez la colonne : ')) - 1
    grille_jeux[pion_j1_ligne][pion_j1_colonne] = 'X'

    while grille_jeux[pion_j2_ligne][pion_j2_colonne] != '':
        pion_j2_colonne = random.randint(0, 2)
        pion_j2_ligne = random.randint(0, 2)
    grille_jeux[pion_j2_ligne][pion_j2_colonne] = 'O'



    if verif_gagne_ligne(grille_jeux) or verif_gagne_colonne(grille_jeux) or verif_gagne_diagonale(grille_jeux):
        print(f'Félicitations, vous avez gagné !')
        en_jeu = input('Veux tu continuer ? (y/N)')
    elif plein(grille_jeux) is True:
        print('Match nul')

    for i in range(3):
        print(grille_jeux[i])


