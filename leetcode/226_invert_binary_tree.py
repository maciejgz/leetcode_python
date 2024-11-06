# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.invertInside(root)
        return root
        
        
    def invertInside(self, node):
        if node is None:
            return
        
        temp_right = node.right;
        node.right = node.left
        node.left = temp_right
        
        self.invertInside(node.left)
        self.invertInside(node.right)
    
if __name__ == "__main__":
    obj = Solution()
