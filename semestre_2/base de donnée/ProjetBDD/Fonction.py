import pandas as pd
import psycopg2
from io import StringIO
from psycopg2 import sql
from collections import defaultdict
import re
from datetime import datetime
import os



def connect_to_database():
    try:
        conn = psycopg2.connect(
            user="gmariebrisso",
            password='AA.rapido100.fr',
            host="pgsql",
            database="gmariebrisso",
            options='-c search_path="ProjetBDD"'
        )
        print("Connexion réussie.")
        return conn
    except psycopg2.Error as e:
        print("Erreur lors de la connexion à la base de données:", e)
        return None


def create_df_region():
    csv_file = 'France/v_region_2023.csv'
    df = pd.read_csv(csv_file)

    # Nettoyage et préparation du DataFrame
    df.drop(columns=['CHEFLIEU', 'TNCC', 'NCCENR', 'LIBELLE'], inplace=True)
    df['chef_lieu'] = None
    df.columns = ['id_region', 'nom_region', 'chef_lieu']
    return df

def create_df_departement():
    csv_file = 'France/v_departement_2023.csv'
    df = pd.read_csv(csv_file)

    # Nettoyage et préparation du DataFrame
    df.drop(columns=['CHEFLIEU', 'TNCC', 'NCCENR', 'LIBELLE'], inplace=True)
    df['chef_lieu'] = None
    df.columns = ['id_departement', 'id_region', 'nom_departement', 'chef_lieu']
    df = df[['id_departement', 'nom_departement', 'chef_lieu', 'id_region']] 
    return df

def create_df_commune():
    csv_file = 'France/v_commune_2023.csv'
    df = pd.read_csv(csv_file)
    
    # Nettoyage et préparation du DataFrame
    df = df[(df['TYPECOM'] == 'COM') | (df['TYPECOM'] == 'ARM')]
    df.drop(columns=['TYPECOM', 'CTCD', 'REG', 'ARR', 'TNCC', 'NCCENR', 'LIBELLE', 'CAN', 'COMPARENT'], errors='ignore', inplace=True)
    df.columns = ['id_com', 'id_departement', 'nom_ville']
    df = df[['id_com', 'nom_ville', 'id_departement']] 
    return df

def aViolerContraine(id_probleme,error_msg, conn, df, table, columns):
    # Check for foreign key violation for 'id_probleme'
    if "viole la contrainte de clé" in error_msg and id_probleme in error_msg:
        # Extract the problematic 'id_probleme' from the error message
        match = re.search(r'\('+id_probleme+'\)=\((\d+)\)', error_msg)
        if match:
            problem_id = int(match.group(1))
            print(f"La clé ("+id_probleme+")=({problem_id}) n'est pas présente dans la table 'commune'.")

            # Remove the rows with the problematic 'id_probleme'
            initial_count = len(df)
            df = df[df[id_probleme] != problem_id]
            print(f"{initial_count - len(df)} ligne(s) supprimée(s) du DataFrame en raison d'une clé étrangère manquante.")

            print("DataFrame après suppression des lignes problématiques :")
            print(df)
            copy_from_stringio(conn, df, table, columns)
        else:
            print("Erreur lors de l'extraction de l'ID problématique.")

def copy_from_stringio(conn, df, table, columns):
    buffer = StringIO()

    # Vérifiez si '' est présent dans le DataFrame pour le remplacer par <NA>
    if (df == '').any().any():
        df = df.replace('', pd.NA)
    df.to_csv(buffer, index=False, header=False, sep=',', na_rep='\\N')
    buffer.seek(0)

    try:
        with conn.cursor() as cur:
            cur.copy_from(buffer, table, sep=',', columns=columns)
            conn.commit()
            print(f"Données chargées avec succès dans la table '{table}'.")
    except psycopg2.Error as e:
        conn.rollback()
        error_msg = str(e)
        print("Erreur lors du chargement des données :", error_msg)
        
        aViolerContraine('id_com',error_msg, conn, df, table, columns)
        aViolerContraine('id_departement',error_msg, conn, df, table, columns)

def add_cheflieu(conn, df, nom_table, nom_column_id):
    # Prépare la requête SQL sans utiliser de paramètres pour les identifiants
    query_template = sql.SQL("""
        UPDATE {table}
        SET chef_lieu = %s
        WHERE {id_column} = %s;
    """).format(
        table=sql.Identifier(nom_table),
        id_column=sql.Identifier('id_' + nom_table)
    )

    try:
        with conn.cursor() as cur:
            for index, row in df.iterrows():
                # Exécute la requête avec les bons paramètres
                cur.execute(query_template, (row['CHEFLIEU'], row[nom_column_id]))
            conn.commit()  # Commit après toutes les insertions pour la performance
            print(f"Données chargées avec succès dans la table '{nom_table}'.")
    except psycopg2.Error as e:
        conn.rollback()  # Rollback en cas d'erreur
        print(f"Erreur lors du chargement des données dans la table {nom_table} :", e)


def delete_date(text):
    keywords = [' entre ', ' en ']
    for keyword in keywords:
        if keyword in text:
            return text.split(keyword)[0]
    return text


def create_df_libeller_pop():
    csv_file = 'base-cc-serie-historique-2020_csv/meta_base-cc-serie-historique-2020.CSV'
    df = pd.read_csv(csv_file, delimiter=';')

    # Nettoyage et préparation du DataFrame
    df.drop(columns=[ 'COD_MOD', 'LIB_MOD', 'TYPE_VAR', 'LONG_VAR'], inplace=True)
    df.columns = ['var_id', 'var_lib', 'var_lib_long']
    df = df[df['var_id'] != 'CODGEO']

    new_data = {
        'var_id': df['var_id'].str.split('_').str[-1].str.replace(r'[0-9]', '', regex=True),
        'var_lib': [delete_date(text) for text in df['var_lib']],
        'var_lib_long': [delete_date(text) for text in df['var_lib_long']]
    }
    new_df = pd.DataFrame(new_data)
    new_df = new_df.drop_duplicates(subset=['var_lib'])

    return new_df

def recuperer_indice(dataframe):
    name_columns = dataframe.columns.str.split('_').str[-1].str.replace(r'[0-9]', '', regex=True)
    indices_dict = defaultdict(list)
    for index, value in enumerate(name_columns):
        indices_dict[value].append(index)
    return indices_dict.items()

def createDate(date):
    try:
        # Initialize variables
        date_debut, date_fin = "", ""
        
        if len(date) == 2:
            year = int(date)
            if year < 30:
                date_debut = f'20{date}-01-01'
                date_fin = f'20{date}-12-31'
            else:
                date_debut = f'19{date}-01-01'
                date_fin = f'19{date}-12-31'

        elif len(date) == 4:
            date_debut = date[:2]
            date_fin = date[2:4]

            year_debut = int(date_debut)
            year_fin = int(date_fin)

            if year_debut < 30:
                date_debut = f'20{date_debut}-01-01'
            else:
                date_debut = f'19{date_debut}-01-01'
            
            if year_fin < 30:
                date_fin = f'20{date_fin}-12-31'
            else:
                date_fin = f'19{date_fin}-12-31'
        return date_debut, date_fin

    except Exception as e:
        print(f"Error processing date: {date} -> {str(e)}")
    
    return None, None

def create_df_statitistique(conn, commune, df, libelle):
    new_df = pd.DataFrame(columns=['valeur', 'date_debut', 'date_fin', 'id_libelle', 'id_com'])

    for column in df.columns:
            date_text = re.sub(r'[a-zA-Zéàêèôâîï\-_]', '', column)
            date_debut, date_fin = createDate(date_text)
            news_columns = pd.DataFrame({
                'valeur': df[column].values,
                'date_debut': date_debut,
                'date_fin': date_fin,
                'id_libelle': libelle,
                'id_com': commune.iloc[:,0]
            })
            
            new_df = pd.concat([new_df, news_columns], ignore_index=True)
    print("Data prepared successfully.")

    return new_df


def addALLColonnes(conn, csv_file):
    df = pd.read_csv(csv_file, delimiter=';', low_memory=False)

    commune = df.iloc[:, :1]
    df = df.iloc[:, 1:]

    tableau_ajout = recuperer_indice(df)
    print("Ajout de chaque premiere labelle pour tester")
    for key, value in tableau_ajout:
        print("labelle :", key)
        new_df = create_df_statitistique(conn, commune, df.iloc[:, value[:1]], key)
        copy_from_stringio(conn, new_df, 'statistique', ('valeur', 'date_debut', 'date_fin', 'id_libelle', 'id_com'))

    print("Ajout du reste des colonnes")
    for key, value in tableau_ajout:
        if value[1:] and (key=='RSECOCC' or key=='LOGVAC' or key=='PMEN'):
            print("labelle :", key)
            new_df = create_df_statitistique(conn, commune, df.iloc[:, value[1:]], key)
            copy_from_stringio(conn, new_df, 'statistique', ('valeur', 'date_debut', 'date_fin', 'id_libelle', 'id_com'))

def is_not_integer(x):
    if 'XX' in x:
        return False
    
    if '_' in x:
        return True
    
    try:
        if float(x) == int(float(x)):
            return False
    except ValueError:
        return True
    return False

def create_df_libeller_mariage():

    new_data = {
        'var_id': ['H', 'F', 'HF', 'HH-FF', 'HH', 'FF', 'HF-H', 'HF-F', '14_19', '20_24', '25_29', '30_34', '35_39', '40_49', '50_59', '60_PL', 'FR_FR', 'FR_ETR', 'ETR_ETR'],
        'var_lib': ['Hommes', 'Femmes', 'Mariages entre personnes de sexe différent', 'Mariages entre personnes de même sexe', 'Mariages entre hommes', 'Mariages entre femmes', 'Mariages entre personnes de sexe différent - Hommes', 'Mariages entre personnes de sexe différent - Femmes', 'Moins de 20 ans', 'De 20 à 24 ans', 'De 25 à 29 ans', 'De 30 à 34 ans', 'De 35 à 39 ans', 'De 40 à 49 ans', 'De 50 à 59 ans', '60 ans ou plus', 'Les deux époux(se) né(e)s en France', 'Couples mixtes', 'Les deux époux(ses) né(e)s à l\'étranger'],
    }
    new_df = pd.DataFrame(new_data)

    titre_choisi = {
        'var_id': ['Janv', 'Fev', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Aou', 'Sep', 'Oct', 'Nov', 'Dec', 'CELIB', 'VEUF', 'DIVO','Dep1.csv','Dep2.csv','Dep3.csv','Dep4.csv','Dep5.csv','Dep6.csv'],
        'var_lib': ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre', 'Célibataires', 'Veufs / Veuves', 'Divorcés / Divorcées','Groupe d\'âges des époux selon le département et la région de mariage. Année 2021','État matrimonial antérieur des époux selon le département et la région de mariage. Année 2021','Groupe d\'âges des époux se mariant pour la première fois selon le département et la région de mariage. Année 2021','Nationalité des époux selon le département et la région de domicile conjugal. Année 2021', 'Pays de naissance des époux selon le département et la région de domicile conjugal. Année 2021', 'Répartition mensuelle des mariages selon le département et la région de mariage. Année 2021']
    }
    titre_choisi_df = pd.DataFrame(titre_choisi)

    new_df = pd.concat([new_df, titre_choisi_df], ignore_index=True)
    new_df['var_lib_long'] = None

    return new_df

month_mapping = {
    '01' : 'Janv',
    '02' : 'Fev',
    '03' : 'Mar',
    '04' : 'Avr',
    '05' : 'Mai',
    '06' : 'Juin',
    '07' : 'Juil',
    '08' : 'Aou',
    '09' : 'Sep',
    '10' : 'Oct',
    '11' : 'Nov',
    '12' : 'Dec'
}

etat_mariage_mapping = {
    '1' : 'CELIB',
    '3' : 'VEUF',
    '4' : 'DIVO',

}


def addMariage(csv_file, filename):
    df = pd.read_csv(csv_file, delimiter=';', low_memory=False)
    df.isetitem(1, df.iloc[:, 1].apply(lambda x: x[2:] if len(x) == 4 else x))

    df.isetitem(1, pd.to_numeric(df.iloc[:, 1], errors='coerce'))
    df = df[pd.notnull(df.iloc[:, 1])]
    df.isetitem(1, df.iloc[:, 1].astype(int))
    df.isetitem(1, df.iloc[:, 1].astype(str).apply(lambda x: x.zfill(2)))
    
    df = df[~df.iloc[:, 2].astype(str).str.contains('TOTAL')]

    if df.columns[2]=='MMAR':
        df = df[~df.iloc[:, 2].astype(str).str.contains('AN')]
        df.iloc[:, 2] = df.iloc[:, 2].replace(month_mapping)
    df.insert(0, 'nom_dep', filename)
    if df.columns[4]=='ETAMAT':
        df = df[~df.iloc[:, 4].astype(str).str.contains('E')]
        df.iloc[:, 4] = df.iloc[:, 4].replace(etat_mariage_mapping)
        df.columns = ['nom_dep','typmar', 'id_departement', 'sexe','libelle_var','nbmaries']
        df = df.loc[:, ['nom_dep','typmar', 'id_departement','libelle_var','nbmaries','sexe']]
        return df

    df.columns= ['nom_dep','typmar', 'id_departement', 'libelle_var','nbmaries']
    return df

def executer_sql(conn, sql_file):
    with open(sql_file, 'r') as file:
        sql_script = file.read()

    # Execute the SQL script
    conn.cursor().execute(sql_script)
    conn.commit()