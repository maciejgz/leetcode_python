from typing import List, Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
            
        # Create root from first preorder element
        root = TreeNode(preorder[0])
        
        # Find position of root in inorder
        mid = inorder.index(preorder[0])
        
        # Build left subtree
        # For left subtree, we need:
        # - preorder: elements after root up to size of left inorder subtree
        # - inorder: elements before root index
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Build right subtree
        # For right subtree, we need:
        # - preorder: remaining elements 
        # - inorder: elements after root index
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()



if __name__ == "__main__":
    unittest.main()
