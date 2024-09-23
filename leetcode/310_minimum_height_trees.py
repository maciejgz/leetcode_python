from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0 or edges is None:
            return None
        
        if n == 1:
            return [0]
        
        adj = [set() for _ in range(n)]
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
            
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves
        return leaves
    
    
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))