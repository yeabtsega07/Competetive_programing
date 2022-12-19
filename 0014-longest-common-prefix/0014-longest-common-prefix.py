class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        
        for j  in range(1, len(strs)):
            check = ""
            for i, char in enumerate(ans):
                if i < len(strs[j]):
                    if char != strs[j][i]:
                        break
                    
                    else:
                        check += char
            ans = check        
        return ans 
            
        