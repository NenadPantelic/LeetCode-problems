#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:20:02 2020

@author: nenad
"""

"""
Problem URL: https://leetcode.com/problems/linked-list-cycle-ii/
Problem description: 
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

a+2b+c==2*(a+b)==>a==c
From the beginning until the two pointers meet, the location where they meet is Z; the distance traveled by the slow pointer isa+b, and the distance traveled by the fast pointer is a+b+c+b;
Because the slow pointer moves one step at a time and the fast pointer moves two steps at a time,no matter what time, the distance of the fast pointer is always twice that of the slow pointer, which is 2*(a+b)==a+b+c+ b.Then,we can knowa==c.
Hope this can help you:)

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Time: O(n)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        

        if slow != fast:
            return None
        node = head
        while node != fast:
            node = node.next
            fast = fast.next
        return node


sol = Solution()

n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2
print(sol.detectCycle(n1).val)

n1 = ListNode(3)
n1.next = n1
print(sol.detectCycle(n1).val)



n1 = ListNode(-1)
n2 = ListNode(-7)
n3 = ListNode(7)
n4 = ListNode(-4)
n5 = ListNode(19)
n6 = ListNode(6)
n7 = ListNode(-9)
n8 = ListNode(-5)
n9 = ListNode(-2)
n10 = ListNode(-5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
n10.next = n10

print(sol.detectCycle(n1).val)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
print(sol.detectCycle(n1))

arr = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
node = ListNode(-21)
first = node
i = 1
while i < len(arr):
    prev = node
    node.next = ListNode(arr[i])
    node = node.next
    if i == 24:
        target = node
    i += 1
    
node.next = target
print(sol.detectCycle(first).val)
            
        