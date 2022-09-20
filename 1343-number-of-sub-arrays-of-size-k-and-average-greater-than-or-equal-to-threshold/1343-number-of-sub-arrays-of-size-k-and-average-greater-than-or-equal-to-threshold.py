class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        track=0
        count=0
        lft,rgt=0,0
        res=0
        while rgt<len(arr):
            track+=arr[rgt]
            count+=1
            if count==k:
                if track/k>=threshold:
                    res+=1
                track-=arr[lft]
                lft+=1
                count-=1
            rgt+=1
        return res     
        