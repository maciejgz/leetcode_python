from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s is None or len(s) == 0 or p is None or len(p) == 0:
            return []

        if len(p) > len(s):
            return []

        anagram_length = len(p)
        result = []

        anagram_array = sorted(list(p))

        for i in range(len(s) - len(p) + 1):
            end_index = i + len(p)
            if self.is_anagram(s[i:end_index], anagram_array):
                result.append(i)

        return result

    def is_anagram(self, s: str, anagram_array: List[str]) -> bool:
        return sorted(list(s)) == anagram_array


if __name__ == "__main__":
    solution = Solution()
    print(solution.findAnagrams("cbaebabacd", "abc"))
