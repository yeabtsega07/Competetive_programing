class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) % 2:
            return 0
        
        track, target = set(), sum(nums) // 2
        track.add(0)
        track.add(nums[-1])
        
        for i in range(len(nums) - 2, -1 , -1):
            
            if nums[i] == target:
                return 1
            
            temp = set()
            for val in track:
                
                if val + nums[i] == target:
                    return 1
                
                temp.add(val + nums[i])
                
            track = track.union(temp)   

        
        return target in track
                