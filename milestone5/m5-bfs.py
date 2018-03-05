#!/usr/bin/env python

# Given this graph
graph = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}

# Write a BFS search that will return the shortest path
def bfs_shortest_path(graph, start, goal):
    explored = []
    # keep track of all the paths to be checked
    queue = [start]

    # return path if start is goal
    if start == goal:
        return "Home sweet home!"

    # Find the shortest path to the goal

    return "Cannot reach goal"

ans = bfs_shortest_path(graph,'G', 'A')
print(ans)
