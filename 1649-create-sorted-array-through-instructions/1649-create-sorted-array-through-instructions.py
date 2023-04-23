from sortedcontainers import SortedList
class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        
        
        list_ = SortedList()
        res = 0
        for num in instructions:
            res += min(list_.bisect_left(num), len(list_) - list_.bisect_right(num))
            res %= (10 ** 9 + 7)
            list_.add(num)

        return res