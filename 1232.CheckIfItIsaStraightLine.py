#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:39:10 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/check-if-it-is-a-straight-line/
Problem description:
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:


Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.

"""
# straight line = all points are on the same line (linear line)
# Time: O(n), space: O(1)
class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        # y1 = kx1 + n
        # y2 = kx2 + n
        # defense against zero division - if they have the same x coord, and every point is unique,
        # we cannot have straight line -> two points that have the same x coord, must have the same y coord
        # to be on the straight line - actually these two points are the same -> contradiction
        if x1 == x2:
            return False
        # y = kx + n
        k = (y1-y2)/(x1-x2)
        
        n = y1 - k * x1
        # check if every other point lies on the same line
        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            yEst = k * x + n
            if yEst != y:
                return False
        return True
    
sol = Solution()

# Test 1
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(sol.checkStraightLine(coordinates))

# Test 2
coordinates = coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(sol.checkStraightLine(coordinates))
        
        