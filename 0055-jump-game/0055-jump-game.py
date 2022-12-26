class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jump, goal = n - 2, n - 1
        
        while jump >= 0:
            if nums[jump] >= goal - jump:
                goal = jump
            jump -= 1
        
        return goal == 0
            
        