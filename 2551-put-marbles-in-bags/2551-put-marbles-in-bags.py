class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        
        pairs = [ weights[i] + weights[i - 1] for i in range(1, len(weights))]
        pairs.sort()
        
        left, right = 0, len(pairs) - 1
        result = 0
        
        while k > 1:

            result += pairs[right] - pairs[left]
            left += 1
            right -= 1
            k -= 1
            
        return result
            
            
        