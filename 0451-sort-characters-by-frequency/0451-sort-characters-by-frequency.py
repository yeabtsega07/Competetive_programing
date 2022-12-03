class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = ""
        for char, cnt in reversed(sorted(count.items(),key = lambda x:x[1])) :
            res += (char * cnt)
            
        return res    