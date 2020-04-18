#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 10:35:50 2020

@author: nenad
"""


class Solution:
    # Time: O(m*n), space: O(m*n)
    def minPathSum(self, grid) -> int:
        # dimensions of the grid
        m,n  = len(grid), len(grid[0])
        # dp table of subresults -> answer is at m-1, n-1
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                # (0,0) position -> cost is value itself
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                # first row -> only column-wise updates (check state of the coresponding element in the previous column)
                elif i == 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                # first column -> only row-wise updates (check state of the coresponding element in the 
                # previous row)
                elif j == 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                # check what's better -> to get into this position from top or from left 
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) +  grid[i][j]
        return dp[m-1][n-1]
        # note - one small optimization (memory) -> use grid directly, manipulate on grid directly (for O(1) additional space))
    
    # Time: O(m*n), space: O(1)
    def minPathSum(self, grid) -> int:
        # dimensions of the grid
        m,n  = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                # (0,0) position -> cost is value itself
                if i == 0 and j == 0:
                   continue
                # first row -> only column-wise updates (check state of the coresponding element in the previous column)
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                # first column -> only row-wise updates (check state of the coresponding element in the 
                # previous row)
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                # check what's better -> to get into this position from top or from left 
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[m-1][n-1]

    
sol = Solution()
# Test 1
grid = [[1,3,1],[1,5,1], [4,2,1]]
print(sol.minPathSum(grid))        