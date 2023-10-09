class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        check = defaultdict(list)
        for i, val in enumerate(nums2):
            check[val].append(i)
        @cache
        def recur(index, lastIndex):

            if lastIndex >= len(nums2):
                return 0
            
            if index >= len(nums1):
                return 0
            
            res  = 0
            for i in check[nums1[index]]:
                if i >= lastIndex:
                    res = max(res, 1 + recur(index + 1,  i + 1))
            
            res = max(res, recur(index + 1,  lastIndex))
            
            return res
        
        return recur(0, 0)