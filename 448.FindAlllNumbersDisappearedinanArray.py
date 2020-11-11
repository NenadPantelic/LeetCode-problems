#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 18:19:17 2020

@author: nenad
"""


"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""
# Time: O(n), space: O(n)
class Solution:
    def findDisappearedNumbers(self, nums):
        disappearedNums = []
        for val in nums:
            index = abs(val) - 1
            if nums[index] >= 0:
                nums[index] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                disappearedNums.append(i+1)
        return disappearedNums
    
    def findDisappearedNumbers(self, nums):
        return list(set(range(1, len(nums) + 1)).difference(set(nums)))
    
# Test 1
arr = [4,3,2,7,8,2,3,1]
print(Solution().findDisappearedNumbers(arr))
        