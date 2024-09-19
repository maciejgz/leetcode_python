from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1;
        
        indexx = 0
        for element in nums:
            if target == element:
                return indexx
            indexx += 1;
            
        return -1;
                
                
                
            


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
