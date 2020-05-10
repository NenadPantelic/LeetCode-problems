#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 14:17:54 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/find-the-town-judge/
Problem description: 
Find the Town Judge
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3


Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= t
"""
from collections import defaultdict
# Time: O(len(trust)), space: O(N)
class Solution:
    def findJudge(self, N: int, trust) -> int:
      # trivial case
      if N == 1 and len(trust) == 0:
          return 1
      # all elements from 1 to N are candidates for the judge
      judgeSet = set(list(range(1,N+1)))
      nonJudges = set()
      # map of those who are loved
      lovedOnes = defaultdict(set)
      for a, b in trust:
          # a cannot be judge - a loves someone
          if a in judgeSet:
              # a is non-judge person
              judgeSet.remove(a)
          # a is non-judge person
          nonJudges.add(a)
          # b is loved by a
          lovedOnes[b].add(a)
      # there must be only one candidate, there is no judge
      if len(judgeSet) != 1:
          return -1
      judgeCandidate = judgeSet.pop()
      fansOfJudgeCandidate = lovedOnes.get(judgeCandidate, None)
      # judge candidate is not loved at all
      if fansOfJudgeCandidate is None:
          return -1
      # all non-judge persons love judge candidate - that is the judge ->
      # complete intersection of nonJudges and fansOfJudge candidate sets = all persons love judge candidate
      if nonJudges.difference(fansOfJudgeCandidate) == set():
          return judgeCandidate
      return -1
  
    
sol = Solution()

# Test 1

N = 2; trust = [[1,2]]
print(sol.findJudge(N, trust))

# Test 2
N = 3; trust = [[1,3],[2,3]]
print(sol.findJudge(N, trust))
# Test 3
N = 3; trust = [[1,2],[2,3]]
print(sol.findJudge(N, trust))

# Test 4
N = 3; trust = [[1,2],[2,3]]
print(sol.findJudge(N, trust))

# Test 5
N = 4; trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
print(sol.findJudge(N, trust))

# Test 6
N = 1; trust = []
print(sol.findJudge(N, trust))