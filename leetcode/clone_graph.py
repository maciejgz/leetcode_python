# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        
    def __str__(self):
        neighbors_vals = [neighbor.val for neighbor in self.neighbors]
        return f"Node(val={self.val}, neighbors={neighbors_vals})"
    
    def addVal(self, node):
        self.neighbors.append(node)


from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None

        if not node.neighbors:
            return Node(node.val, [])

        ## solution
        visited_nodes = {}
        
        def dfs(node):
            if node in visited_nodes:
                return visited_nodes[node]

            clone = Node(node.val)
            visited_nodes[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        
        return dfs(node)
        


if __name__ == "__main__":
    solution = Solution()

    nodeEmpty = Node(0, [])


    node1 = Node(1, None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node4 = Node(4, None)
    
    node1.addVal(node2)
    node1.addVal(node4)
    node2.addVal(node4)
    node2.addVal(node2)
    node3.addVal(node1)
    node3.addVal(node2)
    node4.addVal(node1)
    node4.addVal(node2)
    

    print(solution.cloneGraph(nodeEmpty))
    print(solution.cloneGraph(None))
    print(solution.cloneGraph(node1))
