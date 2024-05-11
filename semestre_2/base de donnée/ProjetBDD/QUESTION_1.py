import psycopg2
import Fonction


def afficher_libelle(conn):
    with conn.cursor() as cur:
        cur.execute("""
        SELECT * FROM "ProjetBDD"."libelle";""",)
        list_libelle = cur.fetchall()
        for lib in list_libelle:
            print(f"key : {lib[0]} - abreviation: {lib[1]} - explication: {lib[2]}")


def list_departments_by_region(conn, region_name):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT d.nom_departement
            FROM departement d
            JOIN region r ON d.id_region = r.id_region
            WHERE r.nom_region = %s;
        """, (region_name,))
        departments = cur.fetchall()
        print(f"Departments in {region_name}:")
        for dept in departments:
            print(dept[0])

def list_communes_by_libelle(conn, department_name,libelle, min_population):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT c.nom_ville, s.valeur, s.date_debut
            FROM commune c
            JOIN statistique s ON c.id_com = s.id_com
            JOIN departement d ON c.id_departement = d.id_departement
            WHERE d.nom_departement = %s
              AND s.id_libelle = %s
              AND s.valeur > %s ;
        """, (department_name, libelle, min_population, ))
        communes = cur.fetchall()
        print(f"Communes in {department_name} with more than {min_population} :")
        for commune in communes:
            print(f"{commune[0]} - {libelle}: {commune[1]} - Date: {commune[2]}")

def most_and_least_libelle_regions(conn, libelle, annee):
    with conn.cursor() as cur:
        cur.execute("""
            SELECT r.nom_region, SUM(s.valeur) as total_population
            FROM commune c
            JOIN departement d ON c.id_departement = d.id_departement
            JOIN region r ON d.id_region = r.id_region
            JOIN statistique s ON c.id_com = s.id_com
            WHERE s.id_libelle = %s
            AND s.date_debut = %s
            GROUP BY r.id_region, r.nom_region
            ORDER BY total_population DESC;
        """, (libelle, f'{annee}-01-01'))
        regions = cur.fetchall()
        if regions:
            print(f"Most {libelle} region: {regions[0][0]} - {libelle}: {regions[0][1]}")
            print(f"Least {libelle} region: {regions[-1][0]} - {libelle}: {regions[-1][1]}")


def main():
    conn = Fonction.connect_to_database()
    if conn:
        try:
            afficher_libelle(conn)
            print()
            list_departments_by_region(conn, 'NOUVELLE AQUITAINE')
            list_communes_by_libelle(conn, 'GIRONDE', 'POP', 50000)
            most_and_least_libelle_regions(conn, 'POP','2020')

            print()
            list_communes_by_libelle(conn, 'GIRONDE', 'DECE', 1000)
            most_and_least_libelle_regions(conn, 'DECE','2020')

            print()
            list_communes_by_libelle(conn, 'GIRONDE', 'LOG', 50000)
            most_and_least_libelle_regions(conn, 'LOG','2020')
        finally:
            conn.close()
            print("Database connection closed.")

if __name__ == "__main__":
    main()
