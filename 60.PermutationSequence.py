#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:10:04 2020

@author: nenad
"""

"""
Problem URL: https://leetcode.com/problems/permutation-sequence/
Problem description:
Permutation Sequence
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

"""

"""
Idea:
Take number by number to form appropriate permutation - 
There are (x-1)! permutations that can be formed with number k as leading number, and x is the length of list of number we can use
Determine what number should be added next to permutation.
Repeat that process until every number is used

"""
from math import factorial, ceil
class Solution:    
    def getPermutation(self, n: int, k: int) -> str:
        permutation = []
        permutationNo = k
        nums = list(range(1,n+1))
        subPermutationNum = factorial(n-1)
        while nums:
            # next number to add to permutation
            permStartNum = nums[ceil(k/subPermutationNum)-1]
            # get new k 
            k = k%subPermutationNum
            permutation.append(str(permStartNum))
            if n > 1: subPermutationNum //= (n-1)
            nums.remove(permStartNum)
            n -= 1
            
        return "".join(permutation)
    
    
    
sol = Solution()

# Test 2
n = 4
k = 2
print(sol.getPermutation(n, k))
    


# Test 2
n = 4
k = 9
print(sol.getPermutation(n, k))

# Test 3
n = 1
k = 1
print(sol.getPermutation(n, k))

# Test 2
n = 4
k = 2
print(sol.getPermutation(n, k))