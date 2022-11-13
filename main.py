from config import Config
from graph import Graph

config_filepath = "config.json"


if __name__ == '__main__':
    # Load config
    config = Config()
    config.load_config(config_filepath)

    # Create graph
    graph = Graph(config.city_numbers)
    graph.compute_distance()
    print("Matrice des distances:")
    # graph.print_distances_by_min_colored()

    # --2.1 Algorithme du plus proche voisin--
    print("Algorithme du plus proche voisin".center(50, "-"))
    L, dist = graph.p_voisin(0)
    print("Distance parcourue:\033[92m", round(dist, 2), "\033[0m")
    print("Chemin parcouru:\033[92m", [s + 1 for s in L], "\033[0m")

    # --2.2 Algorithme du plus proche voisin amélioré--

    # --2.3 Algorithme arête de poids minimum--

    # --2.4 Algorithme arbre couvrant de poids minimum--

    # --2.5 Algorithme heuristique de la demi-somme--
