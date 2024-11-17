import unittest

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        operand = 0
        sign = 1

        for char in s:
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char == "+":
                result += sign * operand
                operand = 0
                sign = 1
            elif char == "-":
                result += sign * operand
                operand = 0
                sign = -1
            elif char == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ")":
                result += sign * operand
                operand = 0
                result *= stack.pop()
                result += stack.pop()

        return result + sign * operand
    
    
    
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        
    def test_case_1(self):
        self.assertEqual(self.solution.calculate("1 + 1"), 2)
        
    def test_case_2(self):
        self.assertEqual(self.solution.calculate(" 2-1 + 2 "), 3)
        
    def test_case_3(self):
        self.assertEqual(self.solution.calculate("(1+(4+5+2)-3)+(6+8)"), 23)
        
    def test_case_4(self):
        self.assertEqual(self.solution.calculate("1"), 1)


if __name__ == "__main__":
    unittest.main()