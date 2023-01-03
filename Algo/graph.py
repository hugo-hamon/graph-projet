import matplotlib.pyplot as plt
from itertools import product
from typing import List
import numpy as np


class Graph:

    def __init__(self, n: int, vertices=None) -> None:
        """Initialize the graph with n vertices. If vertices is None, generate random vertices"""
        if (vertices is None):
            self.n = n
            self.vertices = np.random.uniform(0, 1, (n, 2))
        else:
            self.n = vertices.shape[0]
            self.vertices = vertices
        self.distances = np.zeros((self.n, self.n))
        self.__compute_distance()

    # REQUESTS
    def get_vertices(self) -> np.ndarray:
        """Return a copy of the vertices"""
        return self.vertices.copy()

    def get_distances(self) -> np.ndarray:
        """Return a copy of the distances matrix"""
        return self.distances.copy()

    def compute_distance_by_path(self, L: np.ndarray) -> float:
        """Compute the distance of a path L and return it"""
        return sum(self.distances[L[:-1], L[1:]]) + self.distances[L[0], L[-1]]

    def compute_list_distance_by_path(self, Ll: np.ndarray) -> np.ndarray:
        """Compute a list of distances from a list of paths L and return it"""
        return np.sum(self.distances[Ll[:, :-1], Ll[:, 1:]], axis=1) + self.distances[Ll[:, 0], Ll[:, -1]]

    # COMMANDS
    def __compute_distance(self) -> None:
        """Compute the distance matrix"""
        X = self.vertices[:, 0]
        Y = self.vertices[:, 1]
        self.distances = np.sqrt((X[:, None] - X) ** 2 + (Y[:, None] - Y) ** 2)

    def get_nearest_vertex(self, v1: int) -> int:
        """Return the nearest vertex by index"""
        temp_value, self.distances[v1, v1] = self.distances[v1, v1], np.inf
        min_, self.distances[v1, v1] = int(
            np.argmin(self.distances[v1])), temp_value
        return min_

    def get_nearest_vertex_not_in_list(self, v1: int, L: List[int]) -> int:
        """Return the nearest vertex by index where the vertex index is not in L"""
        if v1 not in L:
            L.append(v1)
        temp_value, self.distances[v1, L] = self.distances[v1, L], np.inf
        min_, self.distances[v1, L] = int(
            np.argmin(self.distances[v1])), temp_value
        return min_

    def compute(self) -> np.ndarray:
        """return the shortest path computed by the algorithm"""
        return NotImplemented

    # TOOLS
    def euclidean_distance(self, v1: np.ndarray, v2: np.ndarray) -> float:
        """Return the euclidean distance between two vertices"""
        return np.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)

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
        for n in range(len(path)):
            i, j = (self.vertices[path[n]],
                    self.vertices[path[(n+1) % len(path)]])
            plt.plot([i[0], j[0]], [i[1], j[1]],
                     '-o', color='black', markersize=10, linewidth=1
                     )
            plt.annotate(str(n), i, textcoords="offset points",
                         xytext=(0, 10), color="red")
        plt.show()
