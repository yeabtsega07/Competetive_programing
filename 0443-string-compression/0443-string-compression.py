class Solution:
    def compress(self, chars: List[str]) -> int:
        count, slow = 1, 0
        
        for i in range(1, len(chars) + 1):
            
            if i < len(chars) and chars[i] == chars[i-1]:
                count += 1
            else:
                chars[slow] = chars[i-1]
                slow += 1
                if count > 1:
                    for j in str(count):
                        chars[slow] = j
                        slow += 1
                count = 1    
        chars = chars[:slow] 
        
        return len(chars)
            
                
        