class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        for i in range(1, len(heights)):
            
            cur_name = names[i]
            cur_height = heights[i]
            ind = i - 1
            while ind >= 0 and cur_height > heights[ind]:
                heights[ind + 1] = heights[ind]
                names[ind + 1] = names[ind]
                ind -= 1
            
            names[ind + 1] =  cur_name
            heights[ind + 1] = cur_height
                       
        return names
        