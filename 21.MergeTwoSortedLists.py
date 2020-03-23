#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 12:56:20 2020

@author: nenad
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # one list is empty
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        n1 = l1
        n2 = l2
        newHead = None
        nextNode = None
        while n1 and n2:
            if n1.val <= n2.val:
                node = n1
                n1 = n1.next
            else:
                node = n2
                n2 = n2.next
            
            if nextNode :
                nextNode.next = node
                nextNode = nextNode.next
            else:
                nextNode = node
                newHead = node
        # add rest of the nodes from the first list
        while n1:
            nextNode.next = n1
            n1 = n1.next
            nextNode = nextNode.next
        
        # add rest of the nodes from the second list
        while n2:
            nextNode.next = n2
            n2 = n2.next
            nextNode = nextNode.next
        
        return newHead
    
    

        
        