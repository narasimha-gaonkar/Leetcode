class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        visited = [False] * n
        
        dp = {}
        
        for x, y in edges:
            if x in dp:
                dp[x].append(y)
            else:
                dp[x] = [y]
                
            if y in dp:
                dp[y].append(x)
            else:
                dp[y] = [x]
        
        if source not in dp or destination not in dp:
            return False
        
        def solve(i):

            visited[i] = True
            
            for transition in dp[i]:
                if not visited[transition]:
                    # print(i, '=>',transition)
                    solve(transition)
            return visited[i]
        solve(source)
        # print(visited)
        return visited[destination]
            
            
            