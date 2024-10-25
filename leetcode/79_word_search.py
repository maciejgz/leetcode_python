from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))  # True
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))  # True
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))  # False