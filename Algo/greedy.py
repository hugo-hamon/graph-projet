from .graph import Graph
import numpy as np


class Greedy(Graph):

    def __init__(self, n: int, vertices=None) -> None:
        super().__init__(n, vertices)

    def compute(self):
        return self.p_voisin(0)

    def p_voisin(self, vertex_idx: int) -> np.ndarray:
        """
        Greedy algorithm by nearest neighbour not already visited return the list of vertices and the distance.
        Vertex is the index of the starting vertex.
        """
        path = [vertex_idx]
        for _ in range(self.n - 1):
            nearest_vertex = self.get_nearest_vertex_not_in_list(
                vertex_idx, path
            )
            path.append(nearest_vertex)
            vertex_idx = nearest_vertex
        return np.array(path)
