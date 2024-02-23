class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        m = len(nums2)
        
        dp = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[n][m]
        
#         def solve(i, j):
#             if i < 0 or j < 0:
#                 return 0
            
#             if dp[i][j] != -1:
#                 return dp[i][j]
            
#             count = 0
#             if nums1[i] == nums2[j]:
#                 count = 1 + solve(i-1, j-1)
            
#             else:
#                 count = max(solve(i-1, j), solve(i, j-1))
#             dp[i][j] = count
            
#             return count
        
#         return solve(n-1, m-1)
        