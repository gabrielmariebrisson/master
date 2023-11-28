# -*- coding: utf-8 -*-
import time
import chess
from random import randint, choice

def randomMove(b):
    '''Renvoie un mouvement au hasard sur la liste des mouvements possibles. Pour avoir un choix au hasard, il faut
    construire explicitement tous les mouvements. Or, generate_legal_moves() nous donne un itérateur.'''
    return choice([m for m in b.generate_legal_moves()])

def deroulementRandom(b):
    '''Déroulement d'une partie d'échecs au hasard des coups possibles. Cela va donner presque exclusivement
    des parties très longues et sans gagnant. Cela illustre cependant comment on peut jouer avec la librairie
    très simplement.'''
    print("----------")
    print(b)
    if b.is_game_over():
        print("Resultat : ", b.result())
        return
    b.push(randomMove(b))
    deroulementRandom(b)
    b.pop()


def explorerTout(b):
    if b.is_game_over():
        return
    for m in b.generate_legal_moves():
        b.push(m)
        explorerTout(m)
        b.pop()


def explorerHorizon(b, max_depth=2):
    if b.is_game_over() or max_depth==0:
        return
    for m in b.generate_legal_moves():
        b.push(m)
        explorerHorizon(b, max_depth - 1)
        b.pop()

def HorizonMax(b, timelimit=30):
    depth = 1
    while True:
        t=time.time()
        explorerHorizon(b,depth)
        if time.time()-t > timelimit:
            return depth -1
        depth+=1
    return depth -1


def explorerHorizonEtCompter(b, max_depth=2):
    if b.is_game_over() or max_depth==0:
        return
    nb=1
    for m in b.generate_legal_moves():
        b.push(m)
        explorerHorizon(b, max_depth - 1)
        b.pop()
        nb+=1
    return nb

def evalBoard(b):
    valeurs = {'K' : 200, 'Q' : 9, 'R' : 5, 'B' :3, 'N' : 3, 'P': 1}

    score =0
    for k , p in b.piece_map().items():
        #print(k, ' --> ', p)
        line = k //8
        #if p.symbol().isupper():
        if p.symbol().upper() == p.symbol():
            score+= valeurs[p.symbol()]
            if p.symbol() == 'P':
                score   +=  0.1* (1+line)
        else:
            score-= valeurs[p.symbol().upper()]
            if p.symbol() == 'P':
                score   -=  0.1* (8 - line)
    return score

board = chess.Board()

def minMax(b, depth =3):
    if b.is_game_over() or depth==0:
        return evalBoard(b)
    pire = 400
    for m in b.generate_legal_moves():
        b.push(m)
        pire = min (pire, maxMin(b, depth -1 ))
        b.pop()
    return pire


def maxMin(b, depth =3):
    if b.is_game_over() or depth==0:
        return evalBoard(b)
    meilleur = -400
    for m in b.generate_legal_moves():
        b.push(m)
        meilleur = max (meilleur, minMax(b, depth -1 ))
        b.pop()
    return meilleur


def IAMinmax(b, depth =3):
    if b.is_game_over() or depth==0:
        return evalBoard(b)
    pire = 400
    best_moves = []
    for m in b.generate_legal_moves():
        b.push(m)
        val=maxMin(b, depth -1 )
        if val < pire:
            best_moves = [m]
            pire =val
        elif val ==pire:
            best_moves.append(m)
        pire = min (pire, val)
        b.pop()
    return choice(best_moves)


def IAMaxMin(b, depth =3):
    if b.is_game_over() or depth==0:
        return evalBoard(b)
    meilleur = -400
    best_moves = []
    for m in b.generate_legal_moves():
        b.push(m)
        val=minMax(b, depth -1 )
        if val > meilleur:
            best_moves = [m]
            meilleur =val
        elif val ==meilleur:
            best_moves.append(m)
        
        meilleur = max (meilleur, val)
        b.pop()
    return choice(best_moves)

print('le score de la board est de : ', evalBoard (board))

print('minmax (board) : ', minMax (board))
print('max (board) : ', maxMin (board))

# print(" Profondeur max explarabl en 30 s : ", HorizonMax(board))
# '''le resultat max est 4'''
# max_depth =4

# for depth in range(1, max_depth+2):
#     print("Nombre de noeuds à profondeur : ", depth," : ", explorerHorizonEtCompter(board, depth))
# explorerHorizon(board)
# explorerTout(board)
# print(board)
# deroulementRandom(board)