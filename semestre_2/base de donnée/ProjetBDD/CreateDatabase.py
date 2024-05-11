import Fonction
import pandas as pd

conn = Fonction.connect_to_database()

if conn:
    cursor = conn.cursor()
    try:
        cursor.execute('CREATE SCHEMA IF NOT EXISTS "ProjetBDD";')
        conn.commit()
        print("Schema 'ProjetBDD' created successfully.")
    except psycopg2.Error as e:
        print("An error occurred:", e)
else:
    print("Failed to connect to the database.")

Fonction.executer_sql(conn, 'create_Table.sql')

#Creation de la france
Fonction.copy_from_stringio(conn, Fonction.create_df_region(), 'region', ('id_region', 'nom_region', 'chef_lieu'))
Fonction.copy_from_stringio(conn, Fonction.create_df_departement(), 'departement', ('id_departement', 'nom_departement', 'chef_lieu', 'id_region'))
Fonction.copy_from_stringio(conn, Fonction.create_df_commune(), 'commune', ('id_com', 'nom_ville', 'id_departement'))

Fonction.add_cheflieu(conn, pd.read_csv('France/v_departement_2023.csv'), 'departement', 'DEP')
Fonction.add_cheflieu(conn, pd.read_csv('France/v_departement_2023.csv'), 'region', 'REG')

#creation libeller pour les stats
Fonction.copy_from_stringio(conn, Fonction.create_df_libeller_pop(), 'libelle', ('var_id', 'var_lib', 'var_lib_long'))
Fonction.copy_from_stringio(conn, Fonction.create_df_libeller_mariage(), 'libelle', ('var_id', 'var_lib', 'var_lib_long'))

