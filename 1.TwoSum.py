#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 18:09:01 2020

@author: nenad
"""
"""
Given an numsay of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

from collections import defaultdict

class Solution:
    def twoSum(self, nums, target: int):
        indices = defaultdict(list)
        n = len(nums)
        # O(n)
        for i in range(n):
            val = nums[i]
            ind = indices.get(target-val, None)
            if ind:
                return [ind[0], i]
            indices[val].append(i)

            
            
    
            
        
# Test 1
arr = [2,7,11,15]
s = Solution()
print(s.twoSum(arr, 9))

# Test 2
arr = [3,2,4]
#s = Solution()
print(s.twoSum(arr, 6))

# Test 3
arr = [3,3]
#s = Solution()
print(s.twoSum(arr, 6))


# Test 4
arr = [0,3,-3,4,-1]
print(s.twoSum(arr, -1))
