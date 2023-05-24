class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        neg, pos = [], []
        for i, cost in enumerate(costs):
            val = cost[0]-cost[1]
            if val >= 0:
                pos.append([val, i])
            else:
                neg.append([val, i])      
        neg.sort(reverse = True)
        pos.sort()
        res = 0
        ex = set()
        check = []
        if len(neg) == len(pos):

            for cost in costs:
                res += min(cost)
            return res
        elif len(pos) > len(neg):
            k = len(costs)//2 - len(neg)
            i = 0
            while k:
                ex.add(pos[i][1])
                res += costs[pos[i][1]][0]

                k -= 1
                i += 1
            for val in neg:
                res += costs[val[1]][0]
                check.append(costs[val[1]][0])
            for val in pos:
                if val[1] not in ex:
                    res += costs[val[1]][1]
                    check.append(costs[val[1]][1])
        
            return res   
        else:
            k = len(costs)//2 - len(pos)
            i = 0
            while k:
                ex.add(neg[i][1])
                res += costs[neg[i][1]][1]

                k -= 1
                i += 1
            for val in pos:
                res += costs[val[1]][1]

            for val in neg:
                if val[1] not in ex:
                    res += costs[val[1]][0]
     
            return res 
                
                
                
        
        