class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        mapping = {}
        
        m = len(grid)
        n = len(grid[0])
        
        queue = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    mapping[(i, j)] = 1
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = 0
        
        if not queue and  not mapping:
            return 0
        elif not queue:
            return -1
        
                    
        while queue:
            res += 1
            que_len = len(queue)
            for _ in range(que_len):
                x, y = queue.pop(0)
                for dx, dy in moves:
                    # print(x, y, dx, dy)
                    if x + dx >= 0 and x + dx <= m and y + dy >= 0 and y + dy <= n and (x + dx, y + dy) in mapping:
                        queue.append((x + dx, y + dy))
                        # print('in', (x + dx, y + dy), queue)
                        del mapping[(x + dx, y + dy)]
                        
            
            
        return res - 1 if len(mapping) == 0 else -1
                
                    
                    
                    
                    
                    
                
                
                
                
                
                
                
                
                
                    
                
                
        