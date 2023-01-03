class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        track = defaultdict(int)
        
        for i in range(len(grid)):
            track["rZero"+str(i)] = grid[i].count(0)
            track["rOne"+str(i)] = grid[i].count(1)
        
        ind = 0
        for list_ in zip(*grid):
            track["cZero"+str(ind)] = list_.count(0)
            track["cOne"+str(ind)] = list_.count(1)
            ind += 1
        # print(track)
        for i in range(len(grid)):
            cur = []
            for j in range(len(grid[0])):
                diff = track["rOne"+str(i)] + track["cOne"+str(j)] - track["rZero"+str(i)] - track["cZero"+str(j)]
                cur.append(diff)
            grid[i] = cur
        
        return grid
                
            


        