#const a = 3.  % Nombre de missionnaires et de cannibales
#const p = 2.  % Capacité de la barque

% Types
group(mis;can).
bank(l;r).
opposite(l,r).
opposite(r,l).
action(move(M,C)) :- M=0..2, C=0..2, M+C<3, M+C>0

% État initial
h(n(G,l),a) :- group(G).
h(n(G,r),0) :- group(G).
h(boat,l).

% Dynamique
1 {o(A) : action(A) } 1.

% Attributs des actions
moved(mis,M) :- o(move(M,C)).
moved(can,C) :- o(move(M,C)).

% Axiomes d'exécutabilité
:- moved(G,N), h(boat,B), h(n(G,B),M), N>M.

% Axiomes d'effet
h(n(G,B),M+N) :- h(n(G,B),M), h(boat,B), moved(G,N).
h(n(G,B),M-N) :- h(n(G,B),M), h(boat,B), moved(G,N).
h(boat,B1)    :- h(boat,B), opposite(B,B1).

% Toujours
:- h(n(mis,B),M), h(n(can,B),C), C>M, M>0.

% Final
:- not goal.
goal :- h(n(mis,r),a), h(n(can,r),p).

#show o/1.
