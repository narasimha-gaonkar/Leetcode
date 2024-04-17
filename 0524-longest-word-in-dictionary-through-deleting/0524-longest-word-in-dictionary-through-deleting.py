class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        max_length_str = ''
        n = len(s)
        
        for word_c in dictionary:
            i = 0
            k = len(word_c)
            # print(k)
            for letter in word_c:
                while i < n:
                    # print(letter, s[i])
                    if letter == s[i]:
                        k -= 1
                        i += 1
                        break
                    i += 1
            # print(k)
            if k == 0 and len(word_c) > len(max_length_str):
                    max_length_str = word_c
            elif k == 0 and len(word_c) == len(max_length_str):
                max_length_str = min(word_c, max_length_str)
                
        return max_length_str
            
    