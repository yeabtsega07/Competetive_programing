class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        for i, word in enumerate(words):
            words[i] = set(word)
        
        count = 0
        for i in range(len(words) - 1):
            for j in range(i + 1 , len(words)):
                if words[i] == words[j]:
                    count += 1
                    
        return count            
        
        