%:- parent(X,Y).
%:- homme(X).
%:- femme(X).

pere(X,Y) :- parent(X,Y), homme(X).
mere(X,Y) :- parent(X,Y), femme(X).

fils(X,Y) :- parent(X,Y), homme(Y).
fille(X,Y) :- parent(X,Y), femme(Y).

frere(X,Y) :- parent(Z,X), parent(Z,Y) , homme(X).
soeur(X,Y) :- parent(Z,X), parent(Z,Y) , femme(X).

grandparent(X,Y) :- parent(X,Z), parent(Z,Y).

oncle(Z,Y) :- parent(X,Y), frere(X,Z).
tante(Z,Y) :- parent(X,Y), soeur(X,Z).

%cousin(X,Y) :- grandparent(Z,X),grandparent(Z,Y). ne fonctionne pas cra frere et soeur  pas cousin
cousin(X,Y) :- parent(Z,X), parent(W,Y), fraterie(Z,W).
fraterie(X,Y) :- parent(Z,X), parent(Z,Y).

parent(X,Y) :- pere(X,Y).
homme(X) :- pere(X,Y).
homme(X) :- frere(X,Y).
homme(X) :- fils(X,Y).
homme(X) :- oncle(X,Y).

parent(X,Y) :- mere(X,Y).
femme(X) :- mere(X,Y).
femme(X) :- soeur(X,Y).
femme(X) :- fille(X,Y).
femme(X) :- tante(X,Y).

fraterie(X,Y) :- fraterie(Y,X).

pere(jean, marie).
mere(marie,pierre). 
pere(jean,david).
%:- not grandparent(jean, pierre).
:- not fraterie(marie, david).