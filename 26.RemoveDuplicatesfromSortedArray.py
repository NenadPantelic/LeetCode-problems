#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 21:15:12 2020

@author: nenad
"""


"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

"""
class Solution:
    # Runner method
    def removeDuplicates(self, nums) -> int:
        # slow pointer
        i = 0
        # fast runner
        j = 0
        n = len(nums)
        # O(n)
        while j < n:
            nums[i] = nums[j]
            i += 1
            val = nums[j]
            j += 1
            while j < n and val == nums[j]:
                j += 1
            
        # new length of the array
        return i
    
    
    # Runner method - version 2
    def removeDuplicates(self, nums) -> int:
        # slow pointer
        i = 0
        # fast runner
        j = 0
        n = len(nums)
        # O(n)
        for j in range(1, n):
            if nums[i] != nums[j]:
                # save nums[i] and write nums[j] to nums[i+1]
                i += 1
                nums[i] = nums[j]
            
        # new length of the array
        return i+1
    
    
sol = Solution()
    
    
# Test 1
nums = [1,1,2]
print(sol.removeDuplicates(nums))
print(nums)


# Test 2
nums = [0,0,1,1,1,2,2,3,3,4]
print(sol.removeDuplicates(nums))
print(nums)        