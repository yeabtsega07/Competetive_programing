class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        def get_subsequence(index, nums,k, t = []):


            if index >= len(nums):
                if len(t) == k:
                    res.append(t[:])
                return 


            t.append(nums[index])
            get_subsequence(index + 1, nums,k ,t)

            t.pop()
            get_subsequence(index + 1, nums,k, t)
            
        nums = [i for i in range(1, n + 1)]
        get_subsequence(0, nums, k)
        
        return res
            