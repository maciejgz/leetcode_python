from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        res = []
        backtrack(0, [])
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))  # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]