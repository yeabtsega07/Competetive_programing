class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt=Counter(arr)
        count=sorted(cnt.items(), key=lambda x:x[1])
        count.reverse()
        sum_,i=0,0
        while sum_<len(arr)//2:
            sum_+=count[i][1]
            i+=1
        return i  