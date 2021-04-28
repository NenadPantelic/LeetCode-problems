#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:24:04 2020

@author: nenad
"""
"""
Problem URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
Problem description:
    
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

"""

# Time: O(log(n)), space: O(1)
class Solution:
    # find starting point of non-rotated array
    def findStartOfTheArray(self, nums, low, high):
        # low and high matched
        if low == high: return low
        # array is not rotated
        if low > high: return -1
        mid = low + (high-low)//2
        # rotation detected
        # e.g. 3 4 5 1 2
        if mid < high and nums[mid] > nums[mid+1]:
            return mid+1
        # example 4 5 1 2 3
        if low < mid and nums[mid] < nums[mid-1]:
            return mid
        # 3 4 1 2 e.g  -> use right side of ther array - there are smaller elements
        if nums[low] > nums[high]:
            return self.findStartOfTheArray(nums, mid+1, high)
        # use left side -> there are smaller elements
        return self.findStartOfTheArray(nums, 0, mid-1)
            
        
    # binary search = O(log(n))
    def binarySearch(self, nums, target, low, high):
        if low > high:
            return -1
        mid = low + (high-low)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(nums, target, low, mid-1)
        else:
            return self.binarySearch(nums, target, mid+1, high)
        
    # general idea - 
    # 1) find pivot index (starting index of non-rotated array)
    # 2) search left subarray -> if element is found -> return index
    # 3) search right subarray -> if element is found -> return index
    # 4) return -1 -> element is not present
    def search(self, nums, target: int) -> int:
        n = len(nums)
        startingIndex = self.findStartOfTheArray(nums,0 ,n-1)
        # index is non-rotated, use only one binary search
        if startingIndex <= 0:
            return self.binarySearch(nums, target, 0, n-1)
        leftSearch = self.binarySearch(nums, target, 0, startingIndex-1)
        if leftSearch != -1:
            return leftSearch
        rightSearch = self.binarySearch(nums, target, startingIndex, n-1)
        if rightSearch != -1:
            return rightSearch
        return -1
    
    def search(self, nums, target: int) -> int:
        def _search(nums, low, high, target):
            if low > high:
                return -1
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            
            if nums[low] <= nums[mid] <= nums[high]:
                if nums[mid] > target:
                    return _search(nums, low, mid-1, target)
                return _search(nums, mid+1, high, target)
            if nums[mid] <= nums[high]:
                if target > nums[high] or target <= nums[mid]:
                    return _search(nums, low, mid, target)
                return _search(nums, mid+1, high, target)
                    
            if nums[low] <= nums[mid]:
                if target < nums[low] or target >= nums[mid]:
                    return _search(nums, mid+1, high, target)
                return _search(nums, low, mid, target)
        return _search(nums, 0, len(nums)-1, target)   

    
    
sol = Solution()
# Test 1
nums = [4,5,6,7,8,9,0,1,2]
print(sol.search(nums, 4))

# Test 2
nums = [4,5,6,7,0,1,2]
print(sol.search(nums, 3))

# Test 3
nums = [0,1,2,3,4,5]
print(sol.search(nums, 5))

# Test 4
nums = [3,1]
print(sol.search(nums, 1))

# Test 5
nums = [6,7,1,2,3,4,5,]
print(sol.search(nums, 6))

# Another very elegant solution
class Solution(object):
    def search(self, nums, target: int) -> int:
        def binSearch(l,r):
            if l > r:
                return -1
            m = (r+l)//2
            if nums[m] == target:
                return m
             # follow left half if left is sorted and target is in its range or right is sorted but target not in its range
            if nums[l] <= target < nums[m] or (nums[m] <= nums[r]  and not nums[m] < target <= nums[r]):
                return binSearch(l,m-1)
            else: 
                return binSearch(m+1, r)
        return binSearch(0,len(nums)-1)
        
sol = Solution()
# Test 1
nums = [4,5,6,7,8,9,0,1,2]
print(sol.search(nums, 4))

# Test 2
nums = [4,5,6,7,0,1,2]
print(sol.search(nums, 3))

# Test 3
nums = [0,1,2,3,4,5]
print(sol.search(nums, 5))

# Test 4
nums = [3,1]
print(sol.search(nums, 1))

# Test 5
nums = [6,7,1,2,3,4,5,]
print(sol.search(nums, 6))

# Time: O(log(n))
class Solution(object):
    def search(self, nums, target: int) -> int:
        def binSearch(nums, target, low, high):
            #print(low, high)
            if low > high:
                return -1
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid
            # go left if the left half is sorted and target value is from that range or if the right
            # half is sorted but the value is not from that range
            if (nums[low] <= target < nums[mid]) or (nums[mid] < nums[high] and (nums[mid] > target or nums[high] < target)):
                high = mid - 1
            # otherwise, go right
            else:
                low = mid + 1
            return binSearch(nums, target, low, high)
        return binSearch(nums, target, 0, len(nums)-1)


print()
print()      
sol = Solution()
# Test 1
nums = [4,5,6,7,8,9,0,1,2]
print(sol.search(nums, 4))

# Test 2
nums = [4,5,6,7,0,1,2]
print(sol.search(nums, 3))

# Test 3
nums = [0,1,2,3,4,5]
print(sol.search(nums, 5))

# Test 4
nums = [3,1]
print(sol.search(nums, 1))

# Test 5
nums = [6,7,1,2,3,4,5,]
print(sol.search(nums, 6))

# Test 6
nums = [4,5,6,7,8,9,0,1,2]
print(sol.search(nums, 8))           

# Test 7
nums = [4,5,6,7,8,1,2,3]
print(sol.search(nums, 8))           

# Test 8 
nums = [4,5,6,7,0,1,2]
print(sol.search(nums, 0))


# Test 9
nums = [5,1,2,3,4]
print(sol.search(nums, 1))