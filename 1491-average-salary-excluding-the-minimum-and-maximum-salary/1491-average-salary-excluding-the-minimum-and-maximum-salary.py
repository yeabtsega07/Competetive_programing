class Solution:
    def average(self, salary: List[int]) -> float:
        max_ = max(salary)
        min_ = min(salary)
        sum_ = sum(salary)
        
        return (sum_ - (min_ + max_)) / (len(salary) - 2)
        