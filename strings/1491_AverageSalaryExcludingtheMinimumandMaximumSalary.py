class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        sum = 0
        for i in salary:
            sum += i
        return sum/len(salary)