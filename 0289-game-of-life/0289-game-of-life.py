class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                
                res = 0
                
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        
                        if not (dx == 0 and dy == 0) and  0 <= i + dx < m and 0 <= j + dy < n:
                            if board[i+dx][j+dy] == 1 or board[i+dx][j+dy] == '#':
                                res += 1
                
                if board[i][j] == 1 and res < 2:
                    board[i][j] = '#'
                elif board[i][j] == 1 and res > 3:
                    board[i][j] = '#'
                elif board[i][j] == 0 and res == 3:
                    board[i][j] = '*'
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 0
                elif board[i][j] == '*':
                    board[i][j] = 1
        
        return board
                
        