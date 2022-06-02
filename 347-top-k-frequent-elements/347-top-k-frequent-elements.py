class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        count=Counter(nums)
        c=sorted(count.items(),key=lambda x:x[1])
        c.reverse()
        ans=[]
        for i in range (k):
            ans.append(c[i][0])
        return ans 
        