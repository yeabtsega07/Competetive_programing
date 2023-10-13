# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        
        def get_peak(arr):
            left, right = 0, arr.length() - 1
        
            while left <= right:

                mid = left + (right - left) // 2
                
                if mid < 1:
                    return mid + 1

                if arr.get(mid - 1) < arr.get(mid) > arr.get(mid + 1):

                    return mid

                elif arr.get(mid - 1) >= arr.get(mid) > arr.get(mid + 1):
                    right = mid - 1


                else:
                    left = mid + 1

            return mid
        

        peak = get_peak(mountain_arr)

        def binary(arr):
            left, right = 0, peak 
            if peak > 0:
                if arr.get(peak - 1)  < arr.get(peak):
                    right = peak
                else:
                    right = peak - 1
            
            while left <= right:
                
                mid = (left + right) // 2
                mid_val = arr.get(mid) 
                
                if mid_val == target:
                    return mid
                elif mid_val > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        
        def binary_reverse(arr):
            left, right = peak ,  arr.length() - 1
            
            if peak < arr.length() - 1:
                if arr.get(peak + 1) < arr.get(peak):
                    left = peak
                else:
                    left = peak + 1
            
            while left <= right:
                
                mid = (left + right) // 2
                mid_val = arr.get(mid) 
                
                if mid_val == target:
                    return mid
                elif mid_val < target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1
        
        res1 = binary(mountain_arr)
        res2 = binary_reverse(mountain_arr)
        
        if res1 == -1 or res2 == -1:
            return max(res1, res2)
        return min(res1, res2)

        
        
                    