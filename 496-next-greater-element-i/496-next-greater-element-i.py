#O(m*n) time complexity O(m) space complexity
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

#O(m+n) time complexity O(m) space complexity    
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1idx={}
        ans=[-1]*len(nums1)
        mon_stack=[]
        for i,num in enumerate(nums1):
            n1idx[num]=i
        for num in nums2:
            while mon_stack and num>mon_stack[-1]:
                val=mon_stack.pop()
                idx=n1idx[val]
                ans[idx]=num
            if num in nums1:
                mon_stack.append(num)
        return ans       
                    
    
    
            
        
