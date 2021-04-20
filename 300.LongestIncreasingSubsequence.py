#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 13:09:32 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/longest-increasing-subsequence/
Problem description: 
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""
from bisect import bisect_left
class Solution:
    # Time: O(n^2), space: O(n)
    def lengthOfLIS(self, nums):
        n = len(nums)
        lisLen = 1
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(0, n-1):
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
                    lisLen = max(lisLen, dp[j])
        return lisLen
    
    # check this    
    def lengthOfLIS(self, nums):
        ans = []
        for val in nums:
            pos = bisect_left(nums, val)
            if pos == len(ans):
                ans.append(val)
            else:
                ans[pos] = val
        return len(ans)
        
    def lengthOfLIS(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [1] * n
        maxx = 1
        for i in range(1, n):
            for j in range(i):
                if arr[j] < arr[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            maxx = max(maxx, dp[i])
        return maxx
    

    
sol = Solution()
# Test 1
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))

# Test 2
print(sol.lengthOfLIS([4,10,4,3,8,9]))
        
# Test 3
print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))
