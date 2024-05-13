class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        
        visited = [False] * n
        
        province = 0
        for i in range(n):
            if not visited[i]:
                province += 1
                
                queue = [i]
                
                while queue:
                    node = queue.pop(0)
                    
                    for j in range(n):
                        if isConnected[node][j] == 1 and not visited[j]:
                            queue.append(j)
                            visited[j] = True
        
        return province
            
                
            
            
        