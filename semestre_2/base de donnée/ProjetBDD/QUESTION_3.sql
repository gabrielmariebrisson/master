ALTER TABLE departement
ADD COLUMN total_population BIGINT DEFAULT 0;

ALTER TABLE region
ADD COLUMN total_population BIGINT DEFAULT 0;

CREATE OR REPLACE PROCEDURE update_population_totals()
LANGUAGE plpgsql
AS $$
BEGIN
    UPDATE departement d
    SET total_population = COALESCE((
        SELECT SUM(s.valeur)
        FROM commune c
        JOIN statistique s ON c.id_com = s.id_com
        WHERE c.id_departement = d.id_departement AND s.id_libelle = 'POP'
    ), 0);

    UPDATE region r
    SET total_population = COALESCE((
        SELECT SUM(d.total_population)
        FROM departement d
        WHERE d.id_region = r.id_region
    ), 0);
END;
$$;

CALL update_population_totals();
