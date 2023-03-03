class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left, right = 0, len(arr) - 1
        
        while left <= right:
            
            mid = left + (right - left) // 2
            if mid < 1:
                return mid + 1

            if arr[mid - 1] < arr[mid] > arr[mid + 1]:

                return mid
            
            elif arr[mid - 1] >= arr[mid] > arr[mid + 1]:
                right = mid - 1
                

            else:
                left = mid + 1
                
        return mid