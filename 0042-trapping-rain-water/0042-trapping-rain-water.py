class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        
        left, right = 0, len(height) - 1
        lMax, rMax, ans = height[0] , height[-1], 0
        
        while left <= right:
            # print(left, right , height[left], height[right])
            
            if height[left] >= lMax:
                lMax = height[left]
            
            if height[right] >= rMax:
                rMax = height[right]
            
            if lMax <= rMax:
                ans += lMax - height[left]
                left += 1
            
            else:
                ans += rMax - height[right]
                right -= 1
                
        
        return ans
                
        