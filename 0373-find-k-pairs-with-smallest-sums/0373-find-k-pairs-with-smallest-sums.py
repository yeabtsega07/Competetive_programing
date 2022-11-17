class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        
        def add(i ,j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(heap, [nums1[i] + nums2[j] , i ,j])
            
        add(0, 0)
        res = []
        
        while heap and len(res) < k:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            add(i, j+1)
            # print(j)
            if j == 0:
                add(i+1, 0)
        
        return res
            
        
        