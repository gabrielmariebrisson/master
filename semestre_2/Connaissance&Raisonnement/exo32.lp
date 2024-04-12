symbol(1..9). % lettres possibles
grid(0..8,0..8). % grille 9x9, indices commençant à 0

% chaque symbole est une et une seule fois par ligne:
1 {solution(X,Y,L) : grid(X,Y) } 1 :- grid(X,_), symbol(L).

% chaque symbole est une et une seule fois par colonne:
1 {solution(X,Y,L) : grid(X,Y) } 1 :- grid(_,Y), symbol(L).
solution(0,0,1). % il y a un 1 sur la case en haut à gauche


%autre solution
% rejeter si un symbole L apparait sur une même ligne X 
% et deux colonnes Y1 et Y2 différentes
%:- solution(X,Y1,L), solution(X,Y2,L), Y1 != Y2.

% rejeter si un symbole L apparait sur une même colonne Y
% et deux lignes X1 et X2 différentes
%:- solution(X1,Y,L), solution(X2,Y,L), X1 != X2.


%blockrange(A,B,A*S..((A+1)*S-1),B*S..((B+1)*S-1)) :- block(A,B), S = 3.
%:- solution(X1,Y1,L), solution(X2,Y2,L), block(X1/3,Y1/3), block(X2/3,Y2/3), (X1,Y1) != (X2,Y2).
