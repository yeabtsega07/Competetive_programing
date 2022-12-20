class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """



        if n == 0:
            return nums1
        
        n1, n2 = m - 1, n - 1
        for i in range(len(nums1) - 1, -1 , -1):
            
            if n2 >= 0 and nums2[n2] > nums1[n1]:
                nums1[i] = nums2[n2]
                n2 -= 1
            elif n1 >= 0  and nums1[n1] >= nums2[n2]:
                nums1[i] = nums1[n1]
                n1 -= 1
            elif n1 < 0 and n2 >= 0:
                nums1[i] = nums2[n2]
                n2 -= 1
            elif n2 < 0:
                break
        # print(i)
                


        
            
            