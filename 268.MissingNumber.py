#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 11:59:28 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/missing-number/
Problem description: 
268. Missing Number
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

class Solution:
    def missingNumber(self, nums) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
    
    def missingNumber(self, nums) -> int:
        sum = 0
        n = len(nums)
        for i in range(n):
            sum += nums[i]
        
        return (n*(n+1)//2) - sum
    
    
    
sol = Solution()

# Test 1
arr = [3,0,1]
print(sol.missingNumber(arr))

# Test 2
arr = [9,6,4,2,3,5,7,0,1]     
print(sol.missingNumber(arr))


# Test 3
arr = [9,6,4,2,3,5,8,7,0,1]     
print(sol.missingNumber(arr))


