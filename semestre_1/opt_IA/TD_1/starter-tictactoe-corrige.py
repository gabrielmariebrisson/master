# -*- coding: utf-8 -*-

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

def exploreTout(b):
    if b.is_game_over():
        return
    for m in b.legal_moves():
        b.push(m)
        exploreTout(b)
        b.pop()

def exploreToutEtCompter(b):
    if b.is_game_over():
        return 0, 1 #on a atteint une feuille
    n, f = 0, 0 #n : nombre total de noeuds, f : nombre de feuilles 
    for m in b.legal_moves():
        n += 1
        b.push(m)
        nn, nf = exploreToutEtCompter(b)
        n += nn
        f += nf
        b.pop()
    return n, f

nbNoeuds = 0
def gagnantAmi(b, compter=False):
    global nbNoeuds
    if compter:
        nbNoeuds += 1
    if b.is_game_over():
       return getresult(b)
    maxx = -1
    for move in b.legal_moves():
        b.push(move)
        minn = gagnantEnnemi(b, compter)
        b.pop()
        if minn > maxx:
            maxx = minn
    return maxx

def gagnantEnnemi(b, compter=False):
    global nbNoeuds
    if compter:
        nbNoeuds += 1
    if b.is_game_over():
       return getresult(b)
    minn = 1
    for move in b.legal_moves():
        b.push(move)
        maxx = gagnantAmi(b, compter)
        b.pop()
        if maxx < minn:
            minn = maxx
    return minn

def gagnantAmiAvecCoupe(b, compter=False):
    global nbNoeuds
    if compter:
        nbNoeuds += 1
    if b.is_game_over():
       return getresult(b)
    maxx = -1
    for move in b.legal_moves():
        b.push(move)
        minn = gagnantEnnemiAvecCoupe(b, compter)
        b.pop()
        if minn == 1: # Ces deux lignes permettent de couper dans l'arbre de recherche
            return 1
        if minn > maxx:
            maxx = minn
    return maxx

def gagnantEnnemiAvecCoupe(b, compter=False):
    global nbNoeuds
    if compter:
        nbNoeuds += 1
    if b.is_game_over():
       return getresult(b)
    minn = 1
    for move in b.legal_moves():
        b.push(move)
        maxx = gagnantAmiAvecCoupe(b, compter)
        b.pop()
        if maxx == -1:  # Ces deux lignes permettent de couper dans l'arbre de recherche
            return -1
        if maxx < minn:
            minn = maxx
    return minn

def getresult(b):
    '''Fonction qui évalue la victoire (ou non) en tant que X. Renvoie 1 pour victoire, 0 pour 
       égalité et -1 pour défaite. '''
    if b.result() == b._X:
        return 1
    elif b.result() == b._O:
        return -1
    else:
        return 0


board = Tictactoe.Board()
#print(board)

### Deroulement d'une partie aléatoire
#deroulementRandom(board)

### Déroulement total
#exploreTout(board)

### Déroulement total et comptage
n, f = exploreToutEtCompter(board)
print('nombre total de noeuds : ',n, ' dont ', f, ' feuilles')

### Deroulement total : temps
#t1 = time.time()
#exploreTout(board)
#print('t : ', time.time() - t1)

### Existe-t-il une stratégie gagnante ?
#print(gagnantAmi(board)) 

### On compare le temps entre avec et sans coupe :
# t = time.time()
# print(gagnantAmi(board)) 
# print('temps sans coupe : ', time.time() - t)

# t = time.time()
# print(gagnantAmiAvecCoupe(board)) 
# print('temps avec coupe : ', time.time() - t)

### On compare le nombre de noeuds entre avec et sans coupe :
nbNoeuds = 0
print('Stratégie gagnante: ', gagnantAmi(board, compter=True)) 
print('Nombre de neouds sans coupe : ', nbNoeuds)
nbNoeuds = 0
print('Stratégie gagnante: ', gagnantAmiAvecCoupe(board, compter=True)) 
print('Nombre de noeuds avec coupe : ', nbNoeuds)


print("Apres le match, chaque coup est défait (grâce aux pop()): on retrouve le plateau de départ :")
print(board)

