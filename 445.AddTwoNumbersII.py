#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 19:44:32 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/add-two-numbers-ii/
Problem description: 
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        firstListLen = secondListLen = 0
        node1, node2 = l1, l2
        while node1 or node2:
            if node1:
                node1 = node1.next
                firstListLen += 1
            if node2:
                node2 = node2.next
                secondListLen += 1
        
        
        