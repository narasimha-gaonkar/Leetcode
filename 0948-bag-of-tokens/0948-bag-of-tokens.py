class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        
        left = 0 
        right = len(tokens) - 1
        tokens.sort()
        score = 0
        max_score = 0
        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                left += 1
                score += 1
                max_score = max(max_score,score)
            elif score >= 1:
                power += tokens[right]
                right -= 1
                score -= 1
            else:
                break
        return max_score