class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def get_index(nums, target):
            
            left, right = 0, len(nums) - 1
            
            while left <= right :
                
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            return -1 
        
        check = get_index(nums, target)
        if check == -1:
            return [-1, -1]
        else:
            ans = []
            
            while check > 0:
                
                if nums[check - 1] == target:
                    check -= 1
                else:
                    break
                    
            ans.append(check)
            
            while check < len(nums) - 1:

                if nums[check + 1] == target:
                    check += 1
                else:
                    break
            
            ans.append(check)
            return ans
            
        