#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 15:45:31 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/contiguous-array/
Problem description:
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

"""
# Time: O(n), space: O(n)
class Solution:
    def findMaxLength(self, nums) -> int:
        # length of max subarray
        maxLen = 0
        # cumsums and their positions
        cumsumPositionsMap = {}
        cumsum = 0
        for i in range(len(nums)):
            # add -1 if element's value is 0, else 1
            cumsum += -1 if nums[i] == 0 else 1
            # if cumsum = 0, use element's index + 1 - (elements neutralized each other - equal numbers of
            # zeros and ones)
            if cumsum == 0:
                maxLen = max(maxLen, i+1)
            else:
                # if cumsum is not in map - add it
                if cumsum not in cumsumPositionsMap:
                    cumsumPositionsMap[cumsum] = i
                # else - if cumsum repeated - we have a case where subarray at slice (i,j] or [i,j)
                # is array of equal number of zeros and ones, so update maxLen if this subarr is longest so far
                else:
                    length = i - cumsumPositionsMap[cumsum]
                    maxLen = max(maxLen, length)
        
        return maxLen
    
    
sol = Solution()
# Test 1
print(sol.findMaxLength([0,1,0]))
        

# Test 2
print(sol.findMaxLength([0,1]))

# Test 3
print(sol.findMaxLength([0,1,1,0,1,1,1,0]))


# Test 4
print(sol.findMaxLength([0,0,1,0,0,0,1,1]))