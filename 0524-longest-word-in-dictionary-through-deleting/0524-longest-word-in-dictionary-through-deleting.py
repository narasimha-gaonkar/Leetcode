class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        max_length_str = ''
        n = len(s)
        dictionary = set(dictionary)
        
        for word_c in dictionary:
            i = 0
            k = len(word_c)
            for letter in word_c:
                while i < n:
                    if letter == s[i]:
                        k -= 1
                        i += 1
                        break
                    i += 1
            if k == 0 and len(word_c) > len(max_length_str):
                    max_length_str = word_c
            elif k == 0 and len(word_c) == len(max_length_str):
                max_length_str = min(word_c, max_length_str)
                
        return max_length_str
            
    