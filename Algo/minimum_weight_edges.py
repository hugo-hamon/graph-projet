from typing import List, Tuple, Set
from itertools import product
from .graph import Graph
import numpy as np


class MinimumWeightEdges(Graph):

    def __init__(self, n: int, vertices=None) -> None:
        super().__init__(n, vertices)
        self.copy_distances = self.distances.copy()

    def compute(self) -> np.ndarray:
        """Compute the solution"""
        return self.minimum_weight_edges()

    def minimum_weight_edges(self) -> np.ndarray:
        """Compute the minimum weight edges of the graph"""
        path = []
        while len(path) < self.n:
            min_edges = self.__get_minimum_weight_edge()
            if not self.__is_close_graph(min_edges, path):
                if min_edges[0] not in path:
                    path.append(min_edges[0])
                if min_edges[1] not in path:
                    path.append(min_edges[1])
                
        return np.array(path)

    def __is_close_graph(self, points: List[int], path: List[int]) -> bool:
        """Return True if the graph is close"""
        if len(points) != 2:
            raise ValueError("The points must be of length 2")
        return points[1] in path and points[0] in path

    def __get_minimum_weight_edge(self) -> List[int]:
        min_edges = [(), np.inf]
        for i, distance in enumerate(self.copy_distances):
            for j, weight in enumerate(distance):
                if i != j and weight < min_edges[1]:
                    min_edges = [(i, j), weight]
        self.copy_distances[min_edges[0][0], min_edges[0][1]] = np.inf
        self.copy_distances[min_edges[0][1], min_edges[0][0]] = np.inf
        return [min_edges[0][0], min_edges[0][1]]
