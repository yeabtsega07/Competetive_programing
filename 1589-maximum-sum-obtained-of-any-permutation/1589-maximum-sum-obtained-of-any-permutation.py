class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        track = [0] * (len(nums) + 1)
        
        for start, end in requests:
            track[start] += 1
            track[end + 1] -= 1
        
        for i in range(1 , len(track)):
            track[i] += track[i - 1]
            
        nums.sort(reverse = True)
        track.sort(reverse = True)
        ans, left = 0, 0
        for count in track:
            
            if count:
                ans += nums[left] * count
                left += 1
            else:
                break
                
        return ans % ( 10 ** 9 + 7)