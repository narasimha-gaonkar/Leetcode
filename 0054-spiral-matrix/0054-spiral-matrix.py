class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        m = len(matrix)
        n = len(matrix[0])
        
        visited = [[False] * n for _ in range(m)]
        x, y = 0, 0
        k = 0
        res = []
        count = 0

        while count < m * n:
            count += 1
            
            visited[x][y] = True
            res.append(matrix[x][y])
            
            dx, dy = steps[k]
            
            nx = x + dx
            ny = y + dy
            
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                x, y = nx, ny
            else:
                k = (k + 1) % 4
                
                dx, dy = steps[k]
                x = x + dx
                y = y + dy
        return res
            
            
            
            
            
            