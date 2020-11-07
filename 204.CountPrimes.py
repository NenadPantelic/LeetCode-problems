#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:46:57 2020

@author: nenad
"""

"""
https://leetcode.com/problems/count-primes/
"""
class Solution:
    def countPrimes(self, n: int) -> int:
        allNums = [True] * (n-2)
        numOfPrimes = max(n-2, 0)
        if numOfPrimes == 0:
            return 0
        for denum in range(2, n):
            if allNums[denum-2] == False:
                continue
            value = denum * denum
            while value < n:
                if allNums[value-2]:
                    allNums[value-2] = False
                    numOfPrimes -= 1
                value += denum
        return numOfPrimes
    
 
# Test 1
n = 10
print(Solution().countPrimes(n))


# Test 2
n = 0
print(Solution().countPrimes(n))
            
        

# Test 3
n = 15
print(Solution().countPrimes(n))     


# Test 4
n = 2
print(Solution().countPrimes(n))
            
        