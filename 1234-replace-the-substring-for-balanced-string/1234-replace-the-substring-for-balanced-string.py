class Solution:
    def balancedString(self, s: str) -> int:
        
        track = {"Q":0,"W":0,"R":0,"E":0}
        for char in s:
            track[char] += 1
        
        k = len(s) // 4
        check = defaultdict(int)
        
        for char in ["Q","W","E","R"]:
            
            if track[char] > k:
                check[char] = track[char] - k

        if not check:
            return 0
        else:
            
            check = Counter(s)
        
        count = defaultdict(int)
        result, left = float("inf"), 0
        
        def are_same(dict1, dict2):
            
            for char in dict2:
                if dict2[char] - dict1[char] > k :
                    return False
            return  True
               
        for i in range(len(s)):
            
            char = s[i]
            count[char] += 1
            
            while count and are_same(count, check):
                result = min(result, i - left + 1)
                count[s[left]] -= 1
                left += 1
                
            
                         
        return result     
                
                