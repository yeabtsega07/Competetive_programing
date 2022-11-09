class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ev, od = [] , []
        
        for num in nums:
            if num % 2 :
                od .append(num)
            else:
                ev .append(num)
        
        for i in range(len(nums)):
            if i % 2:
                nums[i] = od.pop()
            else:
                nums[i] = ev.pop()
        
        return nums
        