#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 13:51:45 2020

@author: nenad
"""

# Time and space: O(n!)
"""
Problem URL: https://leetcode.com/problems/permutations/
Problem description: 
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]
        perms = self.permute(nums[1:])
        result = []
        for perm in perms:
            for i in range(len(perm)+1):
                result.append(perm[:i] + [nums[0]] + perm[i:])
            
        return result
print(Solution().permute([1,2,3]))
        