class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def check(time):
            running_sum = 0

            for i in batteries:
                running_sum += min(i , time)

            return running_sum >= n * time

        low, high = 0, sum(batteries) // n

        while low <= high:
            
            mid = (low + high) // 2
            if check(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high