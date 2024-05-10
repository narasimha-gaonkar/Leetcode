class Solution:
    def trap(self, height: List[int]) -> int:
        
        
        if len(height) < 2:
            return 0
        
        max_left, max_right = height[0], height[-1]
        
        l, r, = 1, len(height) - 2
        
        res = 0
        
        while l <= r:
            
            if max_left < max_right:
                
                if height[l] > max_left:
                    max_left = height[l]
                else:
                    res += abs(max_left - height[l])
                l += 1
            else:
                if height[r] > max_right:
                    max_right = height[r]
                else:
                    res += abs(max_right - height[r])
                r -= 1
        return res
                
            
            
        