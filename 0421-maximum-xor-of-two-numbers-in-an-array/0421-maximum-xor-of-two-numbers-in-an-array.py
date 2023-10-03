class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        res, mask = 0, 0
        
        for i in reversed(range(32)):  
            mask |= (2 ** i)
            hashSet = {mask & val for val in nums}
            cur = res | (2 ** i)
            for val in hashSet:  

                if cur ^ val in hashSet:
                    res = cur
                    break
        return res