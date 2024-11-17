from typing import Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elements = []

        if root is None:
            return 0

        self.traverse(root, elements)
        elements.sort()
        
        if(k > len(elements)):
            return 0
        
        return elements[k-1]
        

    def traverse(self, root: TreeNode, elements):
        if root is not None:
            elements.append(root.val)

        if root.left is not None:
            self.traverse(root.left, elements)

        if root.right is not None:
            self.traverse(root.right, elements)


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        self.assertEqual(self.solution.kthSmallest(root, 1), 1)

    def test_case_2(self):
        root = TreeNode(
            5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)
        )
        self.assertEqual(self.solution.kthSmallest(root, 3), 3)

    def test_case_3(self):
        root = TreeNode(
            5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)
        )
        self.assertEqual(self.solution.kthSmallest(root, 4), 4)



if __name__ == "__main__":
    unittest.main()
