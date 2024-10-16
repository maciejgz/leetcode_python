from collections import Counter, defaultdict


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_t = Counter(t)
        required = len(dict_t)

        left, right = 0, 0
        formed = 0
        window_counts = defaultdict(int)

        min_len = float("inf")
        min_left, min_right = 0, 0

        while right < len(s):
            char = s[right]
            window_counts[char] += 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while left <= right and formed == required:
                char = s[left]

                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left, min_right = left, right

                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                left += 1

            right += 1

        return s[min_left : min_right + 1] if min_len != float("inf") else ""


if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # "BANC"