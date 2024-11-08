from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: TreeNode, lower: float, upper: float) -> bool:
            if not node:
                return True
            if not (lower < node.val < upper):
                return False
            return validate(node.left, lower, node.val) and validate(node.right, node.val, upper)

        return validate(root, float('-inf'), float('inf'))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_bst(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertTrue(self.solution.isValidBST(root))

    def test_invalid_bst(self):
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertFalse(self.solution.isValidBST(root))

    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(self.solution.isValidBST(root))

    def test_empty_tree(self):
        root = None
        self.assertTrue(self.solution.isValidBST(root))

    def test_invalid_bst_with_equal_values(self):
        root = TreeNode(1, TreeNode(1))
        self.assertFalse(self.solution.isValidBST(root))

    def test_invalid_bst_with_specific_values(self):
        root = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
        self.assertFalse(self.solution.isValidBST(root))


if __name__ == "__main__":
    unittest.main()
