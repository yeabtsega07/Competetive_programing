class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        if min(len(nums1),len(nums2))==len(nums1):
            for i in range(len(nums1)):
                num=nums1[i]
                for n in nums2:
                    if num==n and num not in res:
                        res.append(num)
                        break
        else:
            for i in range(len(nums2)):
                num=nums2[i]
                for n in nums1:
                    if num==n and num not in res:
                        res.append(num)
                        break
                    
        return res            
                        
                        
            
            
        