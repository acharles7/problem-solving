'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from station i to its next station (i+1).
You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once
in the clockwise direction, otherwise return -1.
'''


def optimalPoint(magic, distance):
    optimal_point, current_point = 0, 0
    index = 0
    for i in range(len(magic)):
        current_point += magic[i] - distance[i]
        optimal_point += magic[i] - distance[i]

        if current_point < 0:
            index = i+1
            current_point = 0
    if optimal_point < 0:
        return -1
    else:
        return index

magic = [2,4,5,2]
distance = [4,3,1,3]
print(optimalPoint(magic, distance))
