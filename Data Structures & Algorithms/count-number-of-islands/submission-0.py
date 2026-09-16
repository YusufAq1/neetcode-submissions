class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]


        def dfs(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return
            
            if grid[i][j] == '0':
                return
            
            grid[i][j] = '0'
            
            for dr, dc in directions:
                dfs(i + dr, j + dc)
        
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    islands += 1
                    dfs(row, col)
        
        return islands
        


            

            



            
