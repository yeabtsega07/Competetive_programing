class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
            ans = []
            left, right = 0, 0
            
            while left < len(word1) and right < len(word2):
                
                if word1[left] > word2[right]:
                    ans.append(word1[left])
                    left += 1
                elif word1[left] < word2[right]:
                    ans.append(word2[right])
                    right += 1
                else:
                    if word1[left:] > word2[right:]:
                        ans.append(word1[left])
                        left += 1
                    else:
                        ans.append(word2[right])
                        right += 1
                        
            while right < len(word2):
                ans.append(word2[right])
                right += 1
                
            while left < len(word1):  
                ans.append(word1[left])
                left += 1
                
            return "".join(ans)       
