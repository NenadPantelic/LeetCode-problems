#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 22:18:56 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/plus-one/
Problem description: 
Plus One
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""
# Time: O(n), space: O(1)
class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            val = digits[i] + carry
            carry = val // 10
            digits[i] = val % 10
            if carry == 0:
                break
        if carry == 1:
            digits.insert(0, 1)
        return digits

sol = Solution()
# Test 1
digits = [1,2,3]
print(sol.plusOne(digits))
                
# Test 2
digits = [1,2,9,9]
print(sol.plusOne(digits))        


# Test 3
digits = [9,9,9,9]
print(sol.plusOne(digits))        