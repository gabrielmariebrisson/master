SELECT *
FROM pg_indexes
WHERE tablename = 'commune';


EXPLAIN
SELECT c.nom_ville
FROM commune c
JOIN statistique s ON c.id_com = s.id_com
WHERE s.id_libelle = 'POP'
    AND s.valeur < 5000 ;


CREATE INDEX idx_population ON statistique (valeur);

EXPLAIN
SELECT c.nom_ville
FROM commune c
JOIN statistique s ON c.id_com = s.id_com
WHERE  s.id_libelle = 'POP'
    AND s.valeur < 5000 ;


EXPLAIN

SELECT c.nom_ville, d.nom_departement
FROM commune c
JOIN statistique s ON c.id_com = s.id_com
JOIN departement d ON c.id_departement = d.id_departement
WHERE  s.id_libelle = 'POP'
    AND s.valeur < 5000 ;
