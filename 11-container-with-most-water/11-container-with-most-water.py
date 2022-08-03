class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        left,right=0,len(height)-1
        while left<right:
            if height[left]<height[right]:
                area=max((height[left]*(right-left)),area)
                left+=1
            elif height[left]>height[right]:
                     area=max((height[right]*(right-left)),area)
                     right-=1
            else:
                area=max((height[left]*(right-left)),area)
                left+=1
                right-=1
        return area    
        