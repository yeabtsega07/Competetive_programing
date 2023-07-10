class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = { len(s) : 1 }

        
        def recur ( index ):
            
            if index in dp:
                return dp[index]

            if s[index] == "0":
                return 0
            
            alone = recur ( index + 1 )
            grouped = 0
            if index + 1 < len(s) and ( s[index] == "1" or s[index] == "2" and int(s[index + 1])  < 7):
                grouped = recur( index + 2)
            
            dp[index] = alone + grouped

            return dp[index]
        
        return recur(0)