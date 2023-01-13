from queue import PriorityQueue
from .graph import Graph
from typing import Tuple
import numpy as np


class BranchAndBound(Graph):

    def __init__(self, n: int, vertices=None):
        super().__init__(n, vertices)
        self.best_distance = np.inf
        self.best_solution = None

    def compute(self) -> np.ndarray:
        return self.__branch_and_bound(0)

    def __branch_and_bound(self, s: int) -> np.ndarray:
        queue = PriorityQueue()
        queue.put((0, s, np.array([s], dtype=np.int32), 0))
        while not queue.empty():
            upper_bound, city, path, distance = queue.get()
            if len(path) == self.n:
                distance += self.distances[city][s]
                if distance < self.best_distance:
                    self.best_distance = distance
                    self.best_solution = path
            else:
                for next_city in np.setdiff1d(np.arange(self.n), path):
                    new_distance = distance + self.distances[city][next_city]
                    new_path = np.append(path, next_city)
                    remaining_cities = np.setdiff1d(
                        np.arange(self.n), new_path)
                    if remaining_cities.size != 0:
                        new_upper_bound = new_distance + \
                            np.min(self.distances[next_city, remaining_cities])
                    else:
                        new_upper_bound = new_distance
                    if new_upper_bound < self.best_distance:
                        queue.put((new_upper_bound, next_city,
                                  new_path, new_distance))
        return np.array(self.best_solution)
