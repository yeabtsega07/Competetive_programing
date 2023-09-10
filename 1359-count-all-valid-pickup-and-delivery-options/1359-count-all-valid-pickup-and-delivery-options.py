class Solution:
    def countOrders(self, n: int) -> int:
        

        
        def recur( index, slots ):
            
            if index  <= 0 or slots <= 0:
                return 1
            
            cur = (slots * ( slots - 1 )) // 2
            return cur * recur(index - 1, slots - 2)
        
        return recur( n , 2 * n) % (10 ** 9 + 7)
            