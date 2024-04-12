node(1..5).
edge(1,2). edge(2,3). edge(3,4). edge(2,4). edge(4,5).

color(red). color(blue). color(green). color(yellow).

1 { node_color(N, C) : color(C) } 1 :- node(N).

:- edge(X, Y), node_color(X, C), node_color(Y, C).

:- not node_color(_, _).

#show node_color/2.
