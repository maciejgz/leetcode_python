from typing import List
import unittest

class Solution:
    def jobScheduling(self, start_times: List[int], end_times: List[int], profits: List[int]) -> int:
        # Combine the job information into a single list and sort by end time.
        jobs = sorted(zip(end_times, start_times, profits))
        number_of_jobs = len(profits)
        dp = [0] * (number_of_jobs + 1)
      
        for i, (current_end_time, current_start_time, current_profit) in enumerate(jobs):
            # Find the rightmost job that doesn't conflict with the current job's start time.
            index = self.bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])
            # Update the DP table by choosing the maximum of either taking the current job or not.
            dp[i + 1] = max(dp[i], dp[index] + current_profit)
      
        return dp[number_of_jobs]
    
    def bisect_right(self, arr, target, lo=0, hi=None, key=lambda x: x):
        """Helper function to perform binary search."""
        if hi is None:
            hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if key(arr[mid]) <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]), 150)

    def test_case_2(self):
        self.assertEqual(self.solution.jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]), 120)

    def test_case_3(self):
        self.assertEqual(self.solution.jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]), 6)

    def test_case_4(self):
        self.assertEqual(self.solution.jobScheduling([4, 2, 4, 8, 2], [5, 5, 5, 10, 8], [1, 2, 8, 10, 4]), 18)

if __name__ == "__main__":
    unittest.main()
