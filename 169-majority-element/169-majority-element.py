class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur=0
        cnt=0
        for n in nums:
            if not cnt:
                cur=n
                cnt+=1
                continue
            if n!=cur:
                cnt-=1
            else:
                cnt+=1
            if not cnt:
                cur=n
                cnt+=1
        return cur       
                
         
       