#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:44:19 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/single-number/

Problem description: Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

from collections import Counter

class Solution:
    # Time: O(n); space: O(n)
    def singleNumber(self, nums) -> int:
        counter = Counter()
        for val in nums:
            counter[val] += 1
        
        for val in counter:
            if counter[val] == 1:
                return val
    # Time: O(n); space: O(1)        
    def singleNumber(self, nums):
        el = nums[0]
        # x xor x = 0 (if values are the same, xor gives zero)
        for i in range(1, len(nums)):
            el = el ^ nums[i]
        return el
            

sol = Solution()
# Test 1
nums = [2,2,1]
print(sol.singleNumber(nums))

# Test 2
nums = [4,1,2,1,2]
print(sol.singleNumber(nums))