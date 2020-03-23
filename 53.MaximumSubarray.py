#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:10:20 2020

@author: nenad
"""


class Solution:
    # Kadane's algorithm
    def maxSubArray(self, nums):
        maxSoFar = 0
        maxGeneral = 0
        for val in nums:
            maxSoFar += val
            if maxSoFar < 0:
                maxSoFar = 0
            if maxGeneral < maxSoFar:
                maxGeneral = maxSoFar
        
        if maxGeneral == 0:
            # all values are negative - use the greatest one as subarray
            maxGeneral = max(nums)
        return maxGeneral
    
s = Solution()
arr = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(arr))