#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 23:30:50 2020

@author: nenad
"""

"""
Problem URL: https://leetcode.com/problems/random-pick-with-weight/
Problem description: 
Random Pick with Weight

Solution
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

"""
from random import randint
class Solution:
    def __init__(self, w):
        self.buckets = []
        self._populateSpace(w)
    def _populateSpace(self, w):
        cumsum = 0
        for val in w:
            prev = cumsum
            cumsum += val
            self.buckets.append([prev, cumsum])
    def _binSearch(self, arr, low, high, val):
        if low > high:
            return -1
        mid = low + (high-low)//2
        left, right = arr[mid]
        if left < val <= right:
            return mid
        if val <= left:
            return self._binSearch(arr, low, mid-1, val)
        else:
            return self._binSearch(arr, mid+1, high, val)

    def pickIndex(self) -> int:
        cumsum = self.buckets[-1][-1]
        val = randint(1, cumsum)
        # do this task again with bisect functions from bisect lib
        return self._binSearch(self.buckets, 0, len(self.buckets)-1, val)
                
# Test 1    
w = [1]    
sol = Solution(w)
print(sol.pickIndex())

# Test 2
w = [1,3]    
sol = Solution(w)
for i in range(5):
    print(sol.pickIndex())