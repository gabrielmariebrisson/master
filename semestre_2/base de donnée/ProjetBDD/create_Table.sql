CREATE TABLE Libelle (
    VAR_ID VARCHAR(255) PRIMARY KEY,
    VAR_LIB VARCHAR(255) NOT NULL,
    VAR_LIB_LONG VARCHAR(1000)
);

CREATE TABLE Commune (
    id_com VARCHAR PRIMARY KEY,
    nom_ville VARCHAR(255) NOT NULL,
    id_departement VARCHAR
);

CREATE TABLE Statistique (
    id_statistique SERIAL PRIMARY KEY,
    valeur FLOAT ,
    date_debut DATE NULL,
    date_fin DATE NULL,
    id_libelle VARCHAR(255) NOT NULL,
    id_com VARCHAR NOT NULL,
    FOREIGN KEY (id_libelle) REFERENCES Libelle(VAR_ID),
    FOREIGN KEY (id_com) REFERENCES Commune(id_com)
);

CREATE TABLE Region (
    id_region INT PRIMARY KEY,
    nom_region VARCHAR(255) NOT NULL,
    chef_lieu VARCHAR,
    FOREIGN KEY (chef_lieu) REFERENCES Commune(id_com)
);

CREATE TABLE Departement (
    id_departement VARCHAR PRIMARY KEY,
    nom_departement VARCHAR(255) NOT NULL,
    chef_lieu VARCHAR,
    id_region INT,
    FOREIGN KEY (chef_lieu) REFERENCES Commune(id_com),
    FOREIGN KEY (id_region) REFERENCES Region(id_region)
);

CREATE TABLE Statistique_mariage (
    id_statistique SERIAL PRIMARY KEY,
    nom_dep VARCHAR NOT NULL,
    typmar VARCHAR NOT NULL,
    id_departement VARCHAR NOT NULL,
    libelle_var VARCHAR NOT NULL,
    NBmaries INT NOT NULL,
    sexe VARCHAR,
    FOREIGN KEY (nom_dep) REFERENCES Libelle(VAR_ID),
    FOREIGN KEY (typmar) REFERENCES Libelle(VAR_ID),
    FOREIGN KEY (id_departement) REFERENCES Departement(id_departement),
    FOREIGN KEY (libelle_var) REFERENCES Libelle(VAR_ID),
    FOREIGN KEY (sexe) REFERENCES Libelle(VAR_ID)
);

ALTER TABLE Commune
ADD CONSTRAINT fk_departement
FOREIGN KEY (id_departement) REFERENCES Departement(id_departement);
