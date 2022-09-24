class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        # if m==0:
        #     return nums2[:n]
        # elif n==0:
        #     return nums1[:m]
        pt1=0
        pt2=0
        nums=[]
        while pt1<m and pt2<n:
            if nums1[pt1]< nums2[pt2]:
                nums.append(nums1[pt1])
                pt1+=1
            else:
                nums.append(nums2[pt2])
                pt2+=1       
        if pt1<m:
            nums=nums+nums1[pt1:m]
        if pt2<n:
            nums=nums+nums2[pt2:n]
        for i,num in enumerate (nums):
            nums1[i]=num
           
            
            
        