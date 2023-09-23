class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        
        @cache
        def recur ( index1, index2 ):
            
            if index1 < 0 or index2 < 0:
                return 0
            
            
            take  = notTake = 0

            if text1[index1] == text2[index2]:
                take = 1 + recur(index1 - 1, index2 - 1)
            else:
                notTake = max(recur(index1 - 1, index2), recur(index1, index2 - 1))

            
            return max(take, notTake)
        
        cur = recur(len(text1) - 1, len(text2) - 1)


        res = len(text1) - cur if len(text1) - cur >= 0 else 0
        res += len(text2) - cur if len(text2) - cur >= 0 else 0
        return res
        