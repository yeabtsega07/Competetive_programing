class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        def binary(target):
            l, r = 0, len(nums)-1
            ans = -1
            
            while l<=r:
                mid = (l+r)//2
        
                if nums[mid] == target:
                    return mid+1
                elif nums[mid] > target:
                    ans = mid
                    r = mid-1
                else:
                    l = mid+1

            return len(nums) if ans ==-1 else ans        
        nums.sort()
        
        for i in range(1,len(nums)):
            
            nums[i] += nums[i-1]
            
            
        res = []
        
        for i in queries:
            res.append(binary(i))
        
        return res    
            
        
 