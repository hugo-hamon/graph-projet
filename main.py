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
    vertices = graph.get_vertices()

    # --2.1 Algorithme du plus proche voisin--

    L, dist = graph.p_voisin(vertices[0])
    print("Distance parcourue par l'algorithme du plus proche voisin : ", round(dist, 2))

    # --2.2 Algorithme du plus proche voisin amélioré--

    # --2.3 Algorithme arête de poids minimum--

    # --2.4 Algorithme arbre couvrant de poids minimum--

    # --2.5 Algorithme heuristique de la demi-somme--
