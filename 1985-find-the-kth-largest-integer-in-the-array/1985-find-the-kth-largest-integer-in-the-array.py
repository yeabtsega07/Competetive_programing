class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        temp=(int(i) for i in nums)
        count=1
        for i in sorted(temp,reverse=True):
            if count==k:
                return str(i)
            count+=1
        