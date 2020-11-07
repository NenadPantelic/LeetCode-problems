#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:39:30 2020

@author: nenad
"""


"""
https://leetcode.com/problems/sort-array-by-parity/
"""
class Solution:
    def sortArrayByParity(self, A):
        A.sort(key=lambda x:x % 2 == 0, reverse=True)
        return A
    
print(Solution().sortArrayByParity([3,1,2,4]))
        