class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
            
            steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            m = len(grid)
            n = len(grid[0])
            max_gold = 0
            visited = [[False] * n for _ in range(m)]
            
            def val(i,j):
                if i < 0 or j < 0 or i >= m or j >= n or visited[i][j]:
                    return False
                return grid[i][j]!=0
            
            def solve(i, j):
                tmp_max = 0
                
                visited[i][j] = True
                
                for x, y in steps:
                    
                    new_x = i + x
                    new_y = j + y
                    
                    if val(new_x, new_y):
                        tmp_max = max(tmp_max, grid[new_x][new_y] + solve(new_x, new_y))
                
                visited[i][j] = False
                
                return tmp_max
            
            for i in range(m):
                for j in range(n):
                    if grid[i][j] !=0 and not visited[i][j]:
                        max_gold = max(max_gold, grid[i][j]  + solve(i, j))
            return max_gold
                    