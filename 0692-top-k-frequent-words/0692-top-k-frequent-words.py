class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        track = Counter(words)
        frequency = [(-freq, word) for word, freq in track.items()]
        heapify(frequency)
        res = []  
        
        
        while k:

            check = heappop(frequency)
            res.append(check[1])
            k -= 1

            
        return res
        