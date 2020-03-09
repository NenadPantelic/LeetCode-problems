#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:42:37 2020

@author: nenad
"""

class Solution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        if n == 0:
            return -1
        cumsum_forward = [None] * n
        #cumsum_backward = [None] * n
        
        cumsum_forward[0] = nums[0]
        #cumsum_backward[-1] = arr[-1]
        for i in range(1, n):
            cumsum_forward[i] = cumsum_forward[i-1] + nums[i]
            #cumsum_backward[-1-i]=cumsum_backward[-i] + arr[-1-i]
        
        # total sum
        total_sum = cumsum_forward[-1]
        #print(total_sum)
        for i in range(n):
            if cumsum_forward[i] == total_sum:
                return i
            total_sum -= nums[i]
    
        return -1
        

    