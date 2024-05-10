class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        n_len = len(stones)
        target = stones[-1]
        
        @cache
        def solve(pos, k):
            if k <= 0:
                return False
            #Fell in water
            if pos not in stones:
                return False
            #reached target
            if pos == target:
                return True
            
            return solve(pos + k + 1, k + 1) or solve(pos + k, k) or solve(pos + k - 1, k - 1)
        
        return solve(1, 1)