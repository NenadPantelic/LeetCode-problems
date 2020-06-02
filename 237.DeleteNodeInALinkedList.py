#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:15:29 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/delete-node-in-a-linked-list/
Problem description: 
Delete Node in a Linked List
Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:



 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.
 

Note:

The linked list will have at least two elements.
All of the nodes' values will be unique.
The given node will not be the tail and it will always be a valid node of the linked list.
Do not return anything from your function.

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time and space: O(1)
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val= node.next.val
        node.next = node.next.next
        

def printLL(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
        
sol = Solution()
n1 = ListNode(4)
n2 = ListNode(5)
n3 = ListNode(1)
n4 = ListNode(9)
n1.next = n2
n2.next = n3
n3.next = n4

# Test 1
sol.deleteNode(n2)
printLL(n1)