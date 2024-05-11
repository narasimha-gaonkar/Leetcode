class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = defaultdict(list)
        
        
        for word in strs:
            word_freq = [0] * 26
            for let in word:
                word_freq[ord(let) - ord('a')] += 1
            freq[tuple(word_freq)].append(word)
            
        return freq.values()
        