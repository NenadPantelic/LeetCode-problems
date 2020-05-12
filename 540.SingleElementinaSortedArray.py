#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 11:25:16 2020

@author: nenad
"""



"""
Problem URL: 
Problem description: 
Single Element in a Sorted Array
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.

"""
# Good explanation: https://leetcode.com/problems/single-element-in-a-sorted-array/discuss/627921/Java-or-C%2B%2B-or-Python3-or-Easy-explanation-or-O(logn)-or-O(1)
# Time: O(log(n)), space: O(1)
class Solution:
    def singleNonDuplicate(self, nums) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left)//2
            # x ^ 1
            # if x is even -> result is x+1
            # else -> results is x-1
            if nums[mid] == nums[mid^1]:
                left = mid+1
            else:
                right = mid
        return nums[left]
    
    
sol = Solution()

# Test 1
nums = [1,1,2,3,3,4,4,8,8]
print(sol.singleNonDuplicate(nums))

# Test 2
nums = [3,3,7,7,10,11,11]
print(sol.singleNonDuplicate(nums))