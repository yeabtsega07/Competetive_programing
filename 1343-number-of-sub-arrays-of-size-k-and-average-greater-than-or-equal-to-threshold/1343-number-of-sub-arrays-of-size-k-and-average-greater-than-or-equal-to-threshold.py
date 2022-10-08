class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_=0
        slow,fast=0,0
        res=0
        while fast<len(arr):
            sum_+=arr[fast]
            if (fast-slow)==k-1:
                if sum_//k>=threshold:
                    res+=1
                sum_-=arr[slow]
                slow+=1
            fast+=1
        return res    
        