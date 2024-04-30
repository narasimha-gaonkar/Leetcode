class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = defaultdict(int)
        count[0] = 1
        res, mask = 0, 0
        
        for c in word:
            index = (ord(c) - ord('a'))
            mask ^= 1 << index
            
            res += count[mask]
            
            for i in range(10):
                preMask = mask ^ (1 << i)
                res += count[preMask]
            
            count[mask] += 1
        return res