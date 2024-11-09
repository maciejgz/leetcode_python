from typing import List, Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result


class TestMyQueue(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_levelOrder(self):
        node1 = TreeNode(3)
        node2 = TreeNode(9)
        node3 = TreeNode(20)
        node4 = TreeNode(15)
        node5 = TreeNode(7)
        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5
        self.assertEqual(self.solution.levelOrder(node1), [[3], [9, 20], [15, 7]])
        
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node1.left = node2
        node1.right = node3
        node3.left = node4
        node3.right = node5
        self.assertEqual(self.solution.levelOrder(node1), [[1], [2, 3], [4, 5]])
        
        node1 = TreeNode(1)
        self.assertEqual(self.solution.levelOrder(node1), [[1]])
        
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node1.left = node2
        self.assertEqual(self.solution.levelOrder(node1), [[1], [2]])
        
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7
        self.assertEqual(self.solution.levelOrder(node1), [[1], [2, 3], [4, 5, 6, 7]])
        
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node8 = TreeNode(8)
        node9 = TreeNode(9)
        node10 = TreeNode(10)
        node11 = TreeNode(11)
        node12 = TreeNode(12)
        node13 = TreeNode(13)
        node1.left = node2
        node1.right = node3
        node2.left = node4
        node2.right = node5
        node3.left = node6
        node3.right = node7
        node4.left = node8
        node4.right = node9
        node5.left = node10
        node5.right = node11
        node6.left = node12
        node6.right = node13
        self.assertEqual(self.solution.levelOrder(node1), [
            [1], [2, 3], [4, 5, 6, 7], [8, 9, 10, 11, 12, 13]
        ])


if __name__ == "__main__":
    unittest.main()