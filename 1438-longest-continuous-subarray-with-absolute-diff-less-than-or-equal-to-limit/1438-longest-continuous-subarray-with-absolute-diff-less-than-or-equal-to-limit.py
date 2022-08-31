class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        slow=0
        res=0
        inc=deque()
        dec=deque()
        for fast,num in enumerate(nums):
            while dec and num>dec[-1]:
                dec.pop()
            dec.append(num)    
            while inc and num<inc[-1]:
                inc.pop()
            inc.append(num)    
            while dec[0]-inc[0]>limit:
                if dec[0]==nums[slow]:
                    dec.popleft()
                if inc[0]==nums[slow]:
                    inc.popleft()    
                slow+=1
            res=max(res,1+fast-slow)    

        return res       
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         left,rigth=0,1
#         count=0
#         for i in range(len(nums)-1):
#             max_abs=0
#             for j in range(len(nums)):
#                 if abs(nums[i]-nums[j]) >= max_abs:
#                     max_abs=abs(nums[i]-nums[j])
#                     if abs(nums[i]-nums[j])<=limit:
#                         if j-i+1>count:
#                             print(nums[i:j+1])
#                             count=j-i+1

#         return count  
        
        