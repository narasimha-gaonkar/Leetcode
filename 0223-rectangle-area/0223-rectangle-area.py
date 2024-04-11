class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
            x1 = max(ax1, bx1)
            
            y1 = max(ay1, by1)
            
            x2= min(ax2, bx2)
            
            y2 = min(ay2, by2)
            
            # print(x1, y1, x2, y2)
            
            area_a = max(0, ax2-ax1) * max(0, ay2-ay1)
            
            area_b = max(0, bx2-bx1) * max(0, by2-by1)
            
            intersection = max(0, x2-x1) * max(0, y2-y1)
            
            return  area_a + area_b - intersection