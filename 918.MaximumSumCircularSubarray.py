#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:28:55 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/maximum-sum-circular-subarray/solution/
Problem description: 
Maximum Sum Circular Subarray
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.  (Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.  (Formally, for a subarray C[i], C[i+1], ..., C[j], there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)

 

Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1
 

Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000
"""
# Time: O(n), space: O(1)
class Solution:
    def kadane(self, arr):
        cur = ans = float("-inf")
        for val in arr:
            cur = val + max(cur, 0)
            ans = max(ans, cur)
        return ans
    
    def minKadane(self, arr):
        cur = ans = float("inf")
        for val in arr:
            cur = val + min(cur, 0)
            ans = min(ans, cur)
        return ans
    
    def maxSubarraySumCircular(self, A) -> int:
        arrSum = sum(A) # O(n)
        ans1 = self.kadane(A)
        ans2 = arrSum - self.minKadane(A[1:])
        ans3 = arrSum - self.minKadane(A[:-1])
        return max(ans1, ans2, ans3)
    
sol = Solution()

# Test 1
arr = [1,-2,3,-2]
print(sol.maxSubarraySumCircular(arr))
# Test 2
arr = [5,-3,5]
print(sol.maxSubarraySumCircular(arr))

# Test 3
arr = [3,-1,2,-1]
print(sol.maxSubarraySumCircular(arr))

# Test 4
arr = [3,-2,2,-3]
print(sol.maxSubarraySumCircular(arr))

# Test 5
arr = [-2,-3,-1]
print(sol.maxSubarraySumCircular(arr))