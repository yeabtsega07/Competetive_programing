class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        res=[]
        for i,ana in enumerate(strs):
            hashmap[i]=sorted(ana)
        cur=[] 
        
        for  ana in sorted(hashmap.items(),key=lambda x:x[1]):
            if cur and ana[1]!=sorted(cur[-1]):
                res.append(cur)
                cur=[]
                cur.append(strs[ana[0]])
            else:
                cur.append(strs[ana[0]])
        if cur: res.append(cur)        
        return res       
                
            
        
        