import Fonction
import os

conn = Fonction.connect_to_database()

path_to_csv_directory = 'Mariage'
try:

    # Ajout des données pour le mariage
    for filename in os.listdir(path_to_csv_directory):
        if filename.endswith('.csv'):
            csv_file_path = os.path.join(path_to_csv_directory, filename)
            print(f"Processing {csv_file_path}...")

            # Process the file
            try:
                df = Fonction.addMariage(csv_file_path,filename)
                if len(df.columns)==6:
                    Fonction.copy_from_stringio(conn, df, 'statistique_mariage', ('nom_dep','typmar', 'id_departement', 'libelle_var', 'nbmaries','sexe'))
                else :
                    Fonction.copy_from_stringio(conn, df, 'statistique_mariage', ('nom_dep','typmar', 'id_departement', 'libelle_var', 'nbmaries'))
                print(f"Data from {filename} loaded successfully.")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

    # Ajout des données pour les series temporelles
    Fonction.addALLColonnes(conn, csv_file = 'base-cc-serie-historique-2020_csv/base-cc-serie-historique-2020.CSV')


finally:
    # Close the database connection
    conn.close()
    print("Database connection closed.")