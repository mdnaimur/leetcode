#  gas station

"""
n gas station 
gas = ith station
next station = i+1

array gas 
array cost 
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
1. cost value is gas index
2. loop cost value  with i
    start_index = cost [i] #3
    start_station_index = gas[start_index] fixed 
    start_station = gas[start_index] fixed 4

    


"""


class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:

        total_tank = 0
        current_tank = 0
        start_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            if current_tank < 0:
                start_station = i+1
                current_tank = 0

        return start_station if total_tank >= 0 else -1


# Example usage
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

sln = Solution()
result = sln.canCompleteCircuit(gas, cost)
print(f"The starting station index is: {result}")
