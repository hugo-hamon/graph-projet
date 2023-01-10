from .greedy import Greedy
from typing import Tuple
import numpy as np

#TODO Regler le probleme de boucle infini
class GreedyOpti(Greedy):
    def compute(self):
        self.hessMeter = 0
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

    def remove_intersections(self, path: np.ndarray) -> np.ndarray:
        lines = self.compute_lines(path) 
        pointsToCheck = list(path.copy())
        while pointsToCheck != []:
            currentPoint = pointsToCheck[0]
            hasCol = False
            for n in range(len(path)):
                currentPointIndex = np.flatnonzero(path == currentPoint)[0]
                otherPointIndex = np.flatnonzero(path == n)[0]
                # Si les points sont directements connectés (adjacent ou égaux)
                if currentPointIndex == otherPointIndex or \
                    (currentPointIndex + 1) % len(path) == otherPointIndex or \
                    (currentPointIndex - 1) % len(path) == otherPointIndex:
                    continue
                xD1 = self.vertices[currentPoint][0]
                xA1 = self.vertices[path[(currentPointIndex + 1) % len(path)]][0]
                line1 = lines[currentPointIndex]
                xD2 = self.vertices[n][0]
                xA2 = self.vertices[path[(otherPointIndex + 1) % len(path)]][0]
                line2 = lines[otherPointIndex]
                # résoudre ax1 + b1 = ax2 + b2 pour x
                # (a1 - a2)x = b2 - b1
                # x = (b2 - b1)/(a1 - a2)
                x = (line2[1] - line1[1]) / (line1[0] - line2[0])
                if ((x < max(xD1, xA1) + 0.001 and x > min(xD1, xA1) - 0.001) and
                     (x < max(xD2, xA2) + 0.001 and x > min(xD2, xA2) - 0.001)):
                    hasCol = True
                    self.hessMeter += 1
                    if self.hessMeter >= 20:
                        #print("Points : ", currentPoint, n)
                        #print("Index : ", currentPointIndex, otherPointIndex)
                        #print("Droite : ")
                        if self.hessMeter >= 25:
                            print("Boucle?")
                            return path
                    # Arriver ici signifie que la ligne partante de currentPoint vers B
                    #   intersecte avec la ligne partante de n vers D
                    # path : ... currentPoint - B ... n - D...
                    #   deviens ... currentPoint - n ... B - D ...
                    path[currentPointIndex + 1:otherPointIndex + 1] = \
                        path[otherPointIndex:currentPointIndex:-1]
                    lines[currentPointIndex + 1:otherPointIndex + 1] = \
                        lines[otherPointIndex:currentPointIndex:-1]
                    # Recalculer les 2 droites qui change
                    # (D'autres changent avec ax + b = -(ax + b) mais pas important)
                    lines[currentPointIndex] = self.compute_line(
                        path, currentPointIndex)
                    lines[n] = self.compute_line(path, n)
                    # On ajoute l'autre point n si pas déja présent
                    if n not in pointsToCheck:
                        pointsToCheck.append(n)
                    break
            if not hasCol:
                pointsToCheck.remove(currentPoint)
        return path