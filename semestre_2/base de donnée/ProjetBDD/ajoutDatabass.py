import pandas as pd
import psycopg2

try:
    conn = psycopg2.connect(
        user="gmariebrisso",
        password='AA.rapido100.fr',
        #password=input("Entrez le mot de passe : "),
        host="pgsql"
    )
    print("Connexion réussie.")
except psycopg2.Error as e:
    print("Erreur lors de la connexion à la base de données :", e)

csv_file = 'France/v_region_2023.csv'
df = pd.read_csv(csv_file)

df.drop(columns=['CHEFLIEU', 'TNCC', 'NCCENR', 'LIBELLE'], inplace=True)
#print(df)

cur = conn.cursor()
with open(csv_file, 'r', encoding='utf-8') as file:
    next(file)  # Skip header
    cur.copy_from(file, , sep=',', null='', columns=('id_region', 'nom_region', 'chef_lieu'))

"""
#analyser donnée
DatasetClear = []
with open(csv_file, 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Ignorer l'en-tête si nécessaire
    print("Connection reussi")
    for row in reader:
        for 


with open(csv_file, 'r', encoding='utf-8') as file:
    cur.copy_from(file, 'votre_table', sep=',', null='')  # Remplacez 'votre_table' par le nom de votre table
"""