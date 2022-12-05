class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = max(heights)
        heights.append(0)
        stack = [-1]
        
        for i, num in enumerate(heights):
            
            while heights[stack[-1]] > num:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max( height * width , res)
            
            stack.append(i)
        heights.pop()        
                         
        
        return res
        