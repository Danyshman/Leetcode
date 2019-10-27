import math


def kClosest(points, K):
    d = dict()
    for point in points:
        d[tuple(point)] = (math.sqrt(((point[0] - 0)**2) + (point[1] - 0)**2))
    sorted_list = sorted(d.items(), key=lambda x:x[1])
    ans = []
    index = 0
    while K > 0:
        ans.append(list(sorted_list[index][0]))
        index += 1
        K -= 1
    return ans


print(kClosest(points = [[3,3],[5,-1],[-2,4]], K = 2))