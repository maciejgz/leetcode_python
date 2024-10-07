
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a is None or len(a) == 0:
            return b
        if b is None or len(b) == 0:
            return a

        a_index = len(a) - 1
        b_index = len(b) - 1
        carry = 0
        result = ""
        while a_index >= 0 or b_index >= 0:
            a_val = int(a[a_index]) if a_index >= 0 else 0
            b_val = int(b[b_index]) if b_index >= 0 else 0
            sum = a_val + b_val + carry
            carry = sum // 2
            result = str(sum % 2) + result
            a_index -= 1
            b_index -= 1
        if carry > 0:
            result = str(carry) + result
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("11", "1"))
    print(solution.addBinary("1010", "1011"))