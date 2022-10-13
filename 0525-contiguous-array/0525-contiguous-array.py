class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        pre={0:-1}
        res,count=0,0
        for i,n in enumerate(nums):
            if n==0:
                count-=1
            else:
                count+=1
            if count in pre.keys():
                res=max(res,i-pre[count])
            else:
                pre[count]=i
        return res        
            
            

                
        