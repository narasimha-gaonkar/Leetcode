class Solution:
    def firstUniqChar(self, s: str) -> int:
        dmap = {}
        non_considerable = set()
        
        for index, letter in enumerate(s):
            if letter in non_considerable:
                continue
            elif letter in dmap:
                non_considerable.add(letter)
                del dmap[letter]
            else:
                dmap[letter] = index
        
        # uniquechars = filter(lambda x: x[0] == 1, dmap.values())
        if len(dmap) == 0:
            return -1
        
        return min(dmap.values())


