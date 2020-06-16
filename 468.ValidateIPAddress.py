#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 15:27:26 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/validate-ip-address/
Problem description: 
Validate IP Address
Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;

Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.

IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).

However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.

Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.

Note: You may assume there is no extra space or special characters in the input string.

Example 1:
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".
Example 2:
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".
Example 3:
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.

"""

class Solution:
    def validIPAddress(self, IP: str) -> str:
        IP = IP.lower()
        ipParts = IP.split(".")
        if len(ipParts) == 4:
            return "IPv4" if all([not (len(part) > 1 and part[0] == "0") and("0" <= part <= "255" and len(part) <= 3)
                                  for part in ipParts]) else "Neither"
        ipParts = IP.split(":")
        if len(ipParts) ==8:
            return "IPv6" if all([
                         "0" <= part <= "ffff" and len(part) <= 4
                        for part in ipParts]) else "Neither"
        return "Neither"
            
            
    
sol = Solution()
# Test 1
ip = "172.16.254.1"
print(sol.validIPAddress(ip))


# Test 2
ip = "2001:0db8:85a3:0:0:8A2E:0370:7334"
print(sol.validIPAddress(ip))

# Test 3
ip = "256.256.256.256"
print(sol.validIPAddress(ip))

# Test 4
ip = "2001:0db8:85a3:00000:0:8A2E:0370:7334"
print(sol.validIPAddress(ip))

# Test 5
ip = "1111111"
print(sol.validIPAddress(ip))


# Test 6
ip = "192.01.01.0"
print(sol.validIPAddress(ip))

# Test 7
ip = "1.0.1"
print(sol.validIPAddress(ip))