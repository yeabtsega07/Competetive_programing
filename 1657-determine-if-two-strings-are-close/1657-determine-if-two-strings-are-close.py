class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        

        w1, w2 = [0]*26, [0]*26
        
        for i in range(len(word1)):
            
            w1[ord(word1[i]) - 97] += 1
            w2[ord(word2[i]) - 97] += 1
       
        
        for i in range(len(w1)):
            if w1[i] and not w2[i]:
                return False
            elif w2[i] and not w2[i]:
                return False
        
        return sorted(w1) == sorted(w2)
        
        
        
        
        """
        cabbba    abbccc
        c 1       c 3
        b 3       b 2
        a 2       a 1
        
        aacabb    bbcbaa
        a 3       a 2
        b 2       b 3
        c 1       c 1
        
        """
        