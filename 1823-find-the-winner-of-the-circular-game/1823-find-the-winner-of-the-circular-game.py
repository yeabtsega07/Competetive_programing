class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=[i for i in range(1,n+1)]
        if k==1:
            return nums[-1]
        def recur(nums,k,i=0):
            if len(nums)==1:
                return nums[0]
            i=(i+k)%len(nums)
            nums.pop(i)
            return recur(nums,k,i)                    
        return recur(nums,k-1)
        