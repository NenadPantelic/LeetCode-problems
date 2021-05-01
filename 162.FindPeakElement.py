#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:17:36 2021

@author: nenad
"""


"""
URL: https://leetcode.com/problems/find-peak-element/
Description: 
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
 

Follow up: Could you implement a solution with logarithmic complexity?
"""
from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return n-1
        for i in range(1, n-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i
            
    
    def findPeakElement(self, nums: List[int]) -> int:
        def binPeak(nums, low, high):
            if low > high:
                return -1
            mid = low + (high - low) // 2
            left = nums[mid-1] if mid >= 1 else float("-inf")
            right = nums[mid+1] if mid < len(nums)-1 else float("-inf")
            if left < nums[mid] and nums[mid] > right:
                return mid
            leftPeak = binPeak(nums, low, mid-1)
            if leftPeak != -1:
                return leftPeak
            
            rightPeak = binPeak(nums, mid+1, high)
            if rightPeak != -1:
                return rightPeak
            return -1
        return binPeak(nums, 0, len(nums)-1)
            
            

            
        