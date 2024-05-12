class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        @cache
        def solve(i, j):
            
            if i == 0 and j == 0:
                return grid[i][j]
            
            if i > 0:
                up = grid[i][j] + solve(i-1, j)
            else:
                up = float(inf)
            
            if j > 0:
                left = grid[i][j] + solve(i, j-1)
            else:
                left = float(inf)
            
            return min(up, left)
        
        return solve(m-1, n-1)
        