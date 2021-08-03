# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        coef = {}
        for i in range(len(points)):
            p0 = points[i]
            for j in range(1, len(points)):
                p1 = points[j]
                # Here a line is k0*x + y + b = 0 or x + b = 0
                if p0.x == p1.x:
                    k0 = 1
                    k1 = 0
                    b = -p0.x
                else:
                    k0 = (p0.y - p1.y) * 1.0 / (p0.x - p1.x)
                    k1 = -1
                    b = p0.y - k0*p0.x
                tup = (k0, k1, b)
                if coef.get(tup):
                    coef[tup] += 1
                else:
                    coef[tup] = 1
        return max(coef.values())