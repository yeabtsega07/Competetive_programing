class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        
        track  = { "T":0, "F":0 }
        left, result = 0, 0
        
        for right in range( len(answerKey) ):
            
            track[answerKey[right]] += 1

            while min(track.values()) > k and left <= right:

                track[answerKey[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            
        
        
        return result
                
        
        
        