class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        
        res = []
        m = len(land)
        n = len(land[0])
        steps = [(0, 1), (1, 0)]
        
        dp = [ [False] * n for _ in range(m)]
        
        def val(i, j):
            if 0 <= i < m and 0 <= j < n and land[i][j] == 1 and dp[i][j] == False:
                return True
            return False
        
        def solve(i, j, max_i, max_j):
            
            dp[i][j] = True
            
            max_i = max(max_i, i)
            max_j = max(max_j, j)
            
            for dx, dy in steps:
                if val(i + dx, j + dy):
                    max_i, max_j =  solve(i + dx, j + dy, max_i, max_j)
                    
            return [max_i, max_j]
                    
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1 and dp[i][j] == False:
                    tmp = [i, j]
                    tmp.extend(solve(i, j, i, j))
                    res.append(tmp)
        return res
            
            
            