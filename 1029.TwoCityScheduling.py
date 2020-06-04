#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:53:01 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/two-city-scheduling/
Problem description: 
Two City Scheduling
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

Example 1:

Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation: 
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
 

Note:

1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000


"""

# Time and space: O(n)
"""
Idea:
1) for every cost element, calculate diff = costs[i][1] - costs[i][0]
2) store these values in some arr, and also store positions i
3) sort descending  by diff - we make greedy decisions ---> NOTE: we can sort it in place, without using additional space
# sort original array by costs[i][0] - costs[i][1]
 costs[i][1] - costs[i][0] is measure if it is better to go in city A or B, large values means
it is better to go to city A, because flying cost to B is much greater than flying cost to A,
and vice versa, if this 
value is small (negative presumably), it is better to go to city B instead of A. 
4) first half will go to city A, and the other one to city B 
"""
class Solution:
    def twoCitySchedCost(self, costs) -> int:
        valueDiffs = []
        n = len(costs)
        for i in range(n):
            valueDiffs.append([costs[i][1] - costs[i][0], i])
        
        valueDiffs.sort(key=lambda x:x[0], reverse=True)
        totalCost = sum([costs[val[1]][0] for val in valueDiffs[:n//2]]) + \
                    sum([costs[val[1]][1] for val in valueDiffs[n//2:]])
        
        return totalCost

sol = Solution()
                              
# Test 1
print(sol.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))

# Test 2
print(sol.twoCitySchedCost([[10,10],[20,20],[30,1000],[40,2000]]))