from .greedy import Greedy
from typing import Tuple
import numpy as np

#TODO Regler le probleme de boucle infini
class GreedyOpti(Greedy):
    def compute(self):
        base = super().compute()
        return self.remove_intersections(base)

    def compute_lines(self, path: np.ndarray) -> np.ndarray:
        res = []
        for n in range(len(path)):
            coords = (self.vertices[path[n]], self.vertices[path[(n+1) % len(path)]])
            # a = (yf - yd) / (xf - xd)
            a = (coords[1][1] - coords[0][1]) / (coords[1][0] - coords[0][0])
            # b = yd - xda
            b = coords[0][1] - coords[0][0] * a
            res.append((a, b))
        return np.array(res)

    def compute_line(self, path, point) -> Tuple[float, float]:
        """Compute the lines going from the point"""
        n = point
        coords = (self.vertices[path[n]], self.vertices[path[(n+1) % len(path)]])
        # a = (yf - yd) / (xf - xd)
        a = (coords[1][1] - coords[0][1]) / (coords[1][0] - coords[0][0])
        # b = yd - xda
        b = coords[0][1] - coords[0][0] * a
        return a, b
    """ 
    def remove_intersections(self, path: np.ndarray, lines: np.ndarray) -> np.ndarray:
            for couple in list(combinations(range(len(path)), 2)):
                line_couple = (lines[couple[0]], lines[couple[1]])
                # résoudre ax1 + b1 = ax2 + b2 pour x
                # (a1 - a2)x = b2 - b1
                # x = (b2 - b1)/(a1 - a2)
                print(line_couple[1][1],line_couple[0][1],'\n', line_couple[0][0], line_couple[1][0])
                x = (line_couple[1][1] - line_couple[0][1]) / \
                    (line_couple[0][0] - line_couple[1][0])
                x_depart_1 = self.vertices[path[couple[0]]][0]
                x_arrive_1 = self.vertices[path[(couple[0]+1) % len(path)]][0]
                x_depart_2 = self.vertices[path[couple[1]]][0]
                x_arrive_2 = self.vertices[path[(couple[1]+1) % len(path)]][0]
                # si xdépart < x < xarrivé ou xdépart > x > xarrivé
                # print(x, x_depart_1, x_arrive_1, '\n', couple)
                if ((x < max(x_depart_1, x_arrive_1) - 0.001 and x > min(x_depart_1, x_arrive_1) + 0.001) or
                     (x < max(x_depart_2, x_arrive_2) - 0.001 and x > min(x_depart_2, x_arrive_2) + 0.001)):
                    print(x,'\n', x_depart_1, x_arrive_1, '\n', x_depart_2, x_arrive_2)
                    print(self.draw_path(path))
                    return True, path
            return False, path
    """
    def remove_intersections(self, path: np.ndarray) -> np.ndarray:
        lines = self.compute_lines(path) 
        pointsToCheck = list(path.copy())
        while pointsToCheck != []:
            currentPoint = pointsToCheck[0]
            hasCol = False
            for n in range(len(path)):
                currentPointIndex = np.flatnonzero(path == currentPoint)[0]
                otherPointIndex = np.flatnonzero(path == n)[0]
                print("Index : ", currentPointIndex, otherPointIndex)
                if currentPointIndex == otherPointIndex or \
                    (currentPointIndex + 1) % len(path) == otherPointIndex or \
                    (currentPointIndex - 1) % len(path) == otherPointIndex:
                    continue
                # Si les points sont directements connectés (adjacent ou égaux)
                xD1 = self.vertices[currentPoint][0]
                xA1 = self.vertices[path[(currentPointIndex + 1) % len(path)]][0]
                line1 = lines[currentPointIndex]
                xD2 = self.vertices[n][0]
                xA2 = self.vertices[path[(otherPointIndex + 1) % len(path)]][0]
                line2 = lines[otherPointIndex]
                # résoudre ax1 + b1 = ax2 + b2 pour x
                # (a1 - a2)x = b2 - b1
                # x = (b2 - b1)/(a1 - a2)
                #print("b", line2[1], line1[1],"a", line1[0], line2[0])
                x = (line2[1] - line1[1]) / (line1[0] - line2[0])
                print("Points: ", currentPoint, n)
                #print(xD1, xD2, '\n', xA1, xA2, x)
                if ((x < max(xD1, xA1) + 0.001 and x > min(xD1, xA1) - 0.001) and
                     (x < max(xD2, xA2) + 0.001 and x > min(xD2, xA2) - 0.001)):
                    print("CROISEMENT")
                    hasCol = True
                    # Arriver ici signifie que la ligne partante de currentPoint vers B
                    #   intersecte avec la ligne partante de n vers D
                    # path : ... currentPoint - B ... n - D...
                    #   deviens ... currentPoint - n ... B - D ...
                    # TODO : A test
                    path[currentPointIndex + 1:otherPointIndex + 1] = \
                        path[otherPointIndex:currentPointIndex:-1]
                    # Recalculer les 2 droites qui change
                    # (D'autres changent avec a = -a mais pas important)
                    lines[currentPointIndex] = self.compute_line(
                        path, currentPointIndex)
                    lines[n] = self.compute_line(path, n)
                    # On ajoute l'autre point si pas déja présent
                    if len(np.flatnonzero(np.array(pointsToCheck) == n)) != 0:
                        pointsToCheck.append(n)
                    break
                print("")
            if not hasCol:
                pointsToCheck.remove(currentPoint)
        return path