class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first = ""
        
        for char in word1:
            first += char
        
        second = ""
        
        for char in word2:
            second += char
        
        return first == second
        