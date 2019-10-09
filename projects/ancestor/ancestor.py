# Suppose we have some input data describing a graph of relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
# For example, in this diagram and the sample input, 3 is a child of 1 and 2, and 5 is a child of 4:

# Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. If the input individual has no parents, the function should return -1.

# If I keep talking to myself they're going to put in a funny farm.
# What do I know that I need?
# parents, children, ancestors
# (parent, child)
# vertices
# need something to test
# this is the test data # test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

'''
 10
 /
1   2   4  11
 \ /   / \ /
  3   5   8
   \ / \   \
    6   7   9
'''


# def earliest_ancestor(ancestors, starting_node):  
#     # create a vertices dictionary for the pairs
#     vertices = {}
#     # loop through the ancestors
#     for j in ancestors:
#         # we know that parent comes first in the pairs, so parent will be 0, child 1
#         parent = j[0]
#         child = j[1]
#         # if the child isn't in a vertices, make a set and add a parent
#         if child not in vertices:
#             vertices[child] = set()
#             vertices[child].add(parent)
#         # if it is, add a parent
#         elif vertices[child]:
#             vertices[child].add(parent)
from collections import defaultdict

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def dfs(starting_vertex, family):
    visited = []
    ss = Stack()
    ss.push([starting_vertex])
    while ss.size() > 0:
        path = ss.pop()
        vertex = path[-1]
        if vertex not in visited:
            visited.append(vertex)
        for neighbor in family[vertex]:
            path_copy = [*path]
            path_copy.append(neighbor)
            ss.push(path_copy)
    return visited[-1]
def earliest_ancestor(ancestors, starting_node):
    family = defaultdict(list)
    for parent, child in ancestors:
        family[child].append(parent)
    if starting_node not in family:
        return -1
    ancestor = dfs(starting_node, family)
    return ancestor