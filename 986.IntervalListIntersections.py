#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 21:54:45 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/537/week-4-may-22nd-may-28th/3338/
Problem description: 
Interval List Intersections
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""
# Intersection example:
# [1,3], [2, 5] -> take maximum of start (left values) and minimum of end (right values)
# Pay attention: start value of intersection must be less or equal than end value
# [20, 22], [13, 19] -> no intersection

# Time: O(m+n), space: O(m+n)
class Solution:
    def intervalIntersection(self, A, B):
        result  = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            minA, maxA = A[i]
            minB, maxB = B[j]
            # there is no interesection - take next interval from A
            if maxA < minB:
                i += 1
                continue  
            else:
                start = max(minA, minB)
                end = min(maxA, maxB)
                # interval intersection condition
                if start <= end:
                    result.append([start, end])
            # take next interval from A
            if maxA < maxB:
                i += 1
            # take next interval from B
            else:
                j += 1
        return result

    
sol = Solution()

# Test 1
A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]
print(sol.intervalIntersection(A, B))