#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:14:03 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/last-stone-weight/
    
Problem description: 
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

Example 1:

Input: [2,7,4,1,8,1]
Output: 1
Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.
 

Note:

1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""


import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:
        
        # convert values to negative - we use min heap, but we have to extract max in every iteration, so 
        # we will convert values to negative -> we need max heap
        heap = [-x for x in stones]
        # heapify array
        heapq.heapify(heap)
        # while heap is non-empty
        while len(heap):
            # take the heaviest stone - get original value (multiply with -1)
            # O(logn)
            maxx = -heapq.heappop(heap)
            # take second heaviest, if there is one
            if len(heap):
                # O(logn)
                maxx2 = -heapq.heappop(heap)
            # else return last stone
            else:
                return maxx
            # push difference of heaviest stones to heap - with minus sign -> -(maxx-maxx2) = maxx2 - maxx
            if maxx != maxx2:
                # O(logn)
                heapq.heappush(heap, maxx2-maxx)
        # default case
        return 0
                
    
sol = Solution()
# Test 1
stones = [2,7,4,1,8,1]
print(sol.lastStoneWeight(stones))

# Test 2
stones = [2,2]
print(sol.lastStoneWeight(stones))

# Test 3
stones = [3]
print(sol.lastStoneWeight(stones))
