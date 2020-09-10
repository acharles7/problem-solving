'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, 
is it possible for you to finish all courses?
'''


from collections import defaultdict
    
def has_cycle(course, prereqs, visited, checked):
    if checked[course]: return False
    if visited[course]: return True

    visited[course] = True

    cycle = False
    for child in prereqs[course]:
        cycle = has_cycle(child, prereqs, visited, checked)
        if cycle:
            break

    visited[course] = False
    checked[course] = True
    return cycle
        
def can_finish(num_courses, prerequisites):
    prereqs = defaultdict(list)

    for course, prereq in prerequisites:
        prereqs[course].append(prereq)

    visited = [False]*num_courses
    checked = [False]*num_courses

    for course in range(num_courses):
        if has_cycle(course, prereqs, visited, checked):
            return False
    return True
    
    
num_courses = 2
prerequisites = [[0,1]]
can_finish(num_courses, prerequisites)
