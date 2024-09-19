class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i + 1)
            len_max = max(len1, len2)
            if len_max > end - start:
                start = i - (len_max - 1) // 2
                end = i + len_max // 2
        return s[start : end + 1]
    
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("aaaa"))
