#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 20:45:49 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/first-bad-version/
Problem description: 
First Bad Version
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 


"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def __init__(self, badVersion):
        self.badVersion = badVersion

        
    def isBadVersion(self, version):
        return version >= self.badVersion
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        # last examined valid version and last examined valid version
        lastValid = lastBad = 0
        # use bisection search - repeadetly half the interval
        while True:
            mid = low + (high-low) // 2
            isBad = self.isBadVersion(mid)
            # version is not  bad
            if not isBad:
                # if the last examined bad version is next number (successor of this number)
                # => mid+1, adn mid is valid, that means
                # that lastBad actually was the first bad version
                if lastBad - 1 == mid:
                    return lastBad
                # last examined version that is valid
                lastValid = mid
                # update lowe bound
                low = mid
            else:
                # if last examined valid version is previous number (predecessor of this number)
                # => mid - 1 and mid is bad version
                # then mid is the first bad version
                if lastValid + 1 == mid:
                    return mid
                # last examined version that is bad
                lastBad = mid
                high = mid
   
                
                

# Test 1
sol = Solution(4)
print(sol.firstBadVersion(5))

# Test 2
sol = Solution(2)
print(sol.firstBadVersion(5))
          

# Test 3
sol = Solution(1)
print(sol.firstBadVersion(5))
          
# Test 4
sol = Solution(3)
print(sol.firstBadVersion(5))
          

# Test 2
sol = Solution(5)
print(sol.firstBadVersion(5))
          