import numpy as np
import csv

# Data licensed under CC-BY
# Hannah Ritchie, Lucas Rodés-Guirao, Edouard Mathieu, Marcel Gerber, Esteban Ortiz-Ospina, Joe Hasell and Max Roser (2023) - "Population Growth". Published online at OurWorldInData.org. Retrieved from: 'https://ourworldindata.org/population-growth' [Online Resource]

def get_world_population():
    """Returns a 2D array description the evolution of the world population.
    First column correponds to the year, second one to the world population.
    Data from 'https://ourworldindata.org/population-growth'."""
    with open('population-regions-with-projections.csv', 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = np.array(data)
    data = data[1:, :]
    world_population = np.array([[int(line[2]), int(line[3])] for line in data if line[0] == 'World' and int(line[2]) >= 0 and int(line[2]) <= 2020])
    return world_population