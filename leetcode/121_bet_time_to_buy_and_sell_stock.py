import math


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        min = float('inf')
        max_diff = 0

        for price in prices:
            if price < min:
                min = price
                
            max_diff = max(max_diff, (price - min))
            
        return max_diff


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))
    print(s.maxProfit([7, 6, 4, 3, 1]))
