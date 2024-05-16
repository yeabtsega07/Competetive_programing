class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        summ = sum(nums)
        nums.sort(reverse=True)
        if summ % k != 0:
            return False
        value = summ//k

        @cache
        def backTrack(index,arr):
            if index == len(nums):
                return min(arr) == value
            answer = False
            for i in range(len(arr)):
                if arr[i] + nums[index] <= value:
                    new_arr = list(arr)
                    new_arr[i] += nums[index]
                    answer = answer or backTrack(index+1,tuple(new_arr))
                    # arr[i] -= nums[index]
            return answer

        return backTrack(0,tuple([0 for _ in range(k)]))