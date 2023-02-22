class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if  len(p) > len(s):
            return []
        
        dictP ,dictS = defaultdict(int), defaultdict(int)
        
        for char  in p:
            dictP[char] += 1
            
        start, ans = 0, [] 
        
        for end in range(len(s)):
            dictS[s[end]] += 1
            
            if  end - start + 1 == len(p):
                
                if dictP == dictS:
                    ans.append(start)
                
                dictS[s[start]] -= 1
                if dictS[s[start]] == 0:
                    dictS.pop(s[start])
                
                start += 1
        
        return ans
        
        