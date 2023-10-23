# -*- coding: utf-8 -*-
''' la valeur MiniMax de l’arbre est 10  '''
import time
import Tictactoe 
from random import randint,choice

def RandomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles'''
    return choice(b.legal_moves())

def deroulementRandom(b):
    '''Effectue un déroulement aléatoire du jeu de morpion.'''
    print("----------")
    print(b)
    if b.is_game_over():
        res = getresult(b)
        if res == 1:
            print("Victoire de X")
        elif res == -1:
            print("Victoire de O")
        else:
            print("Egalité")
        return
    b.push(RandomMove(b))
    deroulementRandom(b)
    b.pop()


def getresult(b):
    '''Fonction qui évalue la victoire (ou non) en tant que X. Renvoie 1 pour victoire, 0 pour 
       égalité et -1 pour défaite. '''
    if b.result() == b._X:
        return 1
    elif b.result() == b._O:
        return -1
    else:
        return 0

def exploreTout(b):
    if b.is_game_over():
        return getresult
    for m in b.legal_moves():
        b.push(m)
        exploreTout(b)
        b.pop()

def exploreToutInfo(b, g, p, e, n, f):
    if b.is_game_over():
        value = getresult(b)
        if value == 1:
            g += 1
        elif value == -1:
            p += 1
        else:
            e += 1
        return g, p, e, n, f + 1
    for m in b.legal_moves():
        b.push(m)
        g, p, e, n, f = exploreToutInfo(b, g, p, e, n + 1, f)
        b.pop()
    return g, p, e, n, f


def minmax(b):
    if b.is_game_over():
        return getresult(b)
    pire =2
    for m in b.legal_moves():
        b.push(m)
        pire = min (pire, maxMin(b))
        b.pop()
    return pire

def maxMin(b):
    if b.is_game_over():
        return getresult(b)
    pire = -2
    for m in b.legal_moves():
        b.push(m)
        pire = max (pire, minmax(b))
        b.pop()
    return pire

def minmaxAvecCoupe(b):
    if b.is_game_over():
        return getresult(b)
    pire =2
    for m in b.legal_moves():
        b.push(m)
        pire = min (pire, maxMinAvecCoupe(b))
        b.pop()
        if pire ==-1:
            return -1
    return pire

def maxMinAvecCoupe(b):
    if b.is_game_over():
        return getresult(b)
    pire =2
    for m in b.legal_moves():
        b.push(m)
        pire = min (pire, minmaxAvecCoupe(b))
        b.pop()
        if pire == 1:
            return 1
    return pire
#print(gagnantAmi(board)) 

board = Tictactoe.Board()
print(board)

### Deroulement d'une partie aléatoire
deroulementRandom(board)

start_time = time.time()
gagnant, perdant, egalité, noeud, partie = exploreToutInfo(board, 0, 0, 0, 0, 0)
end_time = time.time()

print('nombre de noeuds :', noeud)
print('nombre de parties :', partie)
print('nombre de gagnants :', gagnant)
print('nombre de perdants :', perdant)
print('nombre de egalité :', egalité)

print("Temps d'execution : ", end_time - start_time)

start_time = time.time()
print("Y a-t-il une stratégie gagnante avec coupe ?", "oui" if maxMinAvecCoupe(board)==1 else "non")
end_time = time.time()
print("Temps d'execution : ", end_time - start_time)

start_time = time.time()
print("Y a-t-il une stratégie gagnante sans coupe ?", "oui" if maxMin(board)==1 else "non")
end_time = time.time()
print("Temps d'execution : ", end_time - start_time)


print("Apres le match, chaque coup est défait (grâce aux pop()): on retrouve le plateau de départ :")
print(board)

