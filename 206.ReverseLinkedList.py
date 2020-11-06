#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 20:04:14 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/reverse-linked-list/
Problem description: 
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        node = head
        prev = None
        while True:
            next = node.next
            node.next = prev
            prev = node
            if not next:
                break
            node = next
            
        return node
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        def reverse(node, prev):
            next = node.next
            node.next = prev
            if not next:
                return node
            return reverse(next, node)
        return reverse(head, None)
            
        
    
def printList(node):
    while node:
        print(node.val, end= " ")
        node = node.next
    print()


sol  = Solution()    
    
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3

head = sol.reverseList(n1)
printList(head)




        