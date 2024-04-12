class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        
        right_max = [0] * n
        
        l_max = 0
        r_max = 0
        
        res = 0
        for i in range(n):
            l_max = max(l_max, height[i])
            
            r_max = max(r_max, height[n - i - 1])
            
            left_max[i] = l_max
            right_max[n - i - 1] = r_max
        print(left_max, right_max)
        for i in range(n):
            res += abs(height[i] - min(left_max[i], right_max[i]))
        
        return res
            
            
            
        