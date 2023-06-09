class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        dp = [-1] * len(arr)
        dp[0] = 1
        def recur ( index ):
            
            if index  == 0 :
                arr[0] = 1
                return 1
            
            check = recur( index - 1 )
            if abs(check - arr[index]) <= 1:
                dp[index] = arr[index]
            else:
                dp[index] = check + 1
            
            return dp[index]
        
        recur( len(arr) - 1 )
        # print(dp)
        
        return max(dp)
        
        