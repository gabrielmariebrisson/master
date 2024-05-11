EXPLAIN
SELECT r.nom_region, c.nom_ville
FROM region r
JOIN departement d ON r.id_region = d.id_region
JOIN commune c ON d.id_departement = c.id_departement
JOIN statistique s ON c.id_com = s.id_com
WHERE s.id_libelle = 'POP';


EXPLAIN
SELECT c1.nom_ville, c2.nom_ville
FROM commune c1
JOIN statistique s1 ON c1.id_com = s1.id_com
JOIN commune c2 ON c1.id_departement = c2.id_departement
JOIN statistique s2 ON c2.id_com = s2.id_com
WHERE s1.id_libelle = 'POP' AND s1.valeur > 10000
  AND s2.id_libelle = 'POP' AND s2.valeur > 10000;
