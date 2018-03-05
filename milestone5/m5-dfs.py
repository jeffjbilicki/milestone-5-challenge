#!/usr/bin/env python

# Given this graph
graph = {'A' : ['B','S'],
    'B' : ['A'],
    'C' : ['D','E','F','S'],
    'D' : ['C'],
    'E' : ['C','H'],
    'F' : ['C','G'],
    'G' : ['F','S'],
    'H' : ['E','G'],
    'S' : ['A','C','G']
}

# Write a depth first search to visit every node in the graph count the number of edges traversed
def dfs_visit(graph, start):
    count = 0
    queue = [start]

    return count

ans = dfs_visit(graph, 'A')
print(ans)
