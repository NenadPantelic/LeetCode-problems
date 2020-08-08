#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:32:05 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/rotate-array/
Problem description: 
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
"""
class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        if k == 0:
            return
        newStart = len(nums) - k
        auxArray  = [val for val in nums[newStart:]] # aux-space -> O(k) 
        for i in range(newStart-1, -1, -1):
            nums[i+k] = nums[i]
        nums[:k] = auxArray
    
    
            
    # Great solution    
    def rotate(self, nums, k):
        k = k % len(nums)
        if k == 0:
            return
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start, end = start + 1, end - 1
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, len(nums)-1)
        
        
sol = Solution()

# Test 1
nums = [1,2,3,4,5,6,7]; k = 3
sol.rotate(nums, k)
print(nums)


# Test 2
nums = [-1,-100,3,99]; k = 2
sol.rotate(nums, k)
print(nums)
