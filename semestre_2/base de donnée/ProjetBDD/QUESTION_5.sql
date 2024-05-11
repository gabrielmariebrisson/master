CREATE OR REPLACE FUNCTION update_department_population()
RETURNS void AS $$
BEGIN
    UPDATE departement SET total_population = sq.total
    FROM (
        SELECT d.id_departement, SUM(c.population) AS total
        FROM commune c
        JOIN departement d ON c.id_departement = d.id_departement
        GROUP BY d.id_departement
        HAVING COUNT(*) = (SELECT COUNT(*) FROM commune WHERE id_departement = d.id_departement)
    ) AS sq
    WHERE departement.id_departement = sq.id_departement;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_region_population()
RETURNS void AS $$
BEGIN
    UPDATE region SET total_population = sq.total
    FROM (
        SELECT r.id_region, SUM(d.total_population) AS total
        FROM departement d
        JOIN region r ON d.id_region = r.id_region
        WHERE d.total_population IS NOT NULL
        GROUP BY r.id_region
        HAVING COUNT(d.total_population) = (SELECT COUNT(*) FROM departement WHERE id_region = r.id_region)
    ) AS sq
    WHERE region.id_region = sq.id_region;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION trigger_update_population()
RETURNS trigger AS $$
BEGIN
    -- Mettre à jour la population du département si toutes les communes sont renseignées
    PERFORM update_department_population();

    -- Mettre à jour la population de la région si tous les départements sont renseignés
    PERFORM update_region_population();

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_population_update
AFTER INSERT OR UPDATE ON commune
FOR EACH ROW EXECUTE PROCEDURE trigger_update_population();
