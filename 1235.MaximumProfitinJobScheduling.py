#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 17:36:56 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
Problem description: 
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime , endTime and profit arrays, you need to output the maximum profit you can take such that there are no 2 jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:




Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
 

Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
1 <= startTime[i] < endTime[i] <= 10^9
1 <= profit[i] <= 10^4
"""
# Time: O(n^2)
class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        n = len(startTime)
        jobData  = []
        for i in range(n):
            jobData.append((startTime[i], endTime[i], profit[i]))
        jobData.sort(key=lambda x:x[0])
        dp = [job[2] for job in jobData]
        for i in range(n):
            for j in range(i+1, n):
                if jobData[i][1] <= jobData[j][0]:
                    dp[j] = max(dp[j], jobData[j][2] + dp[i])
        return max(dp)
    
sol = Solution()

# Test 1
startTime = [1,2,3,3]; endTime = [3,4,5,6]; profit = [50,10,40,70]
print(sol.jobScheduling(startTime, endTime, profit))
        
# Test 2
startTime = [1,2,3,4,6]; endTime = [3,5,10,6,9]; profit = [20,20,100,70,60]        
print(sol.jobScheduling(startTime, endTime, profit))

# Test 3
startTime = [1,1,1]; endTime = [2,3,4]; profit = [5,6,4]
print(sol.jobScheduling(startTime, endTime, profit))

# Test 4
startTime = [6,15,7,11,1,3,16,2]
endTime = [19,18,19,16,10,8,19,8]
profit = [2,9,1,19,5,7,3,19]
print(sol.jobScheduling(startTime, endTime, profit))
