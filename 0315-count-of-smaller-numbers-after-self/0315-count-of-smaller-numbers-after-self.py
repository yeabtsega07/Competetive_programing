class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        nums = [ [num, i] for i , num in enumerate(nums) ]
        result = [0] * len(nums)
        
        def mergeSort( nums, low, high ):
            
            if low >= high :
                return 
            
            mid = low + ( high - low ) // 2
            
            mergeSort( nums, low, mid)
            mergeSort( nums, mid + 1, high)
            merge( nums, low, mid, high )
            
        def merge( nums, low, mid, high ):
            
            j = mid + 1
            
            for i in range( low, mid + 1 ):
                
                while j <= high and nums[j][0] < nums[i][0]:
                    j += 1
                
                result[nums[i][1]] += (j - mid - 1)
                
            left, right = low, mid + 1
            cur = []
            while left <= mid and right <= high :
                
                if nums[left][0] <= nums[right][0]:
                    cur.append(nums[left])
                    left += 1
                else:
                    cur.append(nums[right])
                    right += 1
            
            while left <= mid:
                cur.append(nums[left])
                left += 1
            while right <= high:
                cur.append(nums[right])
                right += 1
            
            nums[ low : high + 1 ] = cur
            
            return
        
        mergeSort( nums, 0, len(nums) - 1 )
        return result