class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_=[]
        for i in nums:
            if not sum_:
                sum_.append(i)
            else:
                sum_.append(sum_[-1]+i)
        return sum_        
            