class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        asc = [0] * len(rating)
        dec = [0] * len(rating)
        
        left = 0
        count = 0
        
        for right  in range(1, len(rating)):
             
            while left < right:
                if rating[left] < rating[right]:
                    count += 1
                left += 1
                
            asc[right] = count
            count = 0
            left = 0
        
        right = len(rating) - 1
        count = 0
        for left  in range(len(rating) - 2, -1, -1 ):
            
            while left < right:
                if rating[left] > rating[right]:
                    count += 1
                right -= 1

            dec[left] = count
            count = 0
            right = len(rating) - 1
        
        res = 0
        
        left = 0
        for right  in range(1, len(rating)):
             
            while left < right:
                if rating[left] < rating[right]:
                    res += asc[left]
                left += 1
            left = 0
        
        right = len(rating) - 1
        for left  in range(len(rating) - 2, -1, -1 ):
            
            while left < right:
                if rating[left] > rating[right]:
                    res += dec[right]
                right -= 1
            right = len(rating) - 1
        
        return res