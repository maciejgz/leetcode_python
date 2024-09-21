
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sorted(nums)
        if nums is None:
            return None
        
        result = []
        self.heap_permutations(nums, len(nums), result)
        
        return result
        
        
    def heap_permutations(self, sublist: List[int], size: int, result: List[int]):
        
        if size == 1:
            print(sublist)
            result.append(sublist.copy())
            return
    
        for i in range(size):
            self.heap_permutations(sublist, size-1, result)
    
            if size & 1:
                sublist[0], sublist[size-1] = sublist[size-1], sublist[0]
            else:
                sublist[i], sublist[size-1] = sublist[size-1], sublist[i]
        
         

if __name__ == "__main__":
    sol = Solution()
    print(sol.permute([1,2,3])) 