#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:42:37 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/find-pivot-index/
Problem description: 
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
 

Constraints:

The length of nums will be in the range [0, 10000].
Each element nums[i] will be an integer in the range [-1000, 1000].

"""
# Time: O(n), space: O(n)
class Solution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        prefixCumSumArr, suffixCumSumArr = [0] * n, [0] * n 
        cumsum = 0
        for i in range(1, n):
            cumsum += nums[i-1]
            prefixCumSumArr[i] = cumsum
        
        cumsum = 0
        for i in range(n-2, -1, -1):
            cumsum += nums[i+1]
            suffixCumSumArr[i] = cumsum
        for i in range(n):
            if prefixCumSumArr[i] == suffixCumSumArr[i]:
                return i
        return -1
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        prefixCumSumArr, suffixCumSumArr = [0] * n, [0] * n 
        prefixCumsum = suffixCumsum = 0
        for i in range(1, n):
            prefixCumsum += nums[i-1]
            suffixCumsum += nums[n-i]
            prefixCumSumArr[i] = prefixCumsum
            suffixCumSumArr[n-i-1] = suffixCumsum
        
        for i in range(n):
            if prefixCumSumArr[i] == suffixCumSumArr[i]:
                return i

        return -1
    
    def pivotIndex(self, nums):
        totalSum = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            totalSum -= nums[i]
            if totalSum == leftSum:
                return i
            leftSum += nums[i]
            
        return -1
sol = Solution()

# Test 1
nums = [1,7,3,6,5,6]
print(sol.pivotIndex(nums))     

# Test 2
nums = [1,2,3]
print(sol.pivotIndex(nums))     
   
# Test 3
nums = [-1,-1,-1,0,1,1]
print(sol.pivotIndex(nums))     
       
    