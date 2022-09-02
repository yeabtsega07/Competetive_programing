class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums=[i for i in range(1,n+1)]
        if k==1:
            return nums[-1]
        def recur(nums,k):
            if len(nums)==1:
                return nums[0]
            for i in range(k):
                if i==k-1:
                    nums.pop(0)
                else:    
                    val=nums.pop(0)
                    nums.append(val)
            return recur(nums,k)                    
        return recur(nums,k)
        