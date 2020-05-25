#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:43:15 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/uncrossed-lines/
Problem description: 
Uncrossed Lines
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000
   Hide Hint #1  
Think dynamic programming. Given an oracle dp(i,j) that tells us how many lines A[i:], B[j:] [the sequence A[i], A[i+1], ... and B[j], B[j+1], ...] are uncrossed, can we write this as a recursion?

"""
# Time: O(m*n), space: O(m*n)
class Solution:
    def maxUncrossedLines(self, A, B) -> int:
        m, n = len(A), len(B)
        if m == 0 or n == 0:
            return 0
        dp = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                # if ith value of A is equal to jth value of B - increment value of A[:i-1], B[:i-1] case
                if A[i-1] == B[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                # else use 
                # max of these cases:
                # 1) A[:i-1], B[:i]
                # 2) A[:i], B[:i-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

sol = Solution()

# Test 1
A = [1,4,2]; B = [1,2,4]
print(sol.maxUncrossedLines(A, B))


# Test 2
A = [2,5,1,2,5]; B = [10,5,2,1,5,2]
print(sol.maxUncrossedLines(A, B))


# Test 2
A = [1,3,7,1,7,5]; B = [1,9,2,5,1]
print(sol.maxUncrossedLines(A, B))