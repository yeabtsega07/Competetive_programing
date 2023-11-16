class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        check = set(nums)
        res = [""]
        
        def backtrack (index, cur):
            
            if index >= len(nums):
                binary_str = "".join(cur)
                if binary_str not in check:
                    res[0] = binary_str
                
                return
            
            cur.append("0")
            backtrack(index + 1, cur)
            cur.pop()
            
            cur.append("1")
            backtrack(index + 1, cur)
            cur.pop()
        
        backtrack(0, [])
        
        return res[0]
        