class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        l_maxx = 0
        r_maxx = 0
        res = 0
        
        for i in range(n):
            l_maxx = max(l_maxx, height[i])
            left_max[i] = l_maxx
            
            r_maxx = max(r_maxx, height[n - i - 1])
            right_max[n - i - 1] = r_maxx
        for i in range(n):
            res += abs(height[i] - min(left_max[i], right_max[i]))
        
        return res
            
            
        