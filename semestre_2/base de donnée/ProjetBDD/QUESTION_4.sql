-- Trigger function to prevent modifications
CREATE OR REPLACE FUNCTION prevent_modification()
RETURNS trigger AS $$
BEGIN
    RAISE EXCEPTION 'Modification not allowed on % table.', TG_TABLE_NAME;
END;
$$ LANGUAGE plpgsql;

-- Block changes on departement
CREATE TRIGGER block_departement_modification
BEFORE INSERT OR UPDATE OR DELETE ON departement
FOR EACH ROW EXECUTE PROCEDURE prevent_modification();

-- Block changes on region
CREATE TRIGGER block_region_modification
BEFORE INSERT OR UPDATE OR DELETE ON region
FOR EACH ROW EXECUTE PROCEDURE prevent_modification();


CREATE OR REPLACE FUNCTION update_population_on_change()
RETURNS trigger AS $$
BEGIN
    IF TG_OP = 'UPDATE' AND OLD.id_libelle = 'POP' AND NEW.valeur IS DISTINCT FROM OLD.valeur THEN
        CALL update_population_totals();
    ELSIF TG_OP = 'INSERT' AND NEW.id_libelle = 'POP' THEN
        CALL update_population_totals();
    ELSIF TG_OP = 'DELETE' AND OLD.id_libelle = 'POP' THEN
        CALL update_population_totals();
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER update_population_after_statistique_change
AFTER INSERT OR UPDATE OR DELETE ON statistique
FOR EACH ROW EXECUTE PROCEDURE update_population_on_change();
