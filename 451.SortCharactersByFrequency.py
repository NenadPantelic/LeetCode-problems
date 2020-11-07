#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 12:15:17 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/sort-characters-by-frequency/
Problem description:
Sort Characters By Frequency
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


"""
from heapq import heapify, heappop
from collections import Counter, defaultdict
# Time: O(n), space: O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        # count freqs of chars
        charFreq = Counter(s)
        freqMap = defaultdict(list)
        heap = []
        # put -frequency as key in another map, and number of occurences of that 
		# char is v -> in "tree", this map
        # would be: -2: [ee], -1:[t,r]
        for k,v in charFreq.items():
            freqMap[-v].append(k * v)
        # put keys in heap list
        for k in freqMap:
            heap.append(k)
        # heapify this list
        heapify(heap)
        resList = []
        # pop values from heap (min heap - so values of freq are negative) - join all substrings with the same
        # number of repeating
        while heap:
            freq = heappop(heap)
            resList.append("".join(freqMap[freq]))
            
            
        return "".join(resList)
    
    def frequencySort(self, s):
        counter = Counter(s)
        sortedChars = sorted(counter.items(), key = lambda x:x[1], reverse=True)
        return "".join([item[0] * item[1] for item in sortedChars])
        

sol = Solution()

# Test 1
s = "tree"
print(sol.frequencySort(s))

# Test 2
s = "cccaaa"
print(sol.frequencySort(s))


# Test 2
s = "Aabb"
print(sol.frequencySort(s))