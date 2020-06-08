#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 20:53:42 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/power-of-two/
Problem description:
Power of Two
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false

"""
# Time: O(logn), space: O(1)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        val = 1
        while val < n:
            val <<= 1
        return val == n

sol = Solution()

# Test 1
n = 1
print(sol.isPowerOfTwo(n))


# Test 2
n = 16
print(sol.isPowerOfTwo(n))
            
# Test 3
n = 218
print(sol.isPowerOfTwo(n))