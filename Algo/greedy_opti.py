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

    def compute_line2(self, pd, pf):
        # a = (yf - yd) / (xf - xd)
        a = (pf[1] - pd[1]) / (pf[0] - pd[0])
        # b = yd - xda
        b = pd[1] - pd[0] * a
        return a, b
    
    def check_croisement(self, p1d, p1f, p2d, p2f):
        """Check if the line p1d - p1f cross the line p2d - p2f)"""
        # Calcule les 2 droites
        line1 = self.compute_line2(p1d, p1f)
        line2 = self.compute_line2(p2d, p2f)
        # résoudre ax1 + b1 = ax2 + b2 pour x
        # (a1 - a2)x = b2 - b1
        # x = (b2 - b1)/(a1 - a2)
        x = (line2[1] - line1[1]) / (line1[0] - line2[0])
        return ((x < max(p1d[0], p1f[0]) + 0.01 and x > min(p1d[0], p1f[0]) - 0.01) and
             (x < max(p2d[0], p2f[0]) + 0.01 and x > min(p2d[0], p2f[0]) - 0.01))
        
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
                p1d = self.vertices[currentPoint]
                p1f = self.vertices[path[(currentPointIndex + 1) % len(path)]]
                p2d = self.vertices[n]
                p2f = self.vertices[path[(otherPointIndex + 1) % len(path)]]
                if (self.check_croisement(p1d, p1f, p2d, p2f)):
                    hasCol = True
                    self.hessMeter += 1
                    oldDist = self.compute_distance_by_path(path)
                    if self.hessMeter >= 20:
                        print("Points : ", currentPoint, n, p1d, p1f, p2d, p2f)
                        print("Index : ", currentPointIndex, otherPointIndex)
                        print("Droite : ", lines[currentPointIndex], lines[otherPointIndex])
                        if self.hessMeter >= 25:
                            print("Boucle?")
                            return path
                    # Arriver ici signifie que la ligne partante de currentPoint vers B
                    #   intersecte avec la ligne partante de n vers D
                    # path : ... currentPoint - B ... n - D...
                    #   deviens ... currentPoint - n ... B - D ...
                    minPointIndex = min(currentPointIndex, otherPointIndex)
                    maxPointIndex = max(currentPointIndex, otherPointIndex)
                    path[minPointIndex + 1:maxPointIndex + 1] = \
                        path[maxPointIndex:minPointIndex:-1]
                    newDist = self.compute_distance_by_path(path)
                    if newDist > oldDist :
                        print("C la mer noir")
                    # On ajoute l'autre point n si pas déja présent
                    if n not in pointsToCheck:
                        pointsToCheck.append(n)
                    break
            if not hasCol:
                pointsToCheck.remove(currentPoint)
        return path