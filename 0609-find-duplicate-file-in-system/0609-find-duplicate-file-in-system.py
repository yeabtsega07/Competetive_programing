class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        ans = list()
        
        for path in paths:
            parent, *files = path.split(' ')
            for file in files:
                name, type = file.split('(') 
                dict['('+type].append(parent+'/'+name)
        
        for k, v in dict.items():
            if len(v) > 1:
                ans.append(v)
        
        return ans