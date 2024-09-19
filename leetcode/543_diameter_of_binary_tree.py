# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Height:
    def __init(self):
        self.h = 0


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        height = Height()
        result = diameterOpt(root, height)
        if result > 0:
            result = result - 1
            
        return result


def diameterOpt(root, height):

    lh = Height()
    rh = Height()

    if root is None:
        height.h = 0
        return 0

    ldiameter = diameterOpt(root.left, lh)
    rdiameter = diameterOpt(root.right, rh)

    height.h = max(lh.h, rh.h) + 1

    return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))


if __name__ == "__main__":
    solution = Solution()
    node4 = TreeNode(4, None, None)
    node5 = TreeNode(5, None, None)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3, None, None)
    node1 = TreeNode(1, node2, node3)
    print(solution.diameterOfBinaryTree(node1))
