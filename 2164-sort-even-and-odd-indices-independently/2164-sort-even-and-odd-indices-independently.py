class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        ev, od = [] , []
        
        for i in range(len(nums)):
            if i % 2:
                od .append(nums[i])
            else:
                ev .append(nums[i])
                
        ev.sort(reverse = True)
        od.sort()
        
        for i in range(len(nums)):
            
            if i % 2:
                nums[i] = od.pop()
            else:
                nums[i] = ev.pop()
        
        return nums
            
        