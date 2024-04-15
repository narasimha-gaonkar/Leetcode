class Solution:
    def longestWord(self, words: List[str]) -> str:
        
        words.sort(key=lambda s: len(s))
        
        compare = set()
        compare.add('')
        
        max_len_word = ''
        
        max_len = 0
        
        for word in words:
            if word[:-1] in compare:
                if len(word) > max_len:
                    max_len_word = word
                    max_len = len(word)
                elif len(word) == max_len and word < max_len_word:
                    max_len_word = word
                    max_len = len(word)
                    
                compare.add(word)
        return max_len_word
        