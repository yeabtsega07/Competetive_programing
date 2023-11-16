class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        check = set(nums)
        for cur in product("01", repeat = len(nums)): 
            binary_str = "".join(list(cur))
            if binary_str not in check: 
                return binary_str
            