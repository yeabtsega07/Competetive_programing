class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        track = Counter(nums)
        count = list(track.items())

        k = len(count) - k
        
        def partition( count, low , high):
            
            pivot = count[low][1]
            
            i, j = low, high
            
            while i < j:
                
                while i <= high - 1 and  count[i][1] <= pivot:
                    i += 1
                
                while j >= low + 1 and  count[j][1] > pivot:
                    j -= 1
                
                if i < j:
                    count[i], count[j] = count[j], count[i]
            
            count[low], count[j] = count[j], count[low]
            
            return j
        
        def quickSort( nums, low, high):
            
            pi = partition( nums, low, high)
            
            if pi == k:
                return pi
            
            elif pi > k:
                return quickSort( nums, low, pi - 1)
            
            return quickSort(nums, pi + 1, high)
        
        index = quickSort( count, 0, len(count) - 1)
        result = []

        for i in range(index, len(count)):
            
            result.append(count[i][0])
        
        return result
        
                
        
        