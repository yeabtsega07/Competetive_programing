class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        
        @cache
        def recur ( index, current_height, remaining_w):
            
            # base case
            if index >= len(books):
                return current_height
            
            # First choice place the book on the current shelf
            ans = float("inf")
            if books[index][0] <= remaining_w:
                ans = min(ans, recur(index + 1, max(current_height, books[index][1]), remaining_w - books[index][0]))
            
            # Second choice place the book on the next shelf
            
            ans = min(ans, current_height + recur(index + 1, books[index][1], shelfWidth - books[index][0]))
            
            return ans
        
        return recur(0, 0, shelfWidth)