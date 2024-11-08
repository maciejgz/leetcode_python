
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution(object):
    
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0;
        
        max_depth = self.getInside(root)
        
        return max_depth
    
    def getInside(self, node) -> int:
        if node is None:
            return 0
        
        left_depth = self.getInside(node.left)
        right_depth = self.getInside(node.right)
        
        return 1 + max(left_depth, right_depth)
        
        
if __name__ == '__main__':
    s = Solution()
    node2 = TreeNode(2, None, None)
    node1 = TreeNode(1, None, node2)
    print(s.maxDepth(node1))