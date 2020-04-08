#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:47:02 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/non-decreasing-array/
Problem description: 
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

"""

# Time: O(n), space:O(1)
class Solution:
    def checkPossibility(self, nums) -> bool:
         # flag that tells if at most one element is modified
        modified = False
        prev = None
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                # one element is already modified
                if modified:
                    return False
                # otherwise - set flag as True - element is modified
                modified = True
                # check what to do - to set nums[i+1] = nums or nums[i] = nums[i+1]
                # based on nums[i-1]
                if prev and prev > nums[i+1]:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
            prev = nums[i]
                
        return True
    
sol = Solution()

# Test 1
print(sol.checkPossibility([4,2,3]))

# Test 2
print(sol.checkPossibility([4,2,1]))

# Test 3
print(sol.checkPossibility([3,4,2,3]))