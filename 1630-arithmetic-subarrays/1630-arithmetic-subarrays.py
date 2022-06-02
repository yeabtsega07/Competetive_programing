class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]
        m= len(l)
        for i in range(m):
            check=[]
            for j in range(l[i],r[i]+1):
                check.append(nums[j])
            check.sort()    
            for k in range(len(check)-1):
                diff=check[1]-check[0]
                if diff!= check[k+1]-check[k]:
                    bo=False
                    break
                else:
                    bo=True
            ans.append(bo)       
        return ans  
        