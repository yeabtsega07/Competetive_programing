class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(heights) - 1):
            flag = True
            for j in range(i,len(heights)):
                
                if heights[i] <= heights[j]:
                    names[i], names[j] = names[j], names[i]
                    heights[i], heights[j] = heights[j], heights[i]
                    flag = False
            if flag:
                return names
                    
        return names
        