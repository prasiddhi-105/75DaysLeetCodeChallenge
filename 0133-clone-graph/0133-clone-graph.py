# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node):
        # If graph is empty
        if not node:
            return None

        # Dictionary to store old node -> new node
        old_to_new = {}

        # DFS function
        def dfs(curr):
            # If already cloned, return it
            if curr in old_to_new:
                return old_to_new[curr]

            # Create copy of current node
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # Clone neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)