from typing import List, Optional


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
         
         
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        rightmost = []
        
        level0 = []
        level0.append(root)
        
        self.findRightMost(level0, rightmost)
        
        return rightmost
    
    def findRightMost(self, nodesOnDepth: List[TreeNode], rightmost: List):
        if nodesOnDepth is None or len(nodesOnDepth) == 0:
            return
        
        rightmost.append(nodesOnDepth[-1].val);
        
        nextLevelNodes = []
        for element in nodesOnDepth:
            if element.left is not None:
                nextLevelNodes.append(element.left)
                
            if element.right is not None:
                nextLevelNodes.append(element.right)
                
        if nextLevelNodes is None or len(nextLevelNodes) == 0:
            return
        
        self.findRightMost(nextLevelNodes, rightmost)
        
    
    
if __name__ == "__main__":
    sol = Solution()
    node5 = TreeNode(5, None, None)
    node2 = TreeNode(2, None, node5)
    node4 = TreeNode(4, None, None)
    node3 = TreeNode(3, None, node4)
    node1 = TreeNode(1, node2, node3)
    print(sol.rightSideView(node1))
    
    node23 = TreeNode(3, None, None)
    node21 = TreeNode(1, None, node23)
    print(sol.rightSideView(node21))
    