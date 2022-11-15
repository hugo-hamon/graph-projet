import matplotlib.pyplot as plt
from itertools import product
from typing import List
import numpy as np


class Graph:

    def __init__(self, n: int) -> None:
        self.n = n
        self.vertices = np.random.uniform(0, 1, (n, 2))
        self.distances = np.zeros((n, n))
        self.__compute_distance()

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

    def compute_distance_by_path(self, L: np.ndarray) -> float:
        """Compute the distance by a path"""
        return sum(self.distances[L[i], L[(i + 1) % self.n]] for i in range(self.n))

    # COMMANDS
    def p_voisin(self, vertex_idx: int) -> np.ndarray:
        """
        Greedy algorithm by nearest neighbour not already visited return the list of vertices and the distance.
        Vertex is the index of the starting vertex.
        """
        distances = self.get_distances()
        path = [vertex_idx]
        for _ in range(self.n - 1):
            nearest_vertex = self.get_nearest_vertex_not_in(vertex_idx, path)
            path.append(nearest_vertex)
            vertex_idx = nearest_vertex
        self.distances = distances
        return np.array(path)

    def brute_force(self) -> np.ndarray:
        """Brute force algorithm"""
        if self.n > 8:
            raise ValueError("Too much vertices for brute force algorithm")
        paths = np.array([path for path in product(range(self.n), repeat=self.n) if len(set(path)) == self.n])
        distances = np.array(
            [self.compute_distance_by_path(path) for path in paths])
        return paths[np.argmin(distances)]

            
    # COMMANDS

    def __compute_distance(self) -> None:
        """Compute the distance matrix"""
        X = self.vertices[:, 0]
        Y = self.vertices[:, 1]
        self.distances = np.sqrt((X[:, None] - X) ** 2 + (Y[:, None] - Y) ** 2)

    # TOOLS
    def plot(self) -> None:
        """Plot the vertices"""
        for i, j in product(range(self.n), range(self.n)):
            if self.distances[i, j] != 0:
                plt.plot(
                    [self.vertices[i][0], self.vertices[j][0]],
                    [self.vertices[i][1], self.vertices[j][1]],
                    '-o', color='black', alpha=0.3, markersize=10, linewidth=1
                )
        plt.show()

    def print_distances(self) -> None:
        """Print the distances matrix"""
        print(np.array2string(self.distances, precision=2, floatmode='fixed'))

    def draw_path(self, path) -> None:
        """Plot the path"""
        pass
