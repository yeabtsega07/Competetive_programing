class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        #Prefix sum
        nums = [0] + nums
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        
        monoQ = deque()
        
        n = len(monoQ)
        minLen, curSum = len(nums) , 0
        
        for i, num in enumerate(nums):
            
            while monoQ and num - monoQ[0][1] >= k:
                
                minLen = min(minLen, i - monoQ[0][0])
                monoQ.popleft()

            
            while monoQ and monoQ[-1][1] >= num:
                monoQ.pop()
                
            
            monoQ.append((i, num))
        
        return minLen if minLen < len(nums) else -1