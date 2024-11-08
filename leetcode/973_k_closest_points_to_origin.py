import math
from typing import List
import unittest


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        for point in points:
            point.append(self.calculate_distance(point[0], point[1]))
            
        points.sort(key=lambda x: x[2])
        return [[point[0], point[1]] for point in points[:k]]
        
    def calculate_distance(self, x: int, y: int) -> float:
        return math.sqrt((x * x) + (y * y))

class TestMyQueue(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_kClosest(self):
        self.assertEqual(self.solution.kClosest([[1, 3], [-2, 2]], 1), [[-2, 2]])
        self.assertEqual(self.solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2), [[3, 3], [-2, 4]])
        self.assertEqual(self.solution.kClosest([[1, 2], [2, 3], [3, 4]], 3), [[1, 2], [2, 3], [3, 4]])

if __name__ == "__main__":
    unittest.main()