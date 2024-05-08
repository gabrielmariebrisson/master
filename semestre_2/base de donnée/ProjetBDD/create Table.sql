CREATE TABLE Libelle (
    VAR_ID INT PRIMARY KEY,
    VAR_LIB VARCHAR(255),
    VAR_LIB_LONG VARCHAR(500)
);

CREATE TABLE Statistique (
    id_statistique SERIAL PRIMARY KEY,
    valeur INT,
    date_debut DATE NULL,
    date_fin DATE NULL,
    id_libelle INT, 
    FOREIGN KEY (id_libelle) REFERENCES Libelle(VAR_ID)
);

CREATE TABLE commune (
    id_com INT PRIMARY KEY,
    nom_ville VARCHAR(255),
    id_departement INT,
    id_statistique INT,
    FOREIGN KEY (id_statistique) REFERENCES Statistique(id_statistique)
);

CREATE TABLE region (
    id_region INT PRIMARY KEY,
    nom_region VARCHAR(255),
    chef_lieu INT NULL,
    FOREIGN KEY (chef_lieu) REFERENCES commune(id_com) 
);

CREATE TABLE departement (
    id_departement INT PRIMARY KEY,
    nom_departement VARCHAR(255),
    chef_lieu INT NULL,
    id_region INT,
    FOREIGN KEY (chef_lieu) REFERENCES commune(id_com),
    FOREIGN KEY (id_region) REFERENCES region(id_region)
);

CREATE TABLE Statistique_mariage(
    id_statistique SERIAL PRIMARY KEY,
    valeur INT,
    date_debut DATE NULL,
    date_fin DATE NULL,
    id_libelle VARCHAR(255),
    FOREIGN KEY (id_libelle) REFERENCES Libelle(VAR_ID)
);

CREATE TABLE RelationMariage(
    typmar2 VARCHAR(255),

)

-- rajouter les base de donnée en 2 fois pour simuler le rajout d'une annnée*
--  faire un copy a la place de faire lige par ligne
