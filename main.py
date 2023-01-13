from Algo import Graph, BruteForce, Greedy, GreedyOpti, Prim, MinimumWeightEdges, BranchAndBound
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

    if config.show_info:
        print("Algorithme de poids minimum".center(50, "-"))
    minimum_weight_edges = MinimumWeightEdges(
        config.city_numbers, graph.get_vertices())
    path = minimum_weight_edges.compute()
    dist = graph.compute_distance_by_path(path)
    if config.show_info:
        print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
        print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

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
    if config.show_info:
        print("Algorithme de la demi-somme".center(50, "-"))
    branch_and_bound = BranchAndBound(
        config.city_numbers, graph.get_vertices()
    )
    path = branch_and_bound.compute()
    dist = graph.compute_distance_by_path(path)
    if config.show_info:
        print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
        print("Chemin parcouru:\033[92m", [s + 1 for s in path], "\033[0m")

    # Test matplotlib
    """
    path_brute_force = []
    path_weight = []
    path_greedy = []
    for _ in range(1000000):
        graph = Graph(n=config.city_numbers, vertices=None)
        brute_force = BruteForce(n=config.city_numbers, vertices=graph.get_vertices())
        greedy = Greedy(config.city_numbers, graph.get_vertices())
        minimum_weight_edges = MinimumWeightEdges(config.city_numbers, graph.get_vertices())

        path_greedy.append(graph.compute_distance_by_path(greedy.compute()))
        path_brute_force.append(graph.compute_distance_by_path(brute_force.compute()))
        path_weight.append(graph.compute_distance_by_path(minimum_weight_edges.compute()))

    print(sum(path_greedy) / len(path_greedy))
    print(sum(path_brute_force) / len(path_brute_force))
    print(sum(path_weight) / len(path_weight))
    """
