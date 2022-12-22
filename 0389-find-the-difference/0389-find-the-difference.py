class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt1 = Counter(s)
        cnt2 = Counter(t)
        res = ""
        
        for i in cnt2.keys():
            if i not in cnt1.keys():
                res += i
            else:
                if cnt1[i] < cnt2[i]:
                    res += i
        return res   