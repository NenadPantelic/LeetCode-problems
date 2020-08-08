#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:32:11 2020

@author: nenad
"""



"""
Problem URL: https://leetcode.com/problems/word-break/
Problem description: Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""
# Time:  O(n^2) , space: O(len(wordDict))
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordDict = set(wordDict)
        def wordBreakUtil(s, wordDict):
            if s == "":
                return True
            if s in wordDict:
                return True
            for i in range(1, len(s)): # O(n)
                prefixStr = s[:i]
                suffixStr = s[i:]
                if prefixStr in wordDict:
                    if len(suffixStr) == 0 or suffixStr in wordDict:
                        return True
                    checkSuffixSegmentation = wordBreakUtil(suffixStr, wordDict)
                    if checkSuffixSegmentation:
                        return True
            return False
        return  wordBreakUtil(s, wordDict)
    def wordBreak(self, s:str, wordDict):
        memo = {}
        #wordDict = set(wordDict)
        def wordBreakUtil(s, memo):
            if s == "": return True
            if s in memo: return memo[s]
            memo[s] = False
            for word in wordDict:
                if s[:len(word)] == word and wordBreakUtil(s[len(word):], memo):
                    memo[word] = True
                    return True
            return False
        return wordBreakUtil(s, memo)
        
sol = Solution()

# Test 1
s = "leetcode"; wordDict = ["leetcode", "code"]
print(sol.wordBreak(s, wordDict))


# Test 2
s = "applepenapple"; wordDict = ["apple", "pen"]
print(sol.wordBreak(s, wordDict))
       
# Test 3
s = "catsandog"; wordDict = ["cats", "dog", "sand", "and", "cat"]
print(sol.wordBreak(s, wordDict))

# Test 4
s = "goalspecial"
wordDict = ["go","goal","goals","special"]
print(sol.wordBreak(s, wordDict))


#Test 5
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
print(sol.wordBreak(s, wordDict))