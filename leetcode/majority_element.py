
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        
        for element in nums:
            if element in dict:
                dict[element] += 1;
            else:
                dict[element] = 1
                
        max_results = 0;
        result = 0;
        for vallue in dict:
            if dict[vallue] > max_results:
                max_results = dict[vallue]
                result = vallue;
                
        return result;


if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement([3,2,3]))