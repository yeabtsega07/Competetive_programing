class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        dicti={}
        max_=-1
        res=-1
        for n in nums:
            if n%2==0:
                dicti[n]=dicti.get(n,0)+1
                if dicti[n]>max_:
                    res=n
                elif dicti[n]==max_ and n<res:
                    res=n
                max_=max(max_,dicti[n])
        return res   
        