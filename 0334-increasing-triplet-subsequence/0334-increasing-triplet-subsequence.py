class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        num1 = num2 = float("inf")
        
        for num in nums:
            
            if num <= num1:
                num1 = num
            elif num <=num2:
                num2 = num
            else:
                return True
        
        return False