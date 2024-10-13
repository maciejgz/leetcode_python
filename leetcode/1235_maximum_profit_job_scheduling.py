from typing import List


class Solution:
    def jobScheduling(self, start_times: List[int], end_times: List[int], profits: List[int]) -> int:
        # Combine the job information into a single list and sort by end time.
        jobs = sorted(zip(end_times, start_times, profits))
      
        # Get the total number of jobs.
        number_of_jobs = len(profits)
      
        # Initialize dynamic programming table with 0 profits.
        dp = [0] * (number_of_jobs + 1)
      
        # Iterate over the jobs.
        for i, (current_end_time, current_start_time, current_profit) in enumerate(jobs):
            # Find the rightmost job that doesn't conflict with the current job's start time.
            # Use binary search for efficient querying. 'hi' is set to the current index 'i' for optimization.
            index = self.bisect_right(jobs, current_start_time, hi=i, key=lambda x: x[0])
          
            # Update the DP table by choosing the maximum of either taking the current job or not.
            # If taking the current job, add its profit to the total profit of non-conflicting jobs.
            dp[i + 1] = max(dp[i], dp[index] + current_profit)
      
        # Return the maximum profit which is the last element in the DP table.
        return dp[number_of_jobs]
    
    def bisect_right(self, arr, target, lo=0, hi=None, key=lambda x: x):
        if hi is None:
            hi = len(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if key(arr[mid]) <= target:
                lo = mid + 1
            else:
                hi = mid
        return lo
    


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60])
    )
