class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        [42, 11, 1, 97]
        [24, 11, 1, 79]
        1 1 1 1 1
        (0,1)(0,2)(0,3)(0,)
        
        2 - 1
        3 - 3
        4 - 6
        5 -
        
        """
        
        diff = []
        for val in nums:
            reverse_val = int(str(val)[:: - 1])
            diff.append(val - reverse_val)
        
        count = defaultdict(int)
        for i in range(len(diff) - 1, -1, -1):
            
            count[diff[i]] += 1
        

        result = 0
        for key in count:
            for val in range(1, count[key]):
                result += val
        
        return result % (10 ** 9 + 7)