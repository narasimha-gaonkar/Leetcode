class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def no_edges(i, j):
            count = 0
            for dx, dy in steps:
                if 0 <= i + dx < m and 0 <= j + dy < n and grid[i+dx][j+dy] == 1:
                    continue
                count+=1
            return count
        res = 0   
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res += no_edges(i, j)
        return res