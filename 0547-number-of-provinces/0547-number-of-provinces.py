class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        
        visited = [False] * n
        
        def solve(node):
            visited[node] = True
            for j in range(n):
                if isConnected[node][j] == 1 and not visited[j]:
                    solve(j)
        
        province = 0
        for i in range(n):
            if not visited[i]:
                province += 1
                solve(i)
        
        return province
            
                
            
            
        