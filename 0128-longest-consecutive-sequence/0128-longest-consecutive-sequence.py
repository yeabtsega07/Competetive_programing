class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elms=set(nums)
        count=0
        for i in elms:
            if i-1 in elms:
                continue
            else:
                num=i
                cur_cnt=1
                while num+1 in elms:
                    cur_cnt+=1
                    num+=1
                count=max(cur_cnt,count)    
        return count 
        