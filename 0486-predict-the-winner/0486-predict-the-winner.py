class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def best_score_diff(i,j):
            # invalid state
            if i > j:
                return 0
            # whoever reaches here gets this number
            if i == j:
                return nums[i]
            
            # choose best of both choices
            score_diff_i = nums[i] - best_score_diff(i+1,j) # chose i
            score_diff_j = nums[j] - best_score_diff(i,j-1) # chose j
            return max(score_diff_i,score_diff_j)
        
        return best_score_diff(0,len(nums)-1) >= 0
