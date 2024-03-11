class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        hmap = {}
        for char in s:
            hmap[char] = hmap.get(char, 0) + 1
        res = ''
        for seq in order:
            if seq in hmap:
                res = res + seq * hmap[seq]
                
                del hmap[seq]
        # print(res)
        for char in hmap:
            res = res + char * hmap[char]
        # print(hmap)
        # print(res)
        
        return res
            
        