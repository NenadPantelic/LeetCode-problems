#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:53:56 2020

@author: nenad
"""

"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.


"""
class Solution:
    def removeElement(self, nums, val: int) -> int:
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.pop(i)
        return len(nums)
    # Two pointers runner method
    # O(n)
    def removeElement(self, nums, val: int) -> int:
        # slow pointer
        i = 0
        # fast runner
        j = 0
        n = len(nums)
        while j < n:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        # new length of the array
        return i
    

sol = Solution()
    
    
# Test 1
nums = [3,2,2,3]; val = 3
print(sol.removeElement(nums, val))
print(nums)


# Test 2
nums = [0,1,2,2,3,0,4,2]; val = 2
print(sol.removeElement(nums, val))
print(nums)        