class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = defaultdict(int)
        for i, char in enumerate(s):
            
            lastIndex[char] = max(lastIndex[char], i)
        
        count = pre = max_ = 0
        ans = []
        for i, char in enumerate(s):
            max_ = max(max_, lastIndex[char])
            count += 1
            
            if count + pre - 1 == max_:
                ans.append(count)
                pre += count
                count = 0
        
        return ans
            

            