class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.score = {}
        count, current = defaultdict(int), [-1, - 1]
        for i, time in enumerate(self.times):
            
            count[self.persons[i]] += 1
            if current[1] <= count[self.persons[i]]:
                current = [self.persons[i], count[self.persons[i]] ]
            self.score[time] = current[0]     
        
        
    def q(self, t: int) -> int:
        
        check = bisect_right(self.times, t)
    
        return self.score[self.times[check - 1]]       
        
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)