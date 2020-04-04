#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 13:30:26 2020

@author: nenad
"""



"""
Problem URL: https://leetcode.com/problems/move-zeroes/
Problem description: 
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.

"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        firstPointer = 0
        secondPointer = 1
        while firstPointer < len(nums):
            # if secondPointer is placed before the firstPointer, move secondPointer to position next to firstPointer
            # case when there is a sequence of nonzero numbers
            if secondPointer <= firstPointer:
                secondPointer = firstPointer + 1
            # zero element found -> shifting required
            if nums[firstPointer] == 0:
                # search for first nonzero element via secondPointer
                while secondPointer < len(nums) and not nums[secondPointer]:
                        secondPointer += 1
                # we found nonzero element - swap them
                if secondPointer < len(nums):
                    nums[firstPointer], nums[secondPointer] = nums[secondPointer], nums[firstPointer] 
                    # increment secondPointer
                    secondPointer += 1
                else:
                    # we shifted all nonzero elements
                    break
            # increment firstPointer
            firstPointer += 1
    
sol = Solution()

# Test 1
nums = [0,1,0,3,12]
sol.moveZeroes(nums) 
print(nums)      


# Test 2
nums = [4,2,4,0,0,3,0,5,1,0]
sol.moveZeroes(nums) 
print(nums)      

