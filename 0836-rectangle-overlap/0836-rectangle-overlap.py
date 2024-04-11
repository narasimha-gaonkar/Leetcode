class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        x1, y1, x2, y2 = rec1
        _x1, _y1, _x2, _y2 = rec2
        
        if x2 <= _x1 or _x2 <= x1  or y2 <= _y1 or _y2 <= y1:
            return False
        return True
    
        
        