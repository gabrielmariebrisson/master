create table Immeuble(
NomImmeuble varchar,
Adresse varchar,
NbEtages integer,
AnneeConstruction integer,
NomGerant varchar);

ALTER TABLE Immeuble
ADD PRIMARY KEY (NomImmeuble);

insert into Immeuble(NomImmeuble,Adresse,NbEtages,AnneeConstruction,NomGerant) values
('Koudalou', '3 rue Blanche', 15, 1975, 'Doug'),
('Barabas', '2 Allee Nikos', 2, 1973, 'Ross')
;


Create table Appart(
NomImmeuble varchar,
NoAppart integer,
Superficie integer,
Etage integer);

ALTER TABLE Appart
ADD PRIMARY KEY (NomImmeuble, NoAppart);


insert into Appart values ('Koudalou', 1, 150, 14),
('Koudalou', 34, 50, 15),
('Koudalou', 51, 200, 2),
('Koudalou', 52, 50, 5),
('Barabas', 1, 250, 1),
('Barabas', 2, 250, 2);

create table Personne(
Nom varchar,
Age integer,
Profession varchar);

ALTER TABLE Personne
ADD PRIMARY KEY (Nom);

insert into Personne values
('Ross', 51, 'Informaticien'),
('Alice', 34, 'Cadre'),
('Rachel',23, 'Stagiaire'),
('William',52,'Acteur'),
('Doug',34,'Rentier')
;

create table Occupant(
NomImmeuble varchar,
NoAppart integer,
NomOccupant varchar,
AnneeArrivee integer);

ALTER TABLE Occupant
ADD PRIMARY KEY (NomImmeuble, NoAppart);


insert into Occupant values('Koudalou',1,'Rachel',1992),
('Barabas',1,'Doug',1994),
('Barabas',2,'Ross',1994),
('Koudalou',51,'William',1996),
('Koudalou',34,'Alice',1993);


/*QUESTION 2*/

ALTER TABLE Occupant
ADD CONSTRAINT FK_Appart_Occupant
FOREIGN KEY (NomImmeuble, NoAppart) REFERENCES Appart(NomImmeuble, NoAppart);

ALTER TABLE Appart
ADD CONSTRAINT FK_Immeuble_Appart
FOREIGN KEY (NomImmeuble) REFERENCES Immeuble(NomImmeuble);

ALTER TABLE Occupant
ADD CONSTRAINT FK_Personne_Occupant
FOREIGN KEY (NomOccupant) REFERENCES Personne(Nom);

ALTER TABLE Immeuble
ADD CONSTRAINT FK_Gerant_Immeuble
FOREIGN KEY (NomGerant) REFERENCES Personne(Nom);