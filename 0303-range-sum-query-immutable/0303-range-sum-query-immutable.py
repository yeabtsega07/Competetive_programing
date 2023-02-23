class NumArray:

    def __init__(self, nums: List[int]):
        
        
        self.nums = [0] * (len(nums) + 1) 
        for i in range(1, len(self.nums) ):
            
            self.nums[i] += nums[i - 1] + self.nums[i - 1]
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.nums[right + 1] - self.nums[left]
        
        
            
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)