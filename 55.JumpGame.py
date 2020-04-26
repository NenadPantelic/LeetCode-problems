#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:54:28 2020

@author: nenad
"""



"""
Problem URL: https://leetcode.com/problems/jump-game/
Problem description: 
Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.

"""
# Note: ith element of jumpArray shows if we can come to ith position of the array.
# Time: O(n), space: O(n)
class Solution:
    def canJump(self, nums) -> bool:
        n = len(nums)
        # trivial case - we're alredy at last index
        if n == 1:
            return True
        jumpArray = [False] * n
       
        for i in range(n-1):
            if i == 0:
                # since nums[i] == 0, we stop at this position and we cannot go further
                if nums[i] == 0:
                    return False

            # we cannot get here since we cannot get into previous position
            elif not jumpArray[i-1]:
                return False
            # if i > 0 (there are previous elements), determine whether is better to use
            # current element's jump value or use previous one (decremented by 1 -> we spent that jump
            # coming into this position from the previous one
            elif i > 0:
                nums[i] = max(nums[i], nums[i-1] - 1) # take longer range
                if nums[i] == 0:
                    # if the value is still zero - return False (we will stop here)
                    #e.g. .... 1 0 ... case
                    return False
            # we can get here - set True
            jumpArray[i] = True
        # if penultimate jump value is greater than zero, we can jump from penultimate to last position
        if nums[-2] > 0:
            jumpArray[-1] = True
        return jumpArray[-1]

    
sol = Solution()
# Test 1
nums = [2,3,1,1,4]
print(sol.canJump(nums))

# Test 2
nums = [3,2,1,0,4]
print(sol.canJump(nums))
# Test 3
nums = [0,2,3]
print(sol.canJump(nums))

# Test 4
nums = [0]
print(sol.canJump(nums))

# Test 4
nums = [2,0, 0]
print(sol.canJump(nums))
    