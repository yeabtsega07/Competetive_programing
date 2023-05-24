class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        res = 0
        while k:
            if numOnes:
                res += 1
                numOnes -= 1
            elif numZeros:
                numZeros -= 1
            else:
                res -= 1
                numNegOnes -= 1
            
            k -= 1
        return res     
                