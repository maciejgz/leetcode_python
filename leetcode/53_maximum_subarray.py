from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if nums is None:
            return None
        
        if len(nums) == 0:
            return nums[0]
        
        top_sum = float('-inf')
        current_sum = 0
        for x in nums:
            current_sum = max(x, current_sum + x)
            top_sum = max(top_sum, current_sum)
                
        return top_sum
            
            
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]));
        