class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
            
            steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            visited = set()
            def val(i,j):
                if i < 0 or j < 0 or i >= m or j >= n or (i, j) in visited:
                    return False
                return grid[i][j]!=0
            
            def solve(i, j):
                tmp_max = 0
                
                visited.add((i, j))
                
                for x, y in steps:
                    
                    new_x = i + x
                    new_y = j + y
                    
                    if val(new_x, new_y):
                        tmp_max = max(tmp_max, grid[new_x][new_y] + solve(new_x, new_y))
                visited.remove((i, j))
                return tmp_max

            
            m = len(grid)
            n = len(grid[0])
            max_gold = 0
            
            for i in range(m):
                for j in range(n):
                    
                    if grid[i][j] !=0 :
                        visited = set()
                        max_gold = max(max_gold, grid[i][j]  + solve(i, j))
            return max_gold
                    