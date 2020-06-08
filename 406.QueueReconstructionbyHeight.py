#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 21:13:10 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/problems/queue-reconstruction-by-height/
Problem description: 
Queue Reconstruction by Height
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
 

   Hide Hint #1  
What can you say about the position of the shortest person?
If the position of the shortest person is i, how many people would be in front of the shortest person?
   Hide Hint #2  
Once you fix the position of the shortest person, what can you say about the position of the second shortest person?
"""
# Time: O(n^2), space: O(n)
class Solution:
    def reconstructQueue(self, people):
        n = len(people)
        people.sort()        
        queue = [None] * n
        for person in people:
            height, pos = person
            count = pos
            for i in range(n):
                # we found pos k positions in total, that are empty slots or in these places
                # stand persons with the height greater or equal than current
                # height. Another condition is that current place is empty, so we can place this person there (else
                # we would overwrite some person)
                if count == 0 and queue[i] is None:
                    queue[i] = person
                    break
                # empty place or place where stands person with the height which is >= than the current one
                if queue[i] is None or queue[i][0] >= height:
                    count -= 1
            
        return queue
            
sol = Solution()

# Test 1
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(sol.reconstructQueue(people))