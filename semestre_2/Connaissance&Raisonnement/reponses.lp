
#const a=3. %nb de missionnaires
#const p=3. %nb de cannibales

% État du bateau
bateau(0..2, 0..2).

% État des rives
rivesGauche(0..a,0..p).
rivesDroite(0,0).

% Définition d'une traversée valide
% Définition d'une traversée valide
traverse :-
    rivesGauche(M,C),              % Nombre de missionnaires et de cannibales sur la rive gauche
    rivesDroite(a-M,p-C),          % Nombre de missionnaires et de cannibales sur la rive droite
    bateau(MA_M, MA_C),            % Nombre de cannibales et de missionnaires dans le bateau
    MA_M + M + a-M = a,            % Le total de missionnaires après la traversée est égal au nombre initial sur la rive gauche
    MA_C + C + p-C = p,            % Le total de cannibales après la traversée est égal au nombre initial sur la rive gauche
    MA_C+MA_M > 0,                 % Le bateau transporte au moins une personne
    MA_C+MA_M  < 3,                % Le bateau transporte au plus deux personnes
    a-M >= p-C,                    % Vérification des cannibales sur la rive gauche
    M >= C,                        % Vérification des missionnaires sur la rive gauche
    MA_C >= 0, MA_M >= 0,          % Vérification des nombres de missionnaires et de cannibales dans le bateau
    p - (p-C) + (a-M) = p,         % Nombre de cannibales sur la rive droite après la traversée
    a - (a-M) + (p-C) = a.         % Nombre de missionnaires sur la rive droite après la traversée

% Définition des prédicats pour compter le nombre de personnes sur chaque rive
nombre_personnes(Rive, Missionnaires, Cannibales) :-
    (Rive = gauche -> rivesGauche(Missionnaires, Cannibales) ; rivesDroite(Missionnaires, Cannibales)).

% Prédicat pour afficher l'état de la population sur chaque rive
afficher_etat :-
    nombre_personnes(gauche, MissionnairesGauche, CannibalesGauche),
    nombre_personnes(droite, MissionnairesDroite, CannibalesDroite),
    write('État des rives après la traversée :'), nl,
    write('Rive gauche : '), write(MissionnairesGauche), write(' missionnaires, '), write(CannibalesGauche), write(' cannibales.'), nl,
    write('Rive droite : '), write(MissionnairesDroite), write(' missionnaires, '), write(CannibalesDroite), write(' cannibales.'), nl.

% Point d'entrée pour résoudre le problème
:- not traverse, afficher_etat.
