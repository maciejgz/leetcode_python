from collections import deque
import math
from typing import List


class Solution:

    def __init__(self):
        self.stack = deque()

    def evalRPN(self, tokens: List[str]) -> int:
        for i in range(len(tokens)):
            if self.is_number(tokens[i]):
                self.stack.append(tokens[i])
            elif tokens[i] == "+":
                value1 = int(self.stack.pop())
                value2 = int(self.stack.pop())
                self.stack.append(value1 + value2)
            elif tokens[i] == "-":
                value1 = int(self.stack.pop())
                value2 = int(self.stack.pop())
                self.stack.append(value2 - value1)
            elif tokens[i] == "*":
                value1 = int(self.stack.pop())
                value2 = int(self.stack.pop())
                self.stack.append(value2 * value1)
            elif tokens[i] == "/":
                value1 = int(self.stack.pop())
                value2 = int(self.stack.pop())
                res = value2 / value1
                if res < 0:
                    self.stack.append(math.ceil(res))
                else:
                    self.stack.append(math.floor(res))

        return int(self.stack.pop())

    def is_number(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    solution = Solution()
    # print(solution.evalRPN(["2","1","+","3","*"]))
    print(
        solution.evalRPN(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
    )
