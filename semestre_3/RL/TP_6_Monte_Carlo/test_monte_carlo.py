import grid_world
import monte_carlo

# Crée un environnement GridWorld de taille 4x4 avec 3 "trous"
env = grid_world.GridWorldMDP(height=4, width=4, number_of_holes=3)

# Crée un agent MonteCarlo dans cet environnement
agent = monte_carlo.MonteCarloAgent(env)

# Génère un épisode (une séquence d'états, d'actions et de récompenses)
episode = agent.generate_episode()

# Affiche l'épisode généré
print("Episode généré:", episode)

# Mets à jour la fonction de valeur d'état V à partir de l'épisode généré
agent.update_V(episode)

# Affiche la valeur de V mise à jour
print("Valeurs de V mises à jour:", agent.V)

# (Optionnel) Mets à jour la fonction de valeur d'état-action Q
agent.update_Q(episode)

# Affiche la valeur de Q mise à jour
print("Valeurs de Q mises à jour:", agent.Q)
