import matplotlib.pyplot as plt
from itertools import product
from typing import Tuple, List
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

    def get_distances(self) -> np.ndarray:
        """Return a copy of the distances matrix"""
        return self.distances.copy()

    def get_nearest_vertex(self, v1: int) -> int:
        """Return the nearest vertex by index. Do not perform a copy of the distances matrix."""
        distances = self.get_distances()
        distances[v1, v1] = np.inf
        return int(np.argmin(distances[v1]))

    def get_nearest_vertex_not_in(self, v1: int, L: List[int]) -> int:
        """Return the nearest vertex by index not in L. Do not perform a copy of the distances matrix."""
        self.distances[v1, L] = np.inf
        return int(np.argmin(self.distances[v1]))

    def p_voisin(self, vertex_idx: int) -> Tuple[np.ndarray, float]:
        """
        Greedy algorithm by nearest neighbour not already visited return the list of vertices and the distance.
        Vertex is the index of the starting vertex.
        """
        distances = self.get_distances()
        path = [vertex_idx]
        distance = 0
        for _ in range(self.n - 1):
            nearest_vertex = self.get_nearest_vertex_not_in(vertex_idx, path)
            path.append(nearest_vertex)
            distance += self.distances[vertex_idx, nearest_vertex]
            vertex_idx = nearest_vertex
        distance += self.distances[vertex_idx, path[0]]
        self.distances = distances
        return np.array(path), distance

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

    def print_distances_by_min_colored(self) -> None:
        """Print the distances matrix"""
        for i in range(self.n):
            nearest_vertex = self.get_nearest_vertex(i)
            print("[ ", end="")
            for j in range(self.n):
                n = round(self.distances[i, j], 2)
                if j == nearest_vertex:
                    print(f"\033[92m{n:.2f}\033[0m", end=' ')
                else:
                    print(f"{n:.2f}", end=' ')
            print("]")
        print()
