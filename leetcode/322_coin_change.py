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
        ## TODO implement
        if coins is None or len(coins) == 0 or amount < 0:
            return -1
        if amount == 0:
            return 0
        

if __name__ == "__main__":
    solution = Solution()
    print(solution.coinChange([1, 2, 5], 11))
    print(solution.coinChange([1], 0))
    print(solution.coinChange([186, 419, 83, 408], 6249))
