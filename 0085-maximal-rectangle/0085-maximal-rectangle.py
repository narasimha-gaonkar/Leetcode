class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        def largestRect(heights):
            stack = []
            maxArea = 0
            n = len(heights)

            for i in range(n):
                while stack and heights[i] < heights[stack[-1]]:
                    topHeight = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, topHeight * width)

                stack.append(i)

            while stack:
                topHeight = heights[stack.pop()]
                width = n if not stack else n - stack[-1] - 1
                maxArea = max(maxArea, topHeight * width)

            return maxArea
        
        m = len(matrix)
        n = len(matrix[0])
        
        maxArea = 0
        
        heights = [0] * n
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += int(matrix[i][j])
                else:
                    heights[j] = 0
            maxArea = max(maxArea, largestRect(heights))
       
        return maxArea
        
        
                    
            