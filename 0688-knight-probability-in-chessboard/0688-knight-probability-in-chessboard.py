class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        memo = {}
        def validate(x, y):
            
            if 0 <= x < n and 0 <= y < n:
                return True
            return False
        
        def solve(i, j, k):
            
            if k == 0:
                return 1
            
            if (i, j, k) in memo:
                return memo[(i, j, k)]
            suc = 0
            
            for dx, dy in moves:
                if validate(i+dx, j+dy):
                    suc = suc + solve(i+dx, j+dy, k-1)
            memo[(i, j, k)] = suc
            
            return suc
        
        return solve(row, column, k) / (8 ** k)
            