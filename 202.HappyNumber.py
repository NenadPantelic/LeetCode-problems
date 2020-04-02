#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:43:11 2020

@author: nenad
"""



"""

Problem URL: https://leetcode.com/problems/happy-number/
Problem description: Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Input: 19
Output: true
Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""

class Solution:
    def isHappy(self, n: int, checkedNumbers = set()) -> bool:
        sum = 0
        # O(log_10(n))
        while n > 0:
            sum += (n%10) ** 2
            n //= 10
        # happy number condition 
        if sum == 1:
            checkedNumbers.clear()
            return True
        # if number is already checked, we are entering cycle
        if sum in checkedNumbers:
            checkedNumbers.clear()
            return False
        # add new number to set
        checkedNumbers.add(sum)
        # check new sum
        return self.isHappy(sum, checkedNumbers)
    
    def isHappy(self, n: int) -> bool:
        checkedNumbers = set()
        
        while True:
            sum = 0
            # O(log_10(n))
            while n > 0:
                sum += (n%10) ** 2
                n //= 10
            # happy number condition 
            if sum == 1:
                #checkedNumbers.clear()
                return True
            # if number is already checked, we are entering cycle
            if sum in checkedNumbers:
                #checkedNumbers.clear()
                return False
            # add new number to set
            checkedNumbers.add(sum)
            # check new sum
            n = sum

    
sol = Solution()    
# Test 1
n = 19
print(sol.isHappy(n))


# Test 2
n = 8
print(sol.isHappy(n))

# Test 3
n = 141
print(sol.isHappy(n))

# Test 4
n = 7
print(sol.isHappy(n))

# Test 5
n = 13
print(sol.isHappy(n))