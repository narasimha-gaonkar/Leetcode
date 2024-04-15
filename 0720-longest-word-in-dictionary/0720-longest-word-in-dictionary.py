class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort(key=lambda s: len(s))
        
        res = {}
        
        compare = set()
        compare.add('')
        
        max_len = 0
        
        for word in words:
            if word[:-1] in compare:
                if len(word) >= max_len:
                    max_len = len(word)
                    res[word] = len(word)
                compare.add(word)
        
        if not res:
            return ''
        res = list(filter(lambda x: x[1] == max_len, res.items()))
        
        if len(res) == 1:
            return res[0][0]
        
        return sorted(res)[0][0]
        