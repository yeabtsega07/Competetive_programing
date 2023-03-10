class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def get_count(word):
            track, count = [0] * 26 , 0
            
            for char in word:
                
                indx = ord(char) - 97
                track[indx] += 1
            
            for i in range(27):
                
                if track[i]:
                    count = track[i]
                    break
            return count
        
        for i, query in enumerate(queries):
            
            queries[i] = get_count(query)
        
        for i, word in enumerate(words):
            
            words[i] = get_count(word)
        
        words.sort()
        result = []
        for query in queries:
            
            result.append(len(words) - bisect_right(words, query))
        
        return result
            
        