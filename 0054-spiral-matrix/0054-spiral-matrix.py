class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[False] * n for _ in range(m)]
        x, y = 0, 0
        k = 0
        res = []
        count = 0
        
        def val(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or dp[i][j]:
                return False
            return True
        
        while True:
            count += 1
            # print(count, x, y)
            
            dp[x][y] = True
            res.append(matrix[x][y])
            if count == m * n:
                return res
            
            dx, dy = steps[k]
            
            if val(x+dx, y+dy):
                x = x + dx
                y = y + dy
            else:
                k += 1
                if k == 4:
                    k = 0
                dx, dy = steps[k]
                x = x + dx
                y = y + dy
            
            
            
            
            
            