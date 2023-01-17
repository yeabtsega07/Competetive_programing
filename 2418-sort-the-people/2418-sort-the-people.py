class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(len(heights) - 1):
            
            max_index = i
            for j in range(i + 1 ,len(heights)):
                
                if heights[max_index] < heights[j]:
                    max_index = j
                    
            if heights[max_index] != heights[i]:
                heights[i], heights[max_index] = heights[max_index], heights[i]
                names[i], names[max_index] = names[max_index], names[i]
                   
        return names
        