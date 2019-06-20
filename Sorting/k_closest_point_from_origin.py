

import math
def func(k):
    return k[1]

def k_closest(points, k):
    # x1, y1 = 0, 0
    # res = []
    # pts = []
    # for pt in points:
    #     x2, y2 = pt[0], pt[1]
    #     eu_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    #     res.append([pt,eu_distance])
    # res = sorted(res, key=func)
    #
    # for i in range(k):
    #     pts.append(res[i][0])
    # return pts
    points.sort(key = lambda p: p[0]**2 + p[1]**2)
    print(points)
    return points[:k]

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
# print(points[:k])

print(k_closest(points, k))
