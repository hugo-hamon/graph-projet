import matplotlib.pyplot as plt
from itertools import product
from typing import Tuple
import numpy as np


class Graph:

    def __init__(self, n: int) -> None:
        self.n = n
        self.vertices = np.random.uniform(0, 1, (n, 2))
        self.distances = np.zeros((n, n))

    # REQUESTS
    def euclidean_distance(self, v1: np.ndarray, v2: np.ndarray) -> float:
        """Return the euclidean distance between two vertices"""
        return np.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)

    def get_vertices(self) -> np.ndarray:
        """Return a copy of the vertices"""
        return self.vertices.copy()

    def p_voisin(self, vertex: np.ndarray) -> Tuple[np.ndarray, float]:
        """Greedy algorithm by nearest neighbour return the list of vertices and the distance"""
        already_visited = np.array([vertex])
        vertices = self.get_vertices()
        vertices = np.delete(vertices, np.where((vertices == vertex).all(axis=1))[0][0], axis=0)
        dist = 0
        while len(vertices) > 0:
            nearest_vertex = vertices[np.argmin([self.euclidean_distance(vertex, v) for v in vertices])]
            dist += self.euclidean_distance(vertex, nearest_vertex)
            already_visited = np.append(already_visited, [nearest_vertex], axis=0)
            vertices = np.delete(vertices, np.where((vertices == nearest_vertex).all(axis=1))[0][0], axis=0)
            vertex = nearest_vertex
        dist += self.euclidean_distance(already_visited[0], already_visited[-1])
        return already_visited, dist

    # COMMANDS
    def compute_distance(self) -> None:
        """Compute the distance matrix"""
        X = self.vertices[:, 0]
        Y = self.vertices[:, 1]
        self.distances = np.sqrt((X[:, None] - X) ** 2 + (Y[:, None] - Y) ** 2)
        

    # TOOLS
    def plot(self) -> None:
        """Plot the graph"""
        for i, j in product(range(self.n), range(self.n)):
            if self.distances[i, j] != 0:
                plt.plot(
                    [self.vertices[i][0], self.vertices[j][0]],
                    [self.vertices[i][1], self.vertices[j][1]],
                    '-o', color='black', alpha=0.3, markersize=10, linewidth=1
                )
        plt.show()
