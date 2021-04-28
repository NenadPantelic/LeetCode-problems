#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 14:28:35 2021

@author: nenad
"""
"""
URL: https://leetcode.com/problems/unique-paths/
Description:
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        visited = [[False for j in range(n)] for i in range(m)]
        count = 0
        def isValid(i, j, m, n, visited):
            return 0 <= i < m and 0 <= j < n and not visited[i][j]
    
        def moveInGrid(row, col, m, n, visited):
            nonlocal count
            if row == m-1 and col == n-1:
                return True
            visited[row][col] = True
            if isValid(row+1, col, m, n, visited):
                bottomMoveRes = moveInGrid(row+1, col, m, n, visited)
                if bottomMoveRes:
                    count += 1
            
            if isValid(row, col + 1, m, n, visited):
                rightMoveRes = moveInGrid(row, col + 1, m, n, visited)
                if rightMoveRes:
                    count += 1
            visited[row][col] = False
        moveInGrid(0, 0, m, n, visited)
        return count
    
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            dp[i][0] = 1
        
        for i in range(n):
            dp[0][i] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        
                    
    
            
        