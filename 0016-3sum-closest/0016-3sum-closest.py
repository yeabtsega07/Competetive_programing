class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res=[]
        nums.sort()
        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
                
            left,right=i+1,len(nums)-1
            while left<right:
                temp=n+nums[left]+nums[right]
                res.append(temp)
                if temp>target:
                    right-=1
                    while nums[right]==nums[right+1] and left<right:
                        right-=1
                else:
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                    
        ans=float("inf")            
        for n in res:
            if abs(ans-target)>abs(n-target):
                ans=n
        return ans    
            
        