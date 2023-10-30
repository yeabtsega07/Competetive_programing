
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = k, k
        result, cur_min = nums[k], nums[k]
        
        while 0 <= left and right < n:
            
            if left - 1 >= 0 and right + 1 < n: 
                if nums[left - 1] >= nums[right + 1]:
                    cur_min = min(cur_min, nums[left - 1])
                    left -= 1
                else:
                    cur_min = min(cur_min, nums[right + 1])
                    right += 1
                
                result = max(result, cur_min*(right - left + 1))
                
            else:
                break

        while 0 <= left:
            
            if left - 1 >= 0:
                cur_min = min(cur_min, nums[left - 1])
                left -= 1
                result = max(result, cur_min*(right - left + 1))
                
            else:
                break
            
            
        
        while right < n:
            
            if right + 1 < n:
                cur_min = min(cur_min, nums[right + 1])
                right += 1
                result = max(result, cur_min*(right - left + 1))
                
            else:
                break
                

        
        return result
        
        