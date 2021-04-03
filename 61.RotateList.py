#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 13:16:18 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/rotate-list/
Problem description: 
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or k == 0:
            return head
        node = head
        length = 0
        while node:
            prev = node
            length += 1
            node = node.next
        pivotIndex = length - (k % length)
        if k % length == 0:
            return head
        tail = prev
      
        node = head
        i = 0
        while node and i < pivotIndex:
            prev = node
            node = node.next
            i += 1
        prev.next = None
        tail.next = head
        return node 

class Solution:
    def rotateRight(self, node: ListNode, k: int) -> ListNode:
        if node is None:
            return None
        lenOfList = 0
        head = node
        tail = None
        while node:
            tail = node
            node = node.next
            lenOfList += 1
            
        rotationPos = lenOfList - (k % lenOfList)
        if rotationPos == lenOfList:
            return head
        node = head
        i = 0
        prev = None
        while i  < rotationPos:
            prev = node
            node = node.next
            i += 1
        prev.next = None
        tail.next = head
        return node  

def printList(head):
    node = head
    while node:
        print(node.val, end= " ")
        node = node.next
    print()


sol = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5


head = sol.rotateRight(n1, 5)
printList(head)

n1 = ListNode(1)

head = sol.rotateRight(n1, 5)
printList(head)
        