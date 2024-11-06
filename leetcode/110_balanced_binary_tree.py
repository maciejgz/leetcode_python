# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        return self.checkHeight(root) != -1
    
    def checkHeight(self, node):
        if node is None:
            return 0
        
        left_height = self.checkHeight(node.left)
        if left_height == -1:
            return -1
        
        right_height = self.checkHeight(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
        
if __name__ == "__main__":
    obj = Solution()
