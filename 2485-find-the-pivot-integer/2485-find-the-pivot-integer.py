import cmath
class Solution:
    def pivotInteger(self, n: int) -> int:
        
        root = math.sqrt((n * ( n + 1)) / 2)
        if not root.is_integer(): return -1
        
        for i in range(n, -1, -1):
            if i == root:
                return i