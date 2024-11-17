from typing import List
import unittest


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        word_len = len(beginWord)
        queue = [(beginWord, 1)]
        while queue:
            word, level = queue.pop(0)
            if word == endWord:
                return level
            for i in range(word_len):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + c + word[i + 1 :]
                    if new_word in word_set:
                        word_set.remove(new_word)
                        queue.append((new_word, level + 1))
        return 0


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()
        
    def test_case_1(self):
        self.assertEqual(
            self.solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]),
            5,
        )
        
    def test_case_2(self):
        self.assertEqual(
            self.solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]),
            0,
        )
        
    def test_case_3(self):
        self.assertEqual(
            self.solution.ladderLength("a", "c", ["a", "b", "c"]),
            2,
        )

if __name__ == "__main__":
    unittest.main()
