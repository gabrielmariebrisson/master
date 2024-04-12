#const a=3. %nb de missionnaires
#const p=3. %nb de cannibales

#program initial.
personne(cannibales;missionnaires).
rive(droite;gauche).
oppose(gauche,droite).
oppose(droite,gauche).

nb(position(G, gauche),3 ) :- personne(G).
nb(position(G, droite),0 ) :- personne(G).
nb(bateau,gauche).

action(move(M,C)) :- M=0..2, C=0..2, M+C<3, M+C>0.

#program dynamic.
1 {o(A) : action(A) } 1.

a_bouge(cannibales, C) :- o(move(M, C)).
a_bouge(missionnaires, M) :- o(move(M, C)).

:- a_bouge(G, N), 'nb(bateau, B), 'nb(position(G, B), M), N > M.


nb(position(G, B), M - N) :- 'nb(n(G, B), M), 'nb(bateau, B), a_bouge(G, N).
nb(position(G, B), M + N) :- 'nb(n(G, B), M), nb(bateau, B), a_bouge(G, N).
nb(bateau, B1)     :- 'nb(bateau, B), _oppose(B, B1).

#program always.
:- nb(position(missionnaires, B), M), nb(position(cannibales, B), C), C > M, M > 0.

#program final.
:- nb(position(missionnaires, gauche), a), nb(position(cannibales, gauche), p).

