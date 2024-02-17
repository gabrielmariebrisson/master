INSERT INTO "TP1"."Vols" ("NumVol", "Heure", "Depart", "Arrivee") VALUES
(1002, '2024-02-16 14:00:00', 'LHR', 'CDG'),
(1003, '2024-02-16 11:35:00', 'TLS', 'ORY'),
(1007, '2024-02-16 23:30:00', 'CGD', 'SEA'),
(1004, '2024-02-16 07:00:00', 'BOD', 'TUN'),
(1005, '2024-02-16 09:15:00', 'MRS', 'PRG'),
(1008, '2024-02-16 08:00:00', 'ORY', 'NCE'),
(1006, '2024-02-16 16:45:00', 'ORY', 'TLS'),
(1009, '2024-02-16 18:00:00', 'CGD', 'LUX');

INSERT INTO "TP1"."Pilote" ("Matricule", "Nom", "Anciennete", "Age") VALUES
(2, 'Peter', 40, 10),
(3, 'Scott', 32, 5),
(4, 'John', 46, 12),
(5, 'Bill', 42, 13),
(6, 'Steve', 55, 20),
(7, 'Adam', 30, 2),
(8, 'Tom', 37, 8),
(9, 'Philip', 60, 23);


INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie") values (1002, '2024-11-24  14:00:00', 2, 108); 
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1003, '2024-11-03 14:00:00', 3, 104);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1006, '2024-11-01 14:00:00', 4, 104);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1005, '2024-11-16 14:00:00', 9, 106);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1003, '2024-11-02 14:00:00', 8, 107); 
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1007, '2024-11-10 14:00:00', 7, 101);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1007, '2024-11-24 14:00:00', 5, 103);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1008, '2024-11-10 14:00:00', 5, 107);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1002, '2024-11-30 14:00:00', 5, 108);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1006, '2024-11-05 14:00:00', 4, 104);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1008, '2024-11-02 14:00:00', 2, 105);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1005, '2024-11-02 14:00:00', 3, 106);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1002, '2024-11-15 14:00:00', 5, 101);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1005, '2024-11-03 14:00:00', 9, 106);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1003, '2024-11-05 14:00:00', 4, 104);
INSERT INTO "TP1"."Planning"("NumVol", "DateVol", "Matricule", "NumSerie")  values (1009, '2024-11-24 14:00:00', 7, 101);

