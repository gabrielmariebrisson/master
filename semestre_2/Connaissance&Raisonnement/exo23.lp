% % Énoncé a.
% not_q :- not q.
% p :- not_q.

% % Énoncé b.
% not_q :- not q.
% p_q :- not_q, q.
% :- p, p_q.

% % Énoncé c.
% not_q :- not q.
% not_p :- not p.
% :- not_q, p.
% :- not_p, q.

% Énoncé d.
not_p :- not p.
not_q :- not q.
:- p, not_p.
:- q, not_q.
