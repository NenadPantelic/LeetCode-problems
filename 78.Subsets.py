#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 12:39:03 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/subsets/
Problem description: 78. Subsets
Medium

3977

85

Add to List

Share
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]


"""
# Time: O(2^n * n), space: O(2^n)
class Solution:
    def subsets(self, nums):
        result = []
        for i in range(2 ** len(nums)):
            subset = []
            j = i
            index = 0
            while j > 0:
                if j & 1 == 1:
                    subset.append(nums[index])
                j >>= 1
                index += 1
            result.append(subset)
        return result
    def subsets(self, nums):
        def generateSubsets(i, subsets, subset = []):
            if i == len(nums):
                subsets.append(subset)
                return
            generateSubsets(i+1, subsets, subset + [nums[i]])
            generateSubsets(i+1, subsets, subset)
        subsets = []
        generateSubsets(0, subsets, [])
        return subsets
    
                
            
    
sol = Solution()

# Test 1
print(sol.subsets([1,2,3]))
            


