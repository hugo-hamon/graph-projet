from Algo import Graph, BruteForce, Greedy, GreedyOpti, Prim
import matplotlib.pyplot as plt
from config import Config


config_filepath = "config.json"


if __name__ == '__main__':
    # Load config
    config = Config()
    config.load_config(config_filepath)

    # Create the graph
    graph = Graph(n=config.city_numbers, vertices=None)
    if config.show_graph:
        print("Matrice des distances:")
        graph.print_distances()

    # --2.0 Algorithme de brut froce--
    if config.brute_force:
        brute_force = BruteForce(
            n=config.city_numbers, vertices=graph.get_vertices())
        if config.show_info:
            print("Algorithme de brut force".center(50, "-"))
        path = brute_force.compute()
        dist = brute_force.compute_distance_by_path(path)
        if config.show_info:
            print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
            print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

    # --2.1 Algorithme du plus proche voisin--
    if config.show_info:
        print("Algorithme du plus proche voisin".center(50, "-"))
    greedy = Greedy(config.city_numbers, graph.get_vertices())
    path = greedy.compute()
    dist = greedy.compute_distance_by_path(path)
    if config.show_info:
        print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
        print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

    # --2.2 Algorithme du plus proche voisin amélioré--

    # --2.3 Algorithme arête de poids minimum--

    # --2.4 Algorithme arbre couvrant de poids minimum--

    if config.show_info:
        print("Algorithme de prim".center(50, "-"))
    prim = Prim(config.city_numbers, graph.get_vertices())
    path = prim.compute()
    dist = graph.compute_distance_by_path(path)
    if config.show_info:
        print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
        print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

    # --2.5 Algorithme heuristique de la demi-somme--
