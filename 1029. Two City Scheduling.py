class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        N = len(costs)/2
        sorted_costs = sorted(costs, key=lambda x: abs(x[0] - x[1]))
        
        return sum([x[0] for x in sorted_costs[:int(N)]]) + sum([x[1] for x in sorted_costs[int(N):]])
