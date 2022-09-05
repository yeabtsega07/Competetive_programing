class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        dict={1:"0"}
        def recur(n):
            if n not in dict:
                dict[n]=recur(n-1)+"1"
                add=""
                for i in range(len(dict[n])-1):
                    if dict[n][i]=="0":
                        add+="1"
                    else:
                        add+="0"    
                dict[n]=dict[n]+add[::-1]
                add=""      
            return dict[n] 
        return recur(n)[k-1]
        