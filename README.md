# AI_Connect_Four
Code to implement an AI to play against at Connect four, using the min_max algorithm and alpha_beta pruning
The AI is calculating with a depth of 4, using around 1 or 2 seconds to play. We could increase the depth,
which would also increase the time needed to caculate.
I used 2 main heuristics. The first one promotes 3 tokens connected and square of 2by2 tokens connected
since it can lead to a win for the player connecting the tokens.
The second one promotes the center of the grid, when the AI does not know where to play after looking 
at the first heuristic.

Le code proposé permet de créer une IA de puissance 4 en utilisant l'algorithme Min-Max avec l'élaguage 
Alpha-Beta. La profondeur est de 4 afin d'accélérer le temps de calcul (1 à 2 secondes par coup en général)
Il y a deux heuristiques. La première incite à connecter trois jetons en ligne, diagonale et colonne car cela
peut mener à la victoire. Il y a aussi le carré de 4 jetons (2 sur 2) qui est une position favorable.
La deuxième heuristique permet de départager quand il n'y a pas de coup intéressant selon la première 
heuristique. Cette heuristique favorise le jeu of centre de la grille car cela donne plus de possibilités
de connecter plusieurs jetons
