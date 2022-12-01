from itertools import combinations
from .greedy import Greedy
import numpy as np


class GreedyOpti(Greedy):

    def compute(self):
        self.base = super().compute()
        lines = self.compute_lines(self.base)
        return self.remove_intersections(self.base, lines)

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
                    # print("Path before: ", path, "Couple: ", (couple[0]+1), couple[1] + 1)
                    path[(couple[0]+1):couple[1] +
                         1] = path[(couple[0]+1):couple[1]+1][::-1]
                    lines = self.compute_lines(path)
                    # print("Path after: ", path)
                    # print(self.draw_path(path))
                    break
        return path