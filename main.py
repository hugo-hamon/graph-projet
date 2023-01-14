from Algo import Graph, BruteForce, Greedy, GreedyOpti, Prim, MinimumWeightEdges, BranchAndBound
import matplotlib.pyplot as plt
from config import Config
from time import time


config_filepath = "config.json"


if __name__ == '__main__':
    # Load config
    config = Config()
    config.load_config(config_filepath)
    paths = {}

    # Create the graph
    graph = Graph(n=config.city_numbers, vertices=None)
    if config.show_graph:
        print("Matrice des distances:")
        graph.print_distances()

    # --2.0 Algorithme de brut froce--
    if config.brute_force and config.city_numbers <= 10:
        paths["brute_force"] = []
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
    paths["greedy"] = []
    greedy = Greedy(config.city_numbers, graph.get_vertices())
    start = time()
    path = greedy.compute()
    if config.execution_time:
        print("Temps d'exécution:\033[92m", round(time() - start, 3), "\033[0m")
    dist = greedy.compute_distance_by_path(path)
    if config.show_info:
        print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
        print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

    # --2.2 Algorithme du plus proche voisin amélioré--
    if config.show_info:
        print("Algorithme du plus proche voisin amélioré".center(50, "-"))
    paths["greedy_opti"] = []
    greedy_opti = GreedyOpti(config.city_numbers, graph.get_vertices())
    start = time()
    path = greedy_opti.compute()
    if config.execution_time:
        print("Temps d'exécution:\033[92m", round(time() - start, 3), "\033[0m")
    dist = greedy.compute_distance_by_path(path)
    if config.show_info:
        print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
        print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

    # --2.3 Algorithme arête de poids minimum--

    if config.show_info:
        print("Algorithme de poids minimum".center(50, "-"))
    paths["minimum_weight"] = []
    minimum_weight_edges = MinimumWeightEdges(
        config.city_numbers, graph.get_vertices())
    start = time()
    path = minimum_weight_edges.compute()
    if config.execution_time:
        print("Temps d'exécution:\033[92m", round(time() - start, 3), "\033[0m")
    dist = graph.compute_distance_by_path(path)
    if config.show_info:
        print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
        print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

    # --2.4 Algorithme arbre couvrant de poids minimum--

    if config.show_info:
        print("Algorithme de prim".center(50, "-"))
    paths["prim"] = []
    prim = Prim(config.city_numbers, graph.get_vertices())
    start = time()
    path = prim.compute()
    if config.execution_time:
        print("Temps d'exécution:\033[92m", round(time() - start, 3), "\033[0m")
    dist = graph.compute_distance_by_path(path)
    if config.show_info:
        print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
        print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

    # --2.5 Algorithme heuristique de la demi-somme--
    if config.show_info:
        print("Algorithme de la demi-somme".center(50, "-"))
    if config.city_numbers <= 10:
        paths["branch_and_bound"] = []
        branch_and_bound = BranchAndBound(
            config.city_numbers, graph.get_vertices()
        )
        path = branch_and_bound.compute()
        dist = graph.compute_distance_by_path(path)
        if config.show_info:
            print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
            print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

    # Test matplotlib
    for _ in range(config.iterations_numbers):
        graph = Graph(n=config.city_numbers, vertices=None)
        if config.city_numbers <= 10 and config.brute_force:
            brute_force = BruteForce(n=config.city_numbers, vertices=graph.get_vertices())
            paths["brute_force"].append(graph.compute_distance_by_path(brute_force.compute()))


        greedy = Greedy(config.city_numbers, graph.get_vertices())
        paths["greedy"].append(graph.compute_distance_by_path(greedy.compute()))

        greedy_opti = GreedyOpti(config.city_numbers, graph.get_vertices())
        paths["greedy_opti"].append(graph.compute_distance_by_path(greedy_opti.compute()))

        minimum_weight_edges = MinimumWeightEdges(config.city_numbers, graph.get_vertices())
        paths["minimum_weight"].append(graph.compute_distance_by_path(minimum_weight_edges.compute()))

        prim = Prim(config.city_numbers, graph.get_vertices())
        paths["prim"].append(graph.compute_distance_by_path(prim.compute()))
        if config.city_numbers <= 10:
            branch_and_bound = BranchAndBound(config.city_numbers, graph.get_vertices())
            paths["branch_and_bound"].append(graph.compute_distance_by_path(branch_and_bound.compute()))

    plt.bar(list(paths.keys()), [sum(v) / len(v) if len(v) > 0 else 0 for v in paths.values()], width=0.5, color="maroon")
    plt.xlabel("Algorithmes")
    plt.ylabel("Distance moyenne")
    plt.title(f"Moyenne des distances parcourues pour {config.city_numbers} villes")
    plt.show()
