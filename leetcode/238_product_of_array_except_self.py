from typing import List
import unittest


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums is None:
            return None

        total = 1
        total_without_zeroes = 1
        zeroes = 0
        for el in nums:
            total = total * el
            if el != 0:
                total_without_zeroes = total_without_zeroes * el
            if el == 0:
                zeroes += 1
            

        result = []
        for el in nums:
            if zeroes > 1:
                result.append(0)
            else:
                if el != 0:
                    result.append((int)(total / el))
                else:
                    result.append(total_without_zeroes)

        return result


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])

    def test_case_2(self):
        self.assertEqual(
            self.solution.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0]
        )


if __name__ == "__main__":
    unittest.main()
