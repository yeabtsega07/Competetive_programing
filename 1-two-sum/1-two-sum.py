class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track={}
        for i in range(len(nums)):
            
            if nums[i] in track:
                return track[nums[i]],i
            else:
                track[target-nums[i]]=i
            