#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:19:59 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/find-median-from-data-stream/
Problem description: 
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""
# Time: O(log(n))
from heapq import heapify, heappushpop, heappush
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap, self.maxHeap = [], []
        
        

    def addNum(self, num: int) -> None:
        if len(self.minHeap) == len(self.maxHeap) == 0:
            heappush(self.minHeap, num)
        else:
            if num >= self.minHeap[0]:
                if len(self.minHeap) == len(self.maxHeap):
                    heappush(self.minHeap, num)        
                else:
                    heappush(self.maxHeap, -heappushpop(self.minHeap, num))
            elif num <= self.minHeap[0]:
                if len(self.minHeap) == len(self.maxHeap):
                    heappush(self.minHeap, -heappushpop(self.maxHeap, -num)) 

                else:
                    heappush(self.maxHeap, -num)                            

    def findMedian(self) -> float:
        if len(self.maxHeap) < len(self.minHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
arr = [1, 2, 3, 2, 5, 2, 4,2 ,5,1, -1, 4,2]
medianFilter = MedianFinder()
for val in arr:
    medianFilter.addNum(val)
    print(medianFilter.maxHeap, medianFilter.minHeap)
    print(medianFilter.findMedian())
    
            
        