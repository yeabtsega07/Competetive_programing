class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(nums, target):
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2 

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return left
            
        check = zip(*matrix)
        for col in check:
            indx = binary(col, target)
            if indx < len(col) and col[indx] == target:
                return True
            break
            
        ans = binary(matrix[indx - 1], target)
        # print(ans, matrix[indx - 1], target)
        
        if ans < len(matrix[indx - 1]) and matrix[indx - 1][ans] == target:
            return True
        else:
            return False
            
