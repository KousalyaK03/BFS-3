# Explain your approach in brief:
# This approach uses a DFS traversal to clone the graph. 
# A hash map is used to store already cloned nodes to avoid redundant work and infinite recursion.

# Time Complexity: O(N + E), where N is the number of nodes and E is the number of edges.
# Space Complexity: O(N), for storing visited nodes in the hash map and the recursion stack.
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Hash map to store cloned nodes
        cloned_nodes = {}

        def dfs(current: Node) -> Node:
            # If the node is already cloned, return it
            if current in cloned_nodes:
                return cloned_nodes[current]

            # Clone the current node
            cloned_node = Node(current.val)
            cloned_nodes[current] = cloned_node

            # Recursively clone all neighbors
            for neighbor in current.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))
            
            return cloned_node

        # If the input node is None, return None
        if not node:
            return None
        
        # Start DFS from the given node
        return dfs(node)
