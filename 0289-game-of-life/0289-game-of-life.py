class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = {}
        
        m = len(board)
        n = len(board[0])
        
        def getGridValues(x, y):
            if x < m and y < n and x >= 0 and y >= 0:
                if (x, y) in visited:
                    return visited[(x, y)]
                return board[x][y]
            return 0
        
        
        for i in range(m):
            for j in range(n):
                visited[(i, j)] = board[i][j]
                summ = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        summ += getGridValues(i+k, j+l)
                
                summ -= board[i][j]
                if board[i][j] == 0 and summ == 3:
                    board[i][j] = 1
                elif board[i][j] == 1 and (summ == 2 or summ == 3):
                    board[i][j] = 1
                else:
                    board[i][j] = 0
        return board
        