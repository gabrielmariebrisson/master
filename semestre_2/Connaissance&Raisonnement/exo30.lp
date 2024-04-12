node(1..5).
edge(1,2). edge(2,3). edge(3,4). edge(2,4). edge(4,5).

clique_node(N) :- node(N).

clique(X, Y) :- edge(X, Y), clique_node(X), clique_node(Y).

clique_size_at_least_3(X, Y) :- clique(X, Y), X < Y.
clique_size_at_least_3(X, Z) :- clique_size_at_least_3(X, Y), clique_size_at_least_3(Y, Z).

#show clique_size_at_least_3/2.
