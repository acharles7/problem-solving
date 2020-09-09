'''
841. Keys and Rooms https://leetcode.com/problems/keys-and-rooms/
'''

def can_visit_all_rooms(rooms):
    visited = {0}
    stack = [rooms[0]]

    while stack:
        keys = stack.pop(0)

        for key in keys:
            if key not in visited:
                visited.add(key)
                stack.append(rooms[key])
    return len(visited) == len(rooms)

rooms = [[1],[2],[3],[]]
can_visit_all_rooms(rooms)
