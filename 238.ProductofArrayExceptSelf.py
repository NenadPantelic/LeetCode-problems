#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:54:37 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/product-of-array-except-self/
Problem description:
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
# Time: O(n), space: O(1) excluding output array
class Solution:
    def productExceptSelf(self, nums):
        # output[i] should be equal to prefixProduct[i] * suffixProduct[i] where:
        # 1) prefixProduct[i] = product of elements before (left to the element) ith element - excluding ith element
        #    prefixProduct[0] = 1
        #   so in case nums = [1,2,3,4], prefixProduct = [1,1,2,6]
        # 2) suffixProduct[i] = product of elements after (rgiht to the element) ith element - excluding ith element
        #   suffixProduct[-1] = 1
        #   so in case nums = [1,2,3,4], suffixProduct = [24, 12, 4, 1]
        
        cumproduct = 1
        output = [cumproduct]
        n = len(nums)
        # prefix product arr
        for i in range(1, n):
            cumproduct *= nums[i-1]
            output.append(cumproduct)
        # suffix product arr
        prev = 1
        for i in range(n-2, -1, -1):
            val =  nums[i]
            nums[i] = prev * nums[i+1]
            prev = val
        nums[-1] = 1
        # multiply prefixProduct[i] * suffixProduct[i]
        for i in range(n):
            output[i] *= nums[i]
        return output
    
sol = Solution()
# Test 1
print(sol.productExceptSelf([1,2,3,4]))
