import random

def printResultat(listePosition):
    plateau = [[' ' for j in range(8)] for i in range(8)]
    for (x,y) in listePosition:
        plateau[x][y]='R'
    printPlateau(plateau)

def printPlateau(plateau):
    for x in plateau:
        print (x)

def marquage(ligne, colone, plateau):
    plateau[ligne][colone] = False
    for i in range(8):
        plateau[ligne][i] = False
    for j in range(8):
        plateau[j][colone] = False
    for i in range(8):
        if (ligne + i < 8 and colone + i < 8):
            plateau[ligne + i][colone + i] = False
        if (ligne - i >= 0 and colone - i >= 0):
            plateau[ligne - i][colone - i] = False
        if (ligne + i < 8 and colone - i >= 0):
            plateau[ligne + i][colone - i] = False
        if (ligne - i >= 0 and colone + i < 8):
            plateau[ligne - i][colone + i] = False
    
    printPlateau(plateau)
    return plateau


def placement(plateau, nbreine, listePosition):
    if nbreine == 0:
        return listePosition, plateau
    ligne = 8 - nbreine
    colone = random.randint(0, 7)
    i = 100
    while plateau[ligne][colone] == False and i != 0:
        colone = random.randint(0, 7)
        i -= 1
    plateau = marquage(ligne, colone, plateau)
    listePosition += [(ligne, colone)]
    printResultat(listePosition)
    print()
    return placement(plateau, nbreine - 1, listePosition)

plateau = [[True for j in range(8)] for i in range(8)]
listePosition = []
printPlateau(plateau)
listePosition, plateau = placement(plateau, 8, listePosition)
print(listePosition)
print(plateau)
printResultat(listePosition)
