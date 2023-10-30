class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        graph = {"a":["e"], "e": ["a", "i"], "i":["a", "e","o", "u"], "o": ["i", "u"], "u": ["a"]}
        
        result = [0]
        memo = {}
        
        def recur(val, count):
            
            if (val, count) in memo:
                return memo[(val, count)]
            
            if count == n:
                return 1
            
            cur = 0
            for child in graph[val]:
                cur += recur(child, count + 1)
            
            memo[(val, count)] = cur
            
            return cur
            
        result = 0
        for val in ["a", "e", "i", "o", "u"]:
            result += recur(val, 1)
        
        return result % (10 ** 9 + 7)