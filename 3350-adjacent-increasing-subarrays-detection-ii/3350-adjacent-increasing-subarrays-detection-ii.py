class Solution:
    def maxIncreasingSubarrays(self, arr: List[int]) -> int:
        
        def helper(idx , arr):
            idx2 = idx
            n = len(arr)
            while idx2 + 1 < n and arr[idx2]<arr[idx2+1]:
                idx2 += 1

            return idx2 - idx + 1
        
        n=len(arr)
        prev_len = helper(0,arr)
        ans=prev_len//2
        l=prev_len
        r=0

        while l<n:
            # the lenght will be r-l+1
            curr_len=helper(l, arr)

            ans = max(ans, curr_len // 2)
            ans = max(ans, min(prev_len,curr_len))


            # l = 2 , r = 2
            # l = 2 , r = 3
            prev_len = curr_len
            l += curr_len
        return ans