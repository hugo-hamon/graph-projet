import matplotlib.pyplot as plt
from itertools import product, permutations, combinations
from typing import List
import numpy as np


class Graph:
    """Base class for all algorithm, uses bruteforce"""

    def __init__(self, n: int, vertices=None) -> None:
        if (vertices is None):
            self.n = n
            self.vertices = np.random.uniform(0, 1, (n, 2))
        else:
            self.n = vertices.shape[0]
            self.vertices = vertices
        self.distances = np.zeros((self.n, self.n))
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

    def compute_distance_by_path(self, L: np.ndarray) -> float:
        """Compute the distance of a path"""
        return sum(self.distances[L[:-1], L[1:]]) + self.distances[L[0], L[-1]]

    def compute_list_distance_by_path(self, Ll: np.ndarray) -> np.ndarray:
        """Compute a list of distances from a list of paths"""
        return np.sum(self.distances[Ll[:, :-1], Ll[:, 1:]], axis=1) + self.distances[Ll[:, 0], Ll[:, -1]]

    def compute(self):
        """return the shortest path found using the class' algorithm"""
        return self.__brute_force()

    # COMMANDS

    def __brute_force(self) -> np.ndarray:
        """Brute force algorithm"""
        if self.n > 11:
            raise ValueError("Too much vertices for brute force algorithm")
        paths = np.array(list(permutations(range(self.n))), dtype=np.uint8)
        distances = self.compute_list_distance_by_path(paths)
        return paths[np.argmin(distances)]

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
        for n in range(len(path)):
            i, j = (self.vertices[n], self.vertices[(n+1) % len(path)])
            plt.plot([i[0], j[0]], [i[1], j[1]],
                     '-o', color='black', markersize=10, linewidth=1
                     )
        plt.show()


class Greedy(Graph):
    """Greedy algorithm"""

    def compute(self):
        return self.p_voisin(0)

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

    def get_nearest_vertex(self, v1: int) -> int:
        """Return the nearest vertex by index. Do not perform a copy of the distances matrix."""
        distances = self.get_distances()
        distances[v1, v1] = np.inf
        return int(np.argmin(distances[v1]))

    def get_nearest_vertex_not_in(self, v1: int, L: List[int]) -> int:
        """Return the nearest vertex by index not in L. Do not perform a copy of the distances matrix."""
        self.distances[v1, L] = np.inf
        return int(np.argmin(self.distances[v1]))


class Greedy_opti(Greedy):
    def compute(self):
        base = super().compute()
        lines = self.compute_lines(base)
        return self.remove_intersections(base, lines)

    def compute_lines(self, path: np.ndarray) -> np.ndarray:
        res = []
        for n in range(len(path)):
            coords = (self.vertices[n], self.vertices[(n+1) % len(path)])
            # a = (yf - yd) / (xf - xd)
            a = (coords[1][1] - coords[0][1]) / (coords[1][0] - coords[0][0])
            # b = yd - xda
            b = coords[0][1] - coords[0][0] * a
            res.append((a, b))
        return np.array(res)

    def remove_intersections(self, path: np.ndarray, lines: np.ndarray) -> np.ndarray:
        has_changed = True
        while has_changed:
            has_changed = False
            for couple in list(combinations(range(len(path)), 2)):
                line_couple = (lines[couple[0]], lines[couple[1]])
                # résoudre ax1 + b1 = ax2 + b2 pour x
                # (a1 - a2)x = b2 - b1
                # x = (b2 - b1)/(a1 - a2)
                x = (line_couple[1][1] - line_couple[0][1]) / \
                    (line_couple[0][0] - line_couple[1][0])
                # fix if ou le swap
                x_depart_1 = self.vertices[path[couple[0]]][0]
                x_arrive_1 = self.vertices[path[(couple[0]+1) % len(path)]][0]
                x_depart_2 = self.vertices[path[couple[1]]][0]
                x_arrive_2 = self.vertices[path[(couple[1]+1) % len(path)]][0]
                # si xdépart < x < xarrivé ou xdépart > x > xarrivé
                # print(x, x_depart_1, x_arrive_1, '\n', couple)
                if ((x < x_depart_1 and x > x_arrive_1) or (x < x_arrive_1 and x > x_depart_1)) and \
                        ((x < x_depart_2 and x > x_arrive_2) or (x < x_arrive_2 and x > x_depart_2)):
                    has_changed = True
                    # path = ... A B ... C D...
                    # path deviens ... A C ... B D ...
                    print("Path before: ", path, "Couple: ", (couple[0]+1), couple[1] + 1)
                    path[(couple[0]+1):couple[1] + 1] = path[(couple[0]+1):couple[1]+1][::-1]
                    print("Path after: ", path)
                    print(self.draw_path(path))
                    break
        return path

# BD