# Jeux du morpion

# Importation de la bibliothèque random
import random

# Fonction pour vérifier si un joueur a gagné avec une ligne complète
def verif_gagne_ligne(grille_jeux):
    for i in range(3):
        premier_element = grille_jeux[i][0]
        for element in grille_jeux[i][1:]:
            if element != premier_element or element == '':
                break
        else:
            return True
    return False

# Fonction pour vérifier si un joueur a gagné avec une colonne complète
def verif_gagne_colonne(grille_jeux):
    for i in range(3):
        premier_element = grille_jeux[0][i]
        for j in range(1, 3):
            if grille_jeux[j][i] != premier_element or grille_jeux[j][i] == '':
                break
        else:
            return True
    return False

# Fonction pour vérifier si un joueur a gagné avec une diagonale complète
def verif_gagne_diagonale(grille_jeux):
    premier_element = grille_jeux[0][0]
    for i in range(1, 3):
        if grille_jeux[i][i] != premier_element or grille_jeux[i][i] == '':
            break
    else:
        return True

    premier_element = grille_jeux[0][2]
    for i in range(1, 3):
        if grille_jeux[i][2 - i] != premier_element or grille_jeux[i][2 - i] == '':
            break
    else:
        return True

# Fonction pour vérifier si la grille est pleine et qu'il n'y a pas de gagnant
def plein(grille_jeux):
    for i in range(3):
        for j in range(3):
            if grille_jeux[i][j] != '':
                return False
    return True
# Mini_ia pour le joueur 2
def j2_ia(grille_jeux):
    # Vérification des lignes et des colonnes pour gagner ou bloquer
    for i in range(3):
        # Vérification des lignes
        if grille_jeux[i][0] == grille_jeux[i][1] == 'O' and grille_jeux[i][2] == '':
            grille_jeux[i][2] = 'O'
            return grille_jeux
        if grille_jeux[i][0] == grille_jeux[i][2] == 'O' and grille_jeux[i][1] == '':
            grille_jeux[i][1] = 'O'
            return grille_jeux
        if grille_jeux[i][1] == grille_jeux[i][2] == 'O' and grille_jeux[i][0] == '':
            grille_jeux[i][0] = 'O'
            return grille_jeux

        # Vérification des colonnes
        if grille_jeux[0][i] == grille_jeux[1][i] == 'O' and grille_jeux[2][i] == '':
            grille_jeux[2][i] = 'O'
            return grille_jeux
        if grille_jeux[0][i] == grille_jeux[2][i] == 'O' and grille_jeux[1][i] == '':
            grille_jeux[1][i] = 'O'
            return grille_jeux
        if grille_jeux[1][i] == grille_jeux[2][i] == 'O' and grille_jeux[0][i] == '':
            grille_jeux[0][i] = 'O'
            return grille_jeux

        if grille_jeux[0][0] == grille_jeux[1][1] == 'O' and grille_jeux[2][2] == '':
            grille_jeux[2][2] = 'O'
            return grille_jeux

        if grille_jeux[0][0] == grille_jeux[2][2] == 'O' and grille_jeux[1][1] == '':
            grille_jeux[1][1] = 'O'
            return grille_jeux

        if grille_jeux[1][1] == grille_jeux[2][2] == 'O' and grille_jeux[0][0] == '':
            grille_jeux[0][0] = 'O'
            return grille_jeux
        if plein(grille_jeux) is True:
            return grille_jeux

    # Si aucune possibilité de gagner ou bloquer, jouer aléatoirement
    while True:
        pion_j2_ligne = random.randint(0, 2)
        pion_j2_colonne = random.randint(0, 2)
        if grille_jeux[pion_j2_ligne][pion_j2_colonne] == '':
            grille_jeux[pion_j2_ligne][pion_j2_colonne] = 'O'
            return grille_jeux



# Initialisation de la grille de jeux
grille_jeux = [['', '', ''],
               ['', '', ''],
               ['', '', '']]

en_jeu = 'y'
# Boucle de jeu
while en_jeu != 'N' and en_jeu != 'n':

    # demande de la ligne et de la colonne pour le joueur 1
    pion_j1_ligne = input('Donnez la ligne : ')
    pion_j1_colonne = input('Donnez la colonne : ')

    # Vérification de la saisie si c'est un nombre
    while pion_j1_ligne.isdigit() is False or pion_j1_colonne.isdigit() is False:
        print('Impossible, entrer un nombre.')
        pion_j1_ligne = input('Donnez la ligne : ')
        pion_j1_colonne = input('Donnez la colonne : ')
    # Conversion de la saisie en entier + -1 pour correspondre à l'index
    pion_j1_ligne = int(pion_j1_ligne) - 1
    pion_j1_colonne = int(pion_j1_colonne) - 1

    # Vérification de la saisie si c'est un nombre entre 1 et 3
    while pion_j1_ligne < 0 or pion_j1_ligne > 2 or pion_j1_colonne < 0 or pion_j1_colonne > 2:
        print('Impossible, la case n\'existe pas .')
        pion_j1_ligne = int(input('Donnez la ligne : '))
        pion_j1_colonne = int(input('Donnez la colonne : '))



    # Vérification si la case est déjà occupée pour le joueur
    while grille_jeux[pion_j1_ligne][pion_j1_colonne] != '':
        print('Impossible, une case est déjà occupée par un joueur.')
        pion_j1_ligne = int(input('Donnez la ligne : ')) - 1
        pion_j1_colonne = int(input('Donnez la colonne : ')) - 1
    grille_jeux[pion_j1_ligne][pion_j1_colonne] = 'X'

    # Appel de la fonction pour le joueur 2
    grille_jeux = j2_ia(grille_jeux)

    # Affichage de la grille de jeux
    for i in range(3):
        print(grille_jeux[i])
    # Vérification si un joueur a gagné
    if verif_gagne_ligne(grille_jeux) or verif_gagne_colonne(grille_jeux) or verif_gagne_diagonale(grille_jeux):
        print(f'Félicitations, vous avez gagné !')
        en_jeu = input('Veux tu continuer ? (y/N)')
        grille_jeux = [['', '', ''],
                       ['', '', ''],
                       ['', '', '']]
    # Vérification si la grille est pleine et qu'il n'y a pas de gagnant
    elif plein(grille_jeux) is True:
        print('Match nul')


