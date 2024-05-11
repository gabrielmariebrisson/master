CREATE OR REPLACE VIEW department_population AS
SELECT 
    d.id_departement,
    d.nom_departement,
    DATE_PART('year', s.date_debut) AS year,
    SUM(s.valeur) AS total_population
FROM 
    departement d
JOIN 
    commune c ON d.id_departement = c.id_departement
JOIN 
    statistique s ON c.id_com = s.id_com
WHERE 
    s.id_libelle = 'POP'
GROUP BY 
    d.id_departement, 
    d.nom_departement, 
    DATE_PART('year', s.date_debut);


CREATE OR REPLACE VIEW region_population AS
SELECT 
    r.id_region,
    r.nom_region,
    DATE_PART('year', s.date_debut) AS year,
    SUM(s.valeur) AS total_population
FROM 
    region r
JOIN 
    departement d ON r.id_region = d.id_region
JOIN 
    commune c ON d.id_departement = c.id_departement
JOIN 
    statistique s ON c.id_com = s.id_com
WHERE 
    s.id_libelle = 'POP'
GROUP BY 
    r.id_region, 
    r.nom_region, 
    DATE_PART('year', s.date_debut);
