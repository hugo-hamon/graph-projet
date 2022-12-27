from typing import List, Tuple
from itertools import product
from .graph import Graph
import numpy as np
import heapq


class Prim(Graph):

    def __init__(self, n: int, vertices=None) -> None:
        super().__init__(n, vertices)

    def compute(self) -> np.ndarray:
        """Compute the minimum spanning tree of the graph"""
        return self.__heap_prim(0)

    def __prim(self, s: int) -> np.ndarray:
        """Compute the minimum spanning tree of the graph"""
        path = [s]
        while len(path) < self.n:
            possible_edges = self.__get_possible_edges(path)
            possible_edges.sort(key=lambda x: x[1])
            path.append(possible_edges[0][0][1])
        return np.array(path)

    def __heap_prim(self, s: int) -> np.ndarray:
        """Compute the minimun spanning tree of the graph using a heap"""
        path = [s]
        heap = []
        for i in range(self.n):
            if i != s:
                heapq.heappush(heap, (self.distances[s, i], s, i))
        while len(path) < self.n:
            _, s, i = heapq.heappop(heap)
            if i not in path:
                path.append(i)
                for j in range(self.n):
                    if j not in path:
                        heapq.heappush(heap, (self.distances[i, j], i, j))
        return np.array(path)

    def __get_possible_edges(self, path: List[int]) -> List[Tuple[Tuple[int, int], int]]:
        """Return the couple of possible edges and the distance between them"""
        return [((s, i), self.distances[s, i]) for s, i in product(path, range(self.n))
                if (s in path and i not in path) or (s not in path and i in path)]
