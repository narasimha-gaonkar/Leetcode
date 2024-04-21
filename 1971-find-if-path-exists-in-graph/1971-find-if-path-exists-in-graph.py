class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True
        
        visited = [False] * n
        
        dp = defaultdict(list)
        
        for x, y in edges:
            dp[x].append(y)
            dp[y].append(x)
        
        if source not in dp or destination not in dp:
            return False
        
        def solve(i):
            if i == destination:
                return True
            visited[i] = True
            for transition in dp[i]:
                if not visited[transition]:
                    if solve(transition):
                        return True
            return False
        return solve(source)
        
            
            
            