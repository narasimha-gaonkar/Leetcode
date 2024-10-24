class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort()
        s.sort()
        
        count = 0
        
        idx = 0
        i = 0
        while idx < len(s) and i < len(g):
            if s[idx] >= g[i]:
                count += 1
                i+=1
                idx += 1
            else:
                idx+= 1
        return count
            