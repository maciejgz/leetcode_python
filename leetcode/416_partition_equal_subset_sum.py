from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        dp = [[-1] * (total_sum + 1) for i in range(len(nums) + 1)]

        return self.is_subset_sum(nums, len(nums), total_sum // 2, dp)

    def is_subset_sum(self, arr, n, sum, dp):

        # Base Cases
        if sum == 0:
            return True
        if n == 0 and sum != 0:
            return False

        # return solved subproblem
        if dp[n][sum] != -1:
            return dp[n][sum]

        # If last element is greater than sum, then
        # ignore it
        if arr[n - 1] > sum:
            return self.is_subset_sum(arr, n - 1, sum, dp)

            # else, check if sum can be obtained by any of
            # the following
            # (a) including the last element
            # (b) excluding the last element

        # also store the subproblem in dp matrix
        dp[n][sum] = self.is_subset_sum(arr, n - 1, sum, dp) or self.is_subset_sum(
            arr, n - 1, sum - arr[n - 1], dp
        )

        return dp[n][sum]


if __name__ == "__main__":
    solution = Solution()
    print(solution.canPartition([1, 5, 11, 5]))
