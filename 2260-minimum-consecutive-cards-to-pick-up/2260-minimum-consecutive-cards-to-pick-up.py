class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = float("inf")
        left = 0
        seen = defaultdict(int)
        for right ,num in enumerate(cards):
            
            if num not in seen.keys():
                seen[num] = right
            else:
                res = min(res, right-seen[num]+1)
                seen[num] = right
        
        return  res if res != float("inf") else -1
            
        