from typing import List
import unittest


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        while stack:
            h = heights[stack.pop()]
            w = len(heights) if not stack else len(heights) - stack[-1] - 1
            max_area = max(max_area, h * w)
        return max_area
    

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        
    def test_case_1(self):
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 5, 6, 2, 3]), 10)
        
    def test_case_2(self):
        self.assertEqual(self.solution.largestRectangleArea([2, 4]), 4)
        
    def test_case_3(self):
        self.assertEqual(self.solution.largestRectangleArea([2, 1, 2]), 3)


if __name__ == "__main__":
    unittest.main()
