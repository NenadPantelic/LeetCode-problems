#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 10:35:23 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/majority-element/
Problem description: 
Majority Element
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
# Time: O(n), space: O(n)
from collections import Counter
class Solution:
    def majorityElement(self, nums) -> int:
        counter = Counter(nums)
        threshold = len(nums)//2
        for val in counter:
            if counter[val] > threshold:
                return val
            

sol = Solution()


# Test 1
nums = [3,2,3]
print(sol.majorityElement(nums))

# Test 2
nums = [2,2,1,1,1,2,2]
print(sol.majorityElement(nums))