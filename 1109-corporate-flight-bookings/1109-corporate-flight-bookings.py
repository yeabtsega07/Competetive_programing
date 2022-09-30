class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre=[0]*n
        for book in bookings:
            pre[book[0]-1]+=book[2]
            if book[1]-1!=n-1:
                pre[book[1]+1-1]-=book[2]   
        for i,n in enumerate(pre):
            if i>0:
                pre[i]+=pre[i-1]
        return pre        
        
        
        