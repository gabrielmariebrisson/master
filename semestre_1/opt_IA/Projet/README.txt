IA Reversi - Maître d'Othello

Description :

Bienvenue dans Othello Master, un joueur intelligent de Reversi doté de capacités avancées en intelligence artificielle. Ce README fournit un aperçu des points forts et des fonctionnalités de notre IA Reversi.

Caractéristiques du joueur :

Algorithme Minimax :
Othello Master utilise l'algorithme Minimax pour la prise de décision.
La taille Alpha-Bêta est mise en œuvre pour améliorer l'efficacité dans l'exploration de l'arbre de jeu.
Fonctions heuristiques :
Othello Master propose plusieurs fonctions heuristiques pour évaluer les états du plateau :
- Heuristique de base : Évalue le plateau en fonction de la différence dans le nombre de pièces.
- Heuristique de grille Q-Learning : Utilise le Q-learning pour apprendre des expériences de jeu et prendre des décisions stratégiques.
- Heuristique de grille de voisinage et de position : Tient compte de la position sur le plateau et du nombre de pièces voisines.
Implémentation du Q-Learning :
Othello Master inclut une classe QLearning qui met en œuvre l'algorithme d'apprentissage par renforcement Q-learning.
Le Q-learning est utilisé pour apprendre des stratégies optimales à travers plusieurs simulations de jeu.
Modes de jeu :
Othello Master prend en charge différents modes de jeu, notamment :
- IA contre IA : Regardez deux intelligences artificielles s'affronter.
- IA contre humain : Testez vos compétences contre le joueur IA.
- Humain contre humain : Jouez au jeu classique de Reversi avec un ami.
Code structuré :
Le code est organisé en classes pour la modularité et la lisibilité.
Des commentaires et des docstrings en français fournissent des explications pour les composants clés.

Profondeur : La profondeur de recherche pour l'algorithme Minimax peut être personnalisée pour différents niveaux de difficulté.
Choix heuristiques : Choisissez parmi trois heuristiques pour influencer le processus de prise de décision de l'IA.
Q-Learning : Le joueur IA peut apprendre des expériences en utilisant le Q-learning, améliorant la réflexion stratégique au fil du temps.

Comment jouer :

Exécutez le script et choisissez le mode de jeu :
0 : IA contre IA
1 : IA contre humain
2 : Humain contre humain
Suivez les invites pour effectuer des mouvements ou regardez les IA en action.
