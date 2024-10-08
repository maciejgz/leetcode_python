class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
        
        
if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(2))
    print(solution.climbStairs(3))
  
    