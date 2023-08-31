class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        n1, n2 = nums1, nums2
        
        if len(nums2) < len(nums1) :
            n1 = nums2
            n2 = nums1
        
        total = len(n1) + len(n2)
        half = total // 2
        
        left, right = 0, len(n1) - 1
        
        while True:
            
            mid1 = (left + right) // 2
            mid2 = half - (mid1 + 2)
            
            n1Mid = n1[mid1] if mid1 >= 0 else -float("inf")
            n1Right = n1[mid1 + 1] if (mid1 + 1) < len(n1) else float("inf")
            n2Mid = n2[mid2] if mid2 >= 0 else -float("inf")
            n2Right = n2[mid2 + 1] if (mid2 + 1) < len(n2) else float("inf")
            
            if n1Mid <= n2Right and n2Mid <= n1Right:
                
                if total % 2:
                    return min(n1Right, n2Right)
                return (max(n1Mid, n2Mid ) + min(n1Right, n2Right)) / 2
            
            if n1Mid > n2Right:
                right = mid1 - 1
            else:
                left = mid1 + 1
                
        
        