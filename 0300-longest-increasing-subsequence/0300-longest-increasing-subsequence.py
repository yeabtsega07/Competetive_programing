class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        

        dp = {len(nums) - 1 : 1}
        
        def recur ( index ):
            
            if index >= len(nums):
                return 0
            
            
            if index in dp:
                
                return dp[index]
            
            cur = 0
            for i in range (index + 1, len(nums)):
                
                if nums[index] < nums[i]:
                
                    if i in dp:
                        take = dp[i]
                    else:    
                        take = recur( i )

                    cur = max(cur, take)

            
            dp[index] = cur + 1

            
            return dp[index]
        
        for i in range(len(nums)):
            if i not in dp:

                recur(i)


        return max(dp.values())
        