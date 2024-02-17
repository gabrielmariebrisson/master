SELECT "modele", "capacite" FROM  "TP1"."avion" ORDER BY "capacite";

SELECT
    "Planning"."NumVol",
    "Avions"."Modele",
    "Avions"."Capacite"
FROM
    "TP1"."Planning"
JOIN
    "TP1"."Avions" ON "Planning"."NumSerie" = "Avions"."NumSerie"
WHERE
    "Planning"."DateVol" = '2024-11-10'
    AND "Planning"."Destination" = 'NCE';
