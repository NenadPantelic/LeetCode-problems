#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:20:22 2020

@author: nenad
"""

# O(log10_(n))
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative nums are not palindromes
        if x < 0:
            return False
        digits = []
        # O(log_10(n)) - get digits 
        while x:
            digits.append(x % 10)
            x //= 10
            
        digits_no = len(digits)
        for i in range(digits_no//2):
            # digits at symetrical positions are not the same
            if digits[i] != digits[digits_no-i-1]:
                return False
            
        # otherwise
        return True
    
    def isPalindrome(self, x: int) -> bool:
        # negative nums are not palindromes, as well as nums which finish with zero
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        reverted_num = 0
        # O(log_10(n)) - get digits 
        while x > reverted_num:
            # digit where last element
            last_digit = x % 10
            reverted_num = reverted_num * 10 + last_digit
            x //= 10
        return x == reverted_num or x == reverted_num // 10

s = Solution()
# Test 1
num = 121
print(s.isPalindrome(num))    

# Test 2
num = -121
print(s.isPalindrome(num))


# Test 3
num = 10
print(s.isPalindrome(num))

# Test 4
num = 0
print(s.isPalindrome(num))

# Test 5
num = 1221
print(s.isPalindrome(num)) 