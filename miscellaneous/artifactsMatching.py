from collections import defaultdict

'''
https://www.chegg.com/homework-help/questions-and-answers/task-davy-buried-\
pieces-ancient-artifacts-underground-artifacts-hidden-area-split-nxn-grid-q51996391
'''

def get_all_artifacts(points):
    d1, d2 = points[0], points[1]

    x1, y1 = int(d1[:-1]) - 1, ord(d1[-1]) - ord('A')
    x2, y2 = int(d2[:-1]) - 1, ord(d2[-1]) - ord('A')

    if x1 == x2 and y1 == y2:
        return [[x1, y1]]

    elif x1 == x2:
        if abs(y2 - y1) == 1:
            return [(x1, y1), (x1, y2)]
        elif abs(y2 - y1) == 2:
            return [(x1, y1), (x1, y1 + 1), (x1, y2)]
        elif abs(y2 - y1) == 3:
            return [(x1, y1), (x1, y1 + 1), (x1, y1 + 2), (x1, y2)]

    elif y1 == y2:
        if abs(x2 - x1) == 1:
            return [(x1, x2), (y1, y2)]
        elif abs(x2 - x1) == 2:
            return [(x1, x2), (x1 + 1, y1), (y1, y2)]
        else:
            return [(x1, x2), (x1 + 1, y1), (x1 + 2, y1)(y1, y2)]

    else:
        xc, yc = (x1 + x2) / 2, (y1 + y2) / 2
        xd, yd = (x1 - x2) / 2, (y1 - y2) / 2

        x3, y3 = int(xc - yd), int(yc + xd)
        x4, y4 = int(xc + yd), int(yc - xd)
        return [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]


def convert_points(points):
    return [str(x + 1) + chr(ord('A') + y) for x, y in points]


def solution(n, artifacts, searched):
    finished, unfinished = 0, 0
    jack_artifacts = set(searched.split())
    artifacat_dict = defaultdict(list)

    for idx, artifact in enumerate(artifacts.split(',')):
        artifact_list = convert_points(get_all_artifacts(artifact.split()))
        artifacat_dict[(idx, len(artifact_list))].extend(artifact_list)

    for (_, length), artifacts in artifacat_dict.items():
        count = sum(
            [1 for artifact in artifacts if artifact in jack_artifacts])
        if count == length:
            finished += 1
        elif count > 0:
            unfinished += 1
    return [finished, unfinished]


# n = 4
# artifacts = '1B 2C, 2D 4D'
# searched = '2B 2D 3D 4D 4A'

n = 12
artifacts = '1A 2A,12A 12A'
searched = '12A'

solution(n, artifacts, searched)