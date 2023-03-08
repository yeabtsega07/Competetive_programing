class Solution:
    def hIndex(self, citations: List[int]) -> int:
#         pos = []
        
#         def bisect( nums ):
            
#             left, right = 0, max(citations)
            
#             while left <= right:
                
#                 mid = left + (right - left) // 2
                
#                 check = bisect_left(citations, mid)
#                 if mid <= len(nums) - check :

#                     pos.append([mid, len(nums) - check])
#                     left = mid + 1
#                 else:
#                     right = mid - 1
        
#         bisect(citations)
#         # print(pos)
#         return pos[-1][0]
        left , right = 0 , len(citations) - 1

        while left <= right:
            
            mid = left + (right - left) // 2
            
            if citations[mid] == len(citations) - mid:
                return citations[mid]
            
            elif citations[mid] > len(citations) - mid:
                right = mid - 1
            else:
                left = mid + 1
                
        return len(citations) - left
        