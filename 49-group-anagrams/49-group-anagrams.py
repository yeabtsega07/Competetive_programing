class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=defaultdict(list)
        for i in strs:
            count=[0]*26
            for s in i:
                count[ord(s)-ord("a")]+=1
            dict[tuple(count)].append(i) 
        return dict.values()    
                
            
        
        