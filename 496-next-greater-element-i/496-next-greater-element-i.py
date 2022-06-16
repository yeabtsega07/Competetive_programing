class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        for i in nums1:
            ind=nums2.index(i)
            if len(nums2)>=ind+2:
                for j in range(ind+1,len(nums2)):
                    nxt=-1
                    if i<nums2[j]:
                        nxt=nums2[j]
                        break
                output.append(nxt)       
            else:
                output.append(-1)
        return output        
            
        