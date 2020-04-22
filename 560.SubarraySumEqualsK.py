#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 13:57:01 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/subarray-sum-equals-k/
Problem description: 
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

# General idea:

# store cumsum of elements in array
# sum(i,j) = sum(0,j) - sum(0,i) -> sum of elements between ith and jth index = [i,j-1]
# check if that sum is equal to k or equivalent => if sum(0,i) = sum(0, j) - k
# Time: O(n), space: O(n)
from collections import defaultdict, Counter
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        # counter of cumulative sums
        sumMap = defaultdict(list)
        positionSum = {}
        counter = 0
        cumsum = 0
        # make cumsum and add indexes of those sums to sumMap
        for i in range(len(nums)):
            cumsum += nums[i]
            sumMap[cumsum].append(i)
            positionSum[i] = cumsum
        for i in range(len(nums)):
            val = positionSum[i]
            complement = k + val - nums[i]
            if complement in sumMap:
                counter += sum([1 if ind >= i else 0 for ind in sumMap[complement]])
        return counter
    
    def subarraySum(self, nums, k: int) -> int:
        # counter of cumulative sums
        sumCounter = Counter()
        # result
        counter = 0
        cumsum = 0
        # add zero to sumCounter
        sumCounter[0] = 1
        for i in range(len(nums)):
            cumsum += nums[i]
            # search for complement
            complement = cumsum - k
            counter += sumCounter.get(complement, 0)
            # add cumsum to counter map
            sumCounter[cumsum] += 1
            
        return counter
    
    

    
sol = Solution()    
# Test 1
nums = [1,1,1]
k = 2
print(sol.subarraySum(nums, k))
# Test 2
nums = [1,3,4,2,5,7]
k = 7
print(sol.subarraySum(nums, k))

# Test 3
nums = [1]
k = 0
print(sol.subarraySum(nums, k))


# Test 4
nums = [-1, -1 ,1]
k = 0
print(sol.subarraySum(nums, k))