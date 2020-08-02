#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:05:44 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/kth-largest-element-in-an-array/
Problem description: 
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

"""

from heapq import heapify, heappop, heappushpop
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
            heap = nums[:k]
            heapify(heap)
            min_el = heap[0]
            for i in range(k, len(nums)):
                if min_el < nums[i]:
                    heappushpop(heap, nums[i])
                    min_el = heap[0]
  
            return heappop(heap)
        
sol = Solution()
arr = [3,2,1,5,6,4]; k = 2
print(sol.findKthLargest(arr, k))

arr = [3,2,3,1,2,4,5,5,6]; k = 4
print(sol.findKthLargest(arr, k))
        
        
    