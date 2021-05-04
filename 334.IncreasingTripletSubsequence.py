#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 12:48:39 2021

@author: nenad
"""
"""
URL: https://leetcode.com/problems/increasing-triplet-subsequence/
Description:
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?
"""
from typing import List
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False
        
        small = big = float('inf')
        threshold = float('inf')
        for num in nums:
            if num < small: 
                small = num
            elif num < big and num > small:
                big = num
            if num > big:
                return True
            
        return False