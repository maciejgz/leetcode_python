from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        result = 0

        some_oranges_rotten_this_minute = True
        
        new_grid = [row[:] for row in grid]

        while some_oranges_rotten_this_minute:
            some_oranges_rotten_this_minute = False
            
            new_grid = [row[:] for row in grid]
            
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    if grid[i][j] == 1 and self.has_rotten_neighbours(i, j, grid):
                        new_grid[i][j] = 2
                        some_oranges_rotten_this_minute = True
                        
                        
            grid = new_grid 

            if some_oranges_rotten_this_minute:
                result += 1
                
                
                
        ## check if non rotten oranges left
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    result = -1
                        

        return result
    
    def has_rotten_neighbours(self, row: int, col: int, grid: List[List[int]]) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 2:
                return True
        return False
        


if __name__ == "__main__":
    solution = Solution()
    print(solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
