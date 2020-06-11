#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 22:31:16 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/sort-colors/
Problem description: 
Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""
# Time: O(n), space: O(1)
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countList = [0] * 3
        for val in nums:
            countList[val] += 1
        offset = 0
        for i in range (len(countList)):
            val = countList[i]
            for j in range(val):
                nums[offset + j] = i
            offset += val
            
sol = Solution()

# Test 1
nums = [2,0,2,1,1,0]
sol.sortColors(nums)
print(nums)
        