class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(1, len(heights)):
            
            cur_name = names[i]
            cur_height = heights[i]
            ind = i 
            while ind > 0 and cur_height > heights[ind - 1]:
                heights[ind] = heights[ind - 1]
                names[ind] = names[ind - 1]
                ind -= 1
            
            names[ind] =  cur_name
            heights[ind] = cur_height
                       
        return names
        