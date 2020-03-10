#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:05:10 2020

@author: nenad
"""

"""

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


"""



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        carry = 0
        head = None
        # until we traverse both lists
        while n1 or n2:
            val_1 = val_2 = 0
            if n1:
                val_1 = n1.val
                n1 = n1.next
            if n2:
                val_2 = n2.val
                n2 = n2.next  
            # value and carry
            val = (val_1 + val_2 + carry) % 10
            carry = (val_1 + val_2 + carry) // 10
            if head is None:
                node = ListNode(val)
                head = node
            else:
                node.next = ListNode(val)
                node = node.next
        # e.g. 888+333 - list becomes longer for one digit - leading 1
        if carry:
            node.next = ListNode(carry)
        return head
    
    
# Test 1
l1 = ListNode(2)
l2 = ListNode(4)
l3 = ListNode(3)
l1.next = l2
l2.next = l3

l4 = ListNode(5)
l5 = ListNode(6)
l6 = ListNode(4)
l4.next = l5
l5.next = l6

def print_list(head):
    node = head
    while node:
        print(node.val, end=" ")
        node = node.next
    print()
sol = Solution()    
head = sol.addTwoNumbers(l1, l4)
print_list(head)
    


# Test 2
l1 = ListNode(6)
l2 = ListNode(7)
l3 = ListNode(8)
l1.next = l2
l2.next = l3

l4 = ListNode(3)
l5 = ListNode(3)
l6 = ListNode(3)
l4.next = l5
l5.next = l6            
head = sol.addTwoNumbers(l1, l4)
print_list(head)
