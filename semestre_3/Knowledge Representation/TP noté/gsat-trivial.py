##20 a 100 var, de longueur 3, et m clauses =1*n m clauses =1.25*n puis m clauses =4.5*n

#Avoir un tot d'exploration qui flip de facon 
#pas refaire le flip sur un flip deja fait

#renvoyer le nombre de filp
#trouver la methode qui sastifait la clause

#tableau Nombre de filp
#tableau Nombre de faux

import random
import numpy as np
import matplotlib.pyplot as plt
import time

# Modified SAT solver with the requested improvements

def generate_random_assignment(variables):
    return {var: random.choice([True, False]) for var in variables}

def evaluate_formula(assignment, formula):
    return all(any(assignment.get(abs(lit), False) if lit > 0 else not assignment.get(abs(lit), False) for lit in clause) for clause in formula)

def count_satisfied_clauses(assignment, formula):
    return sum(1 for clause in formula if any(assignment.get(abs(lit), False) if lit > 0 else not assignment.get(abs(lit), False) for lit in clause))

def select_variable_to_flip(assignment, formula):
    best_var = None
    best_increase = -1
    current_satisfied = count_satisfied_clauses(assignment, formula)

    for var in assignment:
        # Flip variable
        assignment[var] = not assignment[var]
        flipped_satisfied = count_satisfied_clauses(assignment, formula)
        
        increase = flipped_satisfied - current_satisfied
        if increase > best_increase:
            best_increase = increase
            best_var = var
        
        # Unflip variable
        assignment[var] = not assignment[var]
    
    return best_var

def gsat(formula, max_flips, max_tries):
    variables = set(abs(lit) for clause in formula for lit in clause)
    flips_count = 0

    for _ in range(max_tries):
        assignment = generate_random_assignment(variables)
        
        for _ in range(max_flips):
            if evaluate_formula(assignment, formula):
                return flips_count, assignment
            
            var_to_flip = select_variable_to_flip(assignment, formula)
            if var_to_flip is not None:
                assignment[var_to_flip] = not assignment[var_to_flip]
                flips_count += 1
        
    return flips_count, None



################# VERSION OPTIMISER ############################

def select_variable_to_flip_with_exploration(assignment, formula, flipped_vars, exploration_rate):
    current_satisfied = count_satisfied_clauses(assignment, formula)
    unsatisfied_clauses = [clause for clause in formula if not any(assignment.get(abs(lit), False) if lit > 0 else not assignment.get(abs(lit), False) for lit in clause)]
    variables_in_unsatisfied = set(abs(lit) for clause in unsatisfied_clauses for lit in clause)

    if not variables_in_unsatisfied:
        return None  # No unsatisfied clauses, so nothing to flip

    # Apply exploration rate (random move among unsatisfied variables)
    if random.random() < exploration_rate:
        return random.choice(list(variables_in_unsatisfied))

    # Otherwise, apply greedy approach: select the best variable to flip
    best_var = None
    best_increase = -1
    for var in variables_in_unsatisfied:
        if var in flipped_vars:
            continue  # Ignore already flipped variables

        # Flip the variable
        assignment[var] = not assignment[var]
        flipped_satisfied = count_satisfied_clauses(assignment, formula)

        increase = flipped_satisfied - current_satisfied
        if increase > best_increase:
            best_increase = increase
            best_var = var

        # Undo the flip
        assignment[var] = not assignment[var]

    return best_var

def gsat_with_exploration(formula, max_flips, max_tries, exploration_rate):
    variables = set(abs(lit) for clause in formula for lit in clause)

    for _ in range(max_tries):
        assignment = generate_random_assignment(variables)
        flips_count = 0
        flipped_vars = set()

        for _ in range(max_flips):
            if evaluate_formula(assignment, formula):
                return flips_count, assignment  # Fully satisfied formula

            var_to_flip = select_variable_to_flip_with_exploration(assignment, formula, flipped_vars, exploration_rate)
            if var_to_flip is None:
                break  # No more flips to make

            assignment[var_to_flip] = not assignment[var_to_flip]
            flipped_vars.add(var_to_flip)
            flips_count += 1

        # Restart with a new random assignment if not solved
    return flips_count, assignment

# Function to generate random SAT formulas
def generate_random_formula(n, m):
    formula = []
    for _ in range(m):
        clause = []
        for _ in range(3):  # Each clause contains 3 literals (3-SAT)
            literal = random.randint(1, n) * random.choice([-1, 1])
            clause.append(literal)
        formula.append(clause)
    return formula

######################### PARAMETERS #####################################

# Test parameters
n_values = [50,100,150]
ratios = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.2, 4.25]  # Ratios m/n
max_flips = 1000
max_tries = 10
exploration_rate = 0.1  # Exploration rate of 10%

# Variables pour stocker les résultats des expérimentations

satisfiability_by_flips = {}
satisfiability_by_ratio = {}
flips_by_ratio = {}

satisfiability_by_flips_NON_OPTI = {}
satisfiability_by_ratio_NON_OPTI = {}
flips_by_ratio_NON_OPTI = {}

# Initialisation des dictionnaires pour les différentes valeurs de n
for n in n_values:
    satisfiability_by_flips[n] = []
    satisfiability_by_ratio[n] = []
    flips_by_ratio[n] = []

    satisfiability_by_flips_NON_OPTI[n] = []
    satisfiability_by_ratio_NON_OPTI[n] = []
    flips_by_ratio_NON_OPTI[n] = []

time_by_ratio_opti = {}
time_by_ratio_non_opti = {}

for n in n_values:
    time_by_ratio_opti[n] = []
    time_by_ratio_non_opti[n] = []

######################### EXPERIENCE #####################################
for n in n_values:
    print("n = ",n)
    for ratio in ratios:
        print("ratio = ",ratio)
        m = int(ratio * n)  # Calcul du nombre de clauses
        formula = generate_random_formula(n, m)

        # Optimized GSAT
        start_time_opti = time.time()
        flips, final_assignment = gsat_with_exploration(formula, max_flips, max_tries, exploration_rate)
        if final_assignment != None and formula != None :
            satisfied_clauses = count_satisfied_clauses(final_assignment, formula)
        else:
            satisfied_clauses_NON_OPTI = 0
        end_time_opti = time.time()

        # Calcul du temps écoulé pour la version optimisée
        elapsed_time_opti = end_time_opti - start_time_opti
        time_by_ratio_opti[n].append(elapsed_time_opti)

        # Non-optimized GSAT
        if (ratio < 2.5 and n== 50) and (ratio < 2 and n== 100)  and (n != 150):
            start_time_non_opti = time.time()
            flips_NON_OPTI, final_assignment_NON_OPTI = gsat(formula, max_flips, max_tries)
            if final_assignment_NON_OPTI != None and formula != None :
                satisfied_clauses_NON_OPTI = count_satisfied_clauses(final_assignment_NON_OPTI, formula)
            else:
                satisfied_clauses_NON_OPTI = 0
            end_time_non_opti = time.time()

            # Calcul du temps écoulé pour la version non-optimisée
            elapsed_time_non_opti = end_time_non_opti - start_time_non_opti
            time_by_ratio_non_opti[n].append(elapsed_time_non_opti)
            print("non opti = ", elapsed_time_non_opti )
        print("opti = ", elapsed_time_opti)

        # Stocker les résultats pour les graphiques
        satisfiability_by_flips[n].append((satisfied_clauses / m) * 100)
        flips_by_ratio[n].append(flips)
        satisfiability_by_ratio[n].append((satisfied_clauses / m) * 100)

        if (ratio < 2.5 and n== 50) and (ratio < 2 and n== 100)  and (n != 150):
            satisfiability_by_flips_NON_OPTI[n].append((satisfied_clauses_NON_OPTI / m) * 100)
            flips_by_ratio_NON_OPTI[n].append(flips_NON_OPTI)
            satisfiability_by_ratio_NON_OPTI[n].append((satisfied_clauses_NON_OPTI / m) * 100)


######################### ANALYSE #####################################

# Graphique 1: Satisfiability (%) vs Number of Flips (Opti vs Non-Opti)
plt.figure(figsize=(12, 6))
for n in n_values:
    plt.plot(flips_by_ratio[n], satisfiability_by_flips[n], marker='o', label=f"Opti n={n}")
plt.title("Satisfiability (%) vs Number of Flips (Opti vs Non-Opti)")
plt.xlabel("Number of Flips")
plt.ylabel("Satisfiability (%)")
plt.grid(True)
plt.legend()

# Graphique 2: Satisfiability (%) vs Ratio (m/n) (Opti vs Non-Opti)
plt.figure(figsize=(12, 6))
for n in n_values:
    plt.plot(ratios, satisfiability_by_ratio[n], marker='o', label=f"Opti n={n}")
plt.title("Satisfiability (%) vs Ratio (m/n) (Opti vs Non-Opti)")
plt.xlabel("Ratio (m/n)")
plt.ylabel("Satisfiability (%)")
plt.grid(True)
plt.legend()

# Graphique 3: Nombre moyen de flips vs Ratio (m/n) (Opti vs Non-Opti)
plt.figure(figsize=(12, 6))
for n in n_values:
    plt.plot(ratios, flips_by_ratio[n], marker='o', label=f"Opti n={n}")
plt.title("Average Number of Flips vs Ratio (m/n) (Opti vs Non-Opti)")
plt.xlabel("Ratio (m/n)")
plt.ylabel("Average Number of Flips")
plt.grid(True)
plt.legend()

# Graphique 4: Temps moyen de calcul vs Ratio (m/n) pour différentes valeurs de n (Opti vs Non-Opti)
plt.figure(figsize=(12, 6))
for n in n_values:
    plt.plot(ratios, flips_by_ratio[n], marker='o', label=f"Opti n={n}")
    plt.plot(ratios, flips_by_ratio_NON_OPTI[n], marker='x', linestyle='--', label=f"Non-Opti n={n}")
plt.title("Average Number of Flips vs Ratio (m/n) (Opti vs Non-Opti)")
plt.xlabel("Ratio (m/n)")
plt.ylabel("Average Number of Flips")
plt.grid(True)
plt.legend()

plt.show()

# Graphique 1: Satisfiability (%) vs Number of Flips (Opti vs Non-Opti)
plt.figure(figsize=(12, 6))
for n in [50,100]:
    plt.plot(flips_by_ratio_NON_OPTI[n], satisfiability_by_flips_NON_OPTI[n], marker='x', linestyle='--', label=f"Non-Opti n={n}")
plt.title("Satisfiability (%) vs Number of Flips (Opti vs Non-Opti)")
plt.xlabel("Number of Flips")
plt.ylabel("Satisfiability (%)")
plt.grid(True)
plt.legend()

# Graphique 2: Satisfiability (%) vs Ratio (m/n) (Opti vs Non-Opti)
plt.figure(figsize=(12, 6))
for n in [50,100]:
    plt.plot(ratios, satisfiability_by_ratio_NON_OPTI[n], marker='x', linestyle='--', label=f"Non-Opti n={n}")
plt.title("Satisfiability (%) vs Ratio (m/n) (Opti vs Non-Opti)")
plt.xlabel("Ratio (m/n)")
plt.ylabel("Satisfiability (%)")
plt.grid(True)
plt.legend()

# Graphique 3: Nombre moyen de flips vs Ratio (m/n) (Opti vs Non-Opti)
plt.figure(figsize=(12, 6))
for n in [50,100]:
    plt.plot(ratios, flips_by_ratio_NON_OPTI[n], marker='x', linestyle='--', label=f"Non-Opti n={n}")
plt.title("Average Number of Flips vs Ratio (m/n) (Opti vs Non-Opti)")
plt.xlabel("Ratio (m/n)")
plt.ylabel("Average Number of Flips")
plt.grid(True)
plt.legend()

plt.show()
