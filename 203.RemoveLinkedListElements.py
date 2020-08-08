#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:53:19 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/remove-linked-list-elements/
Problem description: 
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        node = head
        newHead = None
        prev = None
        while node:
            if node.val == val:
                if node == head:
                    if not node.next or node.next.val != val:
                        newHead = node.next
                else:
                    if prev:
                        prev.next = node.next
            else:
                if not newHead:
                    newHead = node
                prev = node

            node = node.next
        return newHead
    

def printList(head):
    node = head
    while node:
        print(node.val, end= " ")
        node = node.next
        
sol = Solution()

# Test 1
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

        
head = sol.removeElements(n1, 6)
printList(head)
print()

# Test 2
n1 = ListNode(6)
n2 = ListNode(2)
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

        
head = sol.removeElements(n1, 6)
printList(head)
print()



# Test 3
n1 = ListNode(1)
n2 = ListNode(1)    
n1.next = n2
head = sol.removeElements(n1, 1)
printList(head)
print()


# Test 4
n1 = ListNode(1)
n2 = ListNode(2)    
n3 = ListNode(2)
n4 = ListNode(1)    

n1.next = n2
n2.next = n3
n3.next = n4

head = sol.removeElements(n1, 2)
printList(head)
print()


    
                    
        