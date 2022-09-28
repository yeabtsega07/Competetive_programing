class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        pre={}
        sum_=0
        max_=0
        for i,h in enumerate(hours):
            if h>8:
                sum_+=1  
            else: sum_-=1
            if sum_ not in pre.keys():
                pre[sum_]=i
            if sum_>0:
                max_=i+1
            elif sum_-1 in pre.keys():
                max_=max(i-pre[sum_-1],max_)
        return max_        
                

                

        