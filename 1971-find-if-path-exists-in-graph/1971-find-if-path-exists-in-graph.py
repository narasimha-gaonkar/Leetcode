class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        
        visited = [False] * n
        
        dp = defaultdict(set)
        
        for x, y in edges:
            dp[x].add(y)
            dp[y].add(x)
        
        if source not in dp or destination not in dp:
            return False
        
        def solve(i):

            visited[i] = True
            
            for transition in dp[i]:
                if not visited[transition]:
                    solve(transition)
            return visited[i]
        solve(source)
        return visited[destination]
            
            
            