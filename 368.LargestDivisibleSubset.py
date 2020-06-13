#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:29:46 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/largest-divisible-subset/
Problem description: 
 Largest Divisible Subset
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)
Example 2:

Input: [1,2,4,8]
Output: [1,2,4,8]

"""

# Time: O(n^2), space: O(n)
class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        maxInd = 0
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j] + 1
                        prev[i] = j
            if dp[maxInd] < dp[i]:
                maxInd = i
        k = maxInd
        res = []
        while k >= 0:
            res.append(nums[k])
            k = prev[k]
        return res[::-1]
sol = Solution()
# Test 1
nums = [1,2,3]
print(sol.largestDivisibleSubset(nums))

# Test 2
nums = [1,2,4,8]
print(sol.largestDivisibleSubset(nums))