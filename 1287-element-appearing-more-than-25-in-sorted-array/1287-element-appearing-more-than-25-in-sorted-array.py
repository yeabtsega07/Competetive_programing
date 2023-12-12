class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        return max(count.items(), key = lambda x:x[1])[0]