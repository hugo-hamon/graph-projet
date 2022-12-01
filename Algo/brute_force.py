from itertools import permutations
from .graph import Graph
import numpy as np


class BruteForce(Graph):

    def __init__(self, n: int, vertices: np.ndarray) -> None:
        super().__init__(n, vertices)

    def compute(self) -> np.ndarray:
        """Return the shortest path computed by the algorithm"""
        return self.__brute_force()

    def __brute_force(self) -> np.ndarray:
        """Brute force algorithm"""
        if self.n > 11:
            raise ValueError("Too much vertices for brute force algorithm")
        paths = np.array(list(permutations(range(self.n))), dtype=np.uint8)
        distances = self.compute_list_distance_by_path(paths)
        return paths[np.argmin(distances)]
