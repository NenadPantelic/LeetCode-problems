#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 15:40:39 2020

@author: nenad
"""


"""
https://leetcode.com/problems/add-strings/
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1)
        n = len(num2)
        minLen = min(m, n)
        i = 0
        numSum = 0
        digitNum1, digitNum2 = 0, 0
        carry = 0
        asciiZero = ord('0')
        numSum = []
        while i  < minLen:
            digitNum1 = ord(num1[m-i-1]) - asciiZero
            digitNum2 = ord(num2[n-i-1]) - asciiZero
            total = digitNum1 + digitNum2 + carry
            numSum.append(str(total%10))
            carry = total // 10
            i += 1
        
            
        while i < m:
            total = ord(num1[m-i-1]) - asciiZero + carry
            numSum.append(str(total%10))
            carry = total // 10
            i += 1
        
        while i < n:
            total = ord(num2[n-i-1]) - asciiZero + carry
            numSum.append(str(total%10))
            carry = total // 10
            i += 1
        if carry > 0:
            numSum.append(str(carry))
        numSum.reverse()
        return "".join(numSum)
            
num1 = "123"
num2 = "4281"
print(Solution().addStrings(num1, num2))


num1 = "1"
num2 = "9999"
print(Solution().addStrings(num1, num2))