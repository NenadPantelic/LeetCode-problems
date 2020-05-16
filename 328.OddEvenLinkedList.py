#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 19:53:13 2020

@author: nenad
"""



"""

Problem URL: https://leetcode.com/problems/odd-even-linked-list/
Problem description:
Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# Time: O(n), space: O(1)
# we move node two times in every iteration - we append the first node to odd list, and the other one to even list
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        oddHead = odd = head
        evenHead = even = head.next
        if not even:
            return oddHead
        node = even.next  
        while node:
            odd.next = node
            odd = odd.next   
            node = node.next
            if not node:
                break
            even.next = node
            even = even.next
            node = node.next       
        # disconnect tail of even list
        even.next = None  
        # connect odd list and even list - tail of odd list and head of even list
        odd.next = evenHead
        
        return oddHead
    
def printList(head):
    while head:
        print(head.val, end=" ")
        head = head.next
    print()
    
sol = Solution()

# Test 1
n1 = ListNode(1)
node = n1
for i in range(2, 6):
    node.next = ListNode(i)
    node = node.next
    
head = sol.oddEvenList(n1)
printList(head)
