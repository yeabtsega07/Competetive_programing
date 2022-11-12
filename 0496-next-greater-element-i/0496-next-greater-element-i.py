class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        track = {}
        stack = []
        
        for  i,num in enumerate(nums2):
            
            while stack and stack[-1] < num:
                val = stack.pop()
                track[val] = num
            
            stack . append(num)
        
        ans = []
        for num in nums1:
            
            if num in track.keys():
                ans.append(track[num])
            else:
                ans.append(-1)
        
        return ans