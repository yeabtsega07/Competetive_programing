class UndergroundSystem:

    def __init__(self):
        
        self.checkIns = defaultdict(list)
        self.history = defaultdict(list)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkedIn = self.checkIns[id]
        self.history[(checkedIn[0], stationName)].append(t - checkedIn[1])
        self.checkIns.pop(id)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.history[(startStation, endStation)]) / len(self.history[(startStation, endStation)])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)