#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 22:44:02 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/h-index-ii/
Problem description: 
H-Index II
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note:

If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:

This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
Could you solve it in logarithmic time complexity?
"""
# Time: O(log(n)), space: O(1)
class Solution:
    def hIndex(self, citations) -> int:
        n = len(citations)
        # if n == 0:
        #     return 0
        if n == 1:
            return int(citations[0] > 0)
        left = 0
        right = n-1
        res = 0
        while left <= right:
            mid = left + (right-left)//2
            hInd = n - mid
            
            if hInd <= citations[mid]:
                right = mid-1
                res = hInd
            else:
                left = mid+1
                
        return res
            
            
sol = Solution()        

# Test 1
citations = [0,1,3,5,6]
print(sol.hIndex(citations))

# Test 2
citations = [1,2,5,6,7,8,9]
print(sol.hIndex(citations))

# Test 3
citations = [1,2, 4, 5,6,7]
print(sol.hIndex(citations))

# Test 4
citations = [0]
print(sol.hIndex(citations))

# Test 4
citations = [100]
print(sol.hIndex(citations))

# Test 5
citations = [1,2]
print(sol.hIndex(citations))


# Test 6
citations = [0,0]
print(sol.hIndex(citations))