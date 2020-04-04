#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 22:07:34 2020

@author: nenad
"""

"""
Problem link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Problem description:Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

"""

class Solution: 
  
  def binarySearch(self, arr, low, high, el):
      if low > high:
          return -1
      mid = low + (high-low//2)
      if arr[mid] == el:
          return mid
      elif arr[mid] > el:
          return self.binarySearch(arr, low, mid-1, el)
      else:
          return self.binarySearch(arr, mid+1, high, el)
      
  def searchRange(self, arr, target):
    
      n = len(arr)
      ind = self.binarySearch(arr, 0, n-1, target)
      if ind == -1:
          return [ind, ind]
      else:
          # search for right index
          for j in range(ind, n):
              if arr[j] != target:
                  break
              rightIndex = j
          # search for left index
          for j in range(ind, -1, -1):
              if arr[j] != target:
                  break
              leftIndex = j
          return [leftIndex, rightIndex]