"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: "Node | None") -> "Node | None":
        if node is None:
            return None

        copies = {}

        def clone(current):
            if current in copies:
                # this stops the call stack from calling clone(neighbor) again
                return copies[current]

            # initializes current.neighbors as a list
            new_node = Node(current.val)
            copies[current] = new_node

            for neighbor in current.neighbors:
                new_node.neighbors.append(clone(neighbor))

            return new_node # return the first node

        return clone(node)