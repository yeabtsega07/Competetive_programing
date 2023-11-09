class Solution:
    def countHomogenous(self, s: str) -> int:
        
        
        cur, count = s[0], 1
        result = 0
        
        for i in range(1, len(s)):

            if cur != s[i]:
                
                for j in range(count + 1):
                    result += j
                    
                count = 1
                cur = s[i]
                
            else:
                count += 1
            

        if count:
            for i in range(count + 1):
                    result += i
        
        return result % (10 ** 9 + 7)
            
            
            