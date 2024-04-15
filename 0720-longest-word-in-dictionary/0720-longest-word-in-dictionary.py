class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words = sorted(words, key = lambda s: len(s))
        
        res = {}
        
        compare = ['']
        
        max_len = 0
        
        for word in words:
            # if len(word) == 1 or not compare:
            #     compare.append(word)
            # else:
            if word[:-1] in compare:
                if len(word) >= max_len:
                    max_len = len(word)
                    res[word] = len(word)
                compare.append(word)
        
        if not res:
            return ''
        res = list(filter(lambda x: x[1] == max_len, res.items()))
        
        if len(res) == 1:
            return res[0][0]
        
        return sorted(res)[0][0]
        