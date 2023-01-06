class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        heapify(costs)
        count = 0
        while coins and costs:
            # print(coins)
            candy = heappop(costs)
            coins -= candy
            if coins < 0:
                break
            count += 1
        return count    
        