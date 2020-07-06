#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 21:59:05 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/hamming-distance/
Problem description: 
Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        hammingDiff = x ^ y
        return bin(hammingDiff)[2:].count('1')
    
sol = Solution()

# Test 1
x = 1; y = 4
print(sol.hammingDistance(x, y))