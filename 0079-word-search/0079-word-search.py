class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = {}
        m = len(board)
        n = len(board[0])
        
        def solve(i, j, k):
            if k == len(word):
                return True
            
            if i >= m or i < 0 or j >= n or j < 0 or board[i][j] != word[k] or visited.get((i, j)):
                return False
            visited[(i, j)] = True
            
            res = solve(i, j + 1, k + 1) or solve(i, j - 1, k + 1) or solve(i + 1, j, k + 1) or solve(i - 1, j, k + 1)
            
            del visited[(i, j)]
            
            return res
                
            
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and solve(i, j, 0):
                    return True
        return False
        