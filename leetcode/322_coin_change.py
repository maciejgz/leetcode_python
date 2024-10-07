import sys
from typing import List


class Solution:
    def coinChangeGreedy(self, coins: List[int], amount: int) -> int:
        if coins is None or len(coins) == 0 or amount < 0:
            return -1
        if amount == 0:
            return 0

        coins = sorted(coins, reverse=True)
        coins_number = 0
        rest = amount
        for coin in coins:
            print("coin", coin)
            coins_number += rest // coin
            print("coins_number", coins_number)
            rest = rest % coin
            print("rest", rest)
            if rest == 0:
                break

        if rest == 0:
            return coins_number
        else:
            return -1

    def coinChange(self, coins: List[int], amount: int) -> int:

        if coins is None or len(coins) == 0 or amount < 0:
            return -1
        if amount == 0:
            return 0

        m = len(coins)

        return self.minCoins(coins, m, amount)

    def minCoins(self, coins, m, sum):

        # table[i] will be storing the minimum
        # number of coins required for i value.
        # So table[sum] will have result
        table = [0 for i in range(sum + 1)]

        # Base case (If given value sum is 0)
        table[0] = 0

        # Initialize all table values as Infinite
        for i in range(1, sum + 1):
            table[i] = sys.maxsize

        # Compute minimum coins required
        # for all values from 1 to sum
        for i in range(1, sum + 1):

            # Go through all coins smaller than i
            for j in range(m):
                if coins[j] <= i:
                    sub_res = table[i - coins[j]]
                    if sub_res != sys.maxsize and sub_res + 1 < table[i]:
                        table[i] = sub_res + 1

        if table[sum] == sys.maxsize:
            return -1

        return table[sum]


if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))

    print(solution.coinChange([1], 0))
    print(solution.coinChange([186, 419, 83, 408], 6249))
