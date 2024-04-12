/* QUESTION : 3 */

INSERT INTO Immeuble(NomImmeuble, Adresse, NbEtages, AnneeConstruction, NomGerant) 
VALUES ('LeChateau', '5 Rue Royale', 10, 1985, 'Ross');
/*reussite car ross est dans personne */

INSERT INTO Immeuble(NomImmeuble, Adresse, NbEtages, AnneeConstruction, NomGerant) 
VALUES ('LaTour', '8 Rue Belle', 20, 1978, 'Emma');
/*echec car emma n'est pas dans personnne*/


INSERT INTO Appart values ('LeChateau', 1, 500, 10);
INSERT INTO Occupant(NomImmeuble, NoAppart, NomOccupant, AnneeArrivee) 
VALUES ('LeChateau', 1, 'Alice', 2000);*/
/*reussite car Alice est une personne et il y a un appartement dans nom immeuble */

/* QUESTION : 4 */
ALTER TABLE Appart
ADD Loyer integer CHECK (Loyer > 0);

/* QUESTION : 5 */
INSERT INTO Personne(Nom, Profession)
VALUES ('David', 'Cadre');

/* QUESTION : 6 */
SELECT NomImmeuble, AVG(Superficie) AS SuperficieMoyenne
FROM Appart
GROUP BY NomImmeuble
HAVING COUNT(*) > 3;

/* QUESTION : 7 */

SELECT DISTINCT i.NomImmeuble
FROM Immeuble i
JOIN Appart a ON i.NomImmeuble = a.NomImmeuble
GROUP BY i.NomImmeuble
HAVING AVG(a.Superficie) > (
    SELECT AVG(Superficie)
    FROM Appart
    WHERE NomImmeuble = 'Koudalou'
);


/* QUESTION : 8 */
SELECT i.NomImmeuble
FROM Immeuble i
WHERE NOT EXISTS (
    SELECT *
    FROM Appart a
    WHERE a.NomImmeuble = i.NomImmeuble
    AND NOT EXISTS (
        SELECT *
        FROM Occupant o
        WHERE o.NomImmeuble = a.NomImmeuble
        AND o.NoAppart = a.NoAppart
    )
);

/* QUESTION : 9 */
SELECT DISTINCT p1.Nom AS Nom1, p2.Nom AS Nom2, o1.NomImmeuble AS ImmeubleCommun
FROM Occupant o1
JOIN Occupant o2 ON o1.NomImmeuble = o2.NomImmeuble AND o1.NoAppart <> o2.NoAppart
JOIN Personne p1 ON o1.NomOccupant = p1.Nom
JOIN Personne p2 ON o2.NomOccupant = p2.Nom
WHERE p1.Nom < p2.Nom
ORDER BY ImmeubleCommun, Nom1, Nom2;

/* QUESTION : 10 */
SELECT i.NomGerant AS NomGerant, MAX(a.Superficie) AS SuperficieMaximale
FROM Immeuble i
JOIN Appart a ON i.NomImmeuble = a.NomImmeuble
GROUP BY i.NomGerant;

/* QUESTION : 11 */
CREATE VIEW AppartGerant AS
SELECT a.NoAppart, a.NomImmeuble, i.NomGerant
FROM Appart a
JOIN Immeuble i ON a.NomImmeuble = i.NomImmeuble;
SELECT * FROM AppartGerant;

/* QUESTION : 12 */
INSERT INTO Appart(NomImmeuble, NoAppart, Superficie, Etage, Loyer)
VALUES ('Barabas', 3, 300, 3, 400);
SELECT * FROM AppartGerant;