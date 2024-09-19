import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1

        if len(nums) == 1 and nums[0] == target:
            return 0

        startIndex = 0
        endIndex = len(nums) - 1
        
        while startIndex <= endIndex:
            middle = (endIndex + startIndex) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                startIndex = middle + 1
            else:
                endIndex = middle - 1

        return -1


if __name__ == "__main__":
    solution = Solution()
    # print(solution.search([1, 2], 2))
    print(solution.search([-1, 0, 3, 5, 9, 12], 3))
    
    
    print(solution.search(
        [2,5], 5
        
    ))
