from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board is None or str is None:
            return False
        
        rows, cols = len(board), len(board[0])
        
        ## iteracja po wszystkich elementach tablicy
        for y in range(rows):
            for x in range(len(board[y])):
                print("sprawdzenie od litery:", y, x, " wartość: ", board[y][x], end='\n')
                visited = [[False for _ in range(cols)] for _ in range(rows)]
                if self.dfs(board, word, y, x, 0, visited):
                    return True
                
        return False
    
    def dfs(self, board, word, r, c, wordLetterIndex, visited):
        if wordLetterIndex == len(word):
            return True
        
        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != word[wordLetterIndex] or visited[r][c]:
            return False
        
        visited[r][c] = True
        found = (self.dfs(board, word, r + 1, c, wordLetterIndex + 1, visited) or
                 self.dfs(board, word, r - 1, c, wordLetterIndex + 1, visited) or
                 self.dfs(board, word, r, c + 1, wordLetterIndex + 1, visited) or
                 self.dfs(board, word, r, c - 1, wordLetterIndex + 1, visited))
        visited[r][c] = False
        return found
        
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))  # True
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))  # True
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))  # False