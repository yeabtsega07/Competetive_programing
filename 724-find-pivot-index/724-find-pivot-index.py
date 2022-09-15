class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum=[0]*len(nums)
        for i ,num in enumerate(nums):
            if i ==0:
                prefixsum[i]=num
            else:
                prefixsum[i]=prefixsum[i-1]+num 
        i=0
        while i<len(prefixsum):
            if i==0:
                if 0==(prefixsum[len(nums)-1]-nums[i]):
                    return 0
            elif prefixsum[i-1]==(prefixsum[len(nums)-1]-prefixsum[i-1]-nums[i]):
                return i
            i+=1
        return -1    
  
        