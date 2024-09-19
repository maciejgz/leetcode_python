from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1  
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1  
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return results
    
    
    def getKey(self, nums: List[int]):
        nums.sort()
        result = '' + str(nums[0]) + str(nums[1]) + str(nums[2])
        return result
    
    
    
    
if __name__ == "__main__":
    solution = Solution()
    
    nums = [-1,0,1,2,-1,-4]
    
    print(solution.threeSum(nums))