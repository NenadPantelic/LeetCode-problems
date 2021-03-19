#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 13:17:49 2020

@author: nenad
"""


"""
Problem description: Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
"""

Time Complexity:O(NKlogK), where N is the length of strs, and K is the maximum length of a 
string in strs. The outer loop has complexity O(N) as we iterate through each string. 
Then, we sort each string in O(KlogK)time.

Space Complexity: O(NK) - the total information content stored in ans.
"""

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        # mapping: sorted str:all his anagramas
        anagramMap = defaultdict(list)
        for str in strs:
            chars = "".join(sorted(str))
            anagramMap[chars].append(str)
        
        anagramList = []
        for str in anagramMap:
            anagramList.append(anagramMap[str])
        return anagramList
    
    def groupAnagrams(self, strs):
        sortedStrs = ["".join(sorted(string)) for string in strs]
        groupedAnagrams = defaultdict(list)
        for i in range(len(sortedStrs)):
            sortedStr = sortedStrs[i]
            originalStr = strs[i]
            groupedAnagrams[sortedStr].append(originalStr)
        groupedAnagramsAsList = [anagram for anagram in groupedAnagrams.values()]
        return groupedAnagramsAsList
            
    
sol = Solution() 
# Test 1
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol.groupAnagrams(strs))