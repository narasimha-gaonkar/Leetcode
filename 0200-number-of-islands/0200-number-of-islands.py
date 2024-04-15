class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid)
        n = len(grid[0])
        dp = [[False] * n for _ in range(m)]
        
        steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def val(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or dp[i][j] or grid[i][j] == '0':
                return False
            return True
        
        def solve(i, j):
            # isIsland = False
            # print('line 17')
            dp[i][j] = True
            
            for dx, dy in steps:
                
                new_x = i + dx
                new_y = j + dy
                if val(new_x, new_y):
                    solve(new_x, new_y)
            
            return
        
        
        no_island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and dp[i][j] == False:
                    solve(i, j)
                    no_island += 1
        return no_island