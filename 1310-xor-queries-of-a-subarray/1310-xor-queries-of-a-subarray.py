class Solution:
    def xorQueries(self, arr: List[int], qu: List[List[int]]) -> List[int]:
        pre=[0]*len(arr)
        for i,n in enumerate(arr):
            if not pre:
                pre[i]=n
                continue
            pre[i]=pre[i-1]^n
        
        ans=[]
        for i in qu:
            if i[0]==0:
                ans.append(pre[i[1]])
            else:   
                 ans.append(pre[i[1]]^pre[i[0]-1])
         
        return ans
            
         
        
        