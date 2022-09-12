class Solution:
    def compress(self, chars: List[str]) -> int:
        s=""
        slow=0
        fast=0
        while slow<len(chars):
            if fast==len(chars):
                break
            char=chars[slow]
            s+=char

            count=0    
            while fast<len(chars):
                if chars[fast]==char:
                    fast+=1
                    count+=1
                else:
                    slow=fast
                    break
            if count>1:        
                s+=str(count)
        for i,char in enumerate(s):
            chars[i]=char
        chars=chars[:len(s)]    
        return len(chars)
            
                
        