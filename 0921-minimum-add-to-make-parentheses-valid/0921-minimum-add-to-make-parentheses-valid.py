class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        left_cnt, right_cnt = 0, 0
        
        for pare in s:
            
            if pare == "(":
                left_cnt += 1
            else:
                if left_cnt:
                    left_cnt -= 1
                else:
                    right_cnt += 1
        
        return left_cnt + right_cnt
        