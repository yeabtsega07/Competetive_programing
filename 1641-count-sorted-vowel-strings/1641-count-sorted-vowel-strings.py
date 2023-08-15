class Solution:
    def countVowelStrings(self, n: int) -> int:
        
        vowels = [1,1,1,1,1]
        
        for i in range(1, n):
            
            for j in range(3, -1, -1):
                
                vowels[j] += vowels[j + 1]
        
        return sum(vowels)
                