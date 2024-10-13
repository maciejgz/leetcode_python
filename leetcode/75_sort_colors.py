from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, 0
        for element in nums:
            if element == 0:
                red += 1
            elif element == 1:
                white += 1
            elif element == 2:
                blue += 1

        for i in range(0, red):
            nums[i] = 0

        for i in range(0, white):
            nums[i + red] = 1

        for i in range(0, blue):
            nums[i + red + white] = 2

        print(nums)


if __name__ == "__main__":
    sol = Solution()
    sol.sortColors([2, 0, 2, 1, 1, 0])
