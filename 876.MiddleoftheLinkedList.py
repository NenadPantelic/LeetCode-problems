#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:32:15 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/middle-of-the-linked-list/
Problem description:
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the fast middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the fast one.
    

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Time: O(n), space: O(1)
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
                
        # two pointers - runner method
        slow = head
        fast = head.next
        
        # slow goes one step further
        # fast goes one step further
        while fast:
            slow = slow.next
            fast = fast.next
            if  not fast:
                break
            fast = fast.next
        return slow
    
sol = Solution()

def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
        

# Test 1
l1 = ListNode(1)
l = l1
i = 1
arr = [1,2,3,4,5]
while i  < 5:
    l.next = ListNode(arr[i])
    l = l.next
    i += 1
printList((sol.middleNode(l1)))
print()
# Test 2
l1 = ListNode(1)
l = l1
i = 1
arr = [1,2,3,4,5,6]
while i  < 6:
    l.next = ListNode(arr[i])
    l = l.next
    i += 1

printList((sol.middleNode(l1)))
# Test 3
print()
l = ListNode(1)
printList(sol.middleNode(l))
