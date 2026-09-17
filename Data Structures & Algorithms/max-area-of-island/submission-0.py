class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # dfs
        # count number of neighbors? 

        directions = [(1,0), (0,1), (-1,0), (0, -1)]

        def dfs(row, col, area):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return area
            
            if grid[row][col] == 0:
                return area
            
            grid[row][col] = 0 
            area = 1

            for dr, dc in directions:
                area += dfs(row+dr, col+dc, 0)

            return area
            
        max_area = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    a = dfs(i,j,0)
                    max_area = max(a,max_area)

        return max_area