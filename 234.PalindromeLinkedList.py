#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 14:27:40 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/palindrome-linked-list/
Problem description:
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Time: O(n), space: O(n/2)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow, fast = head, head.next
        stack = [slow.val]
        k = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast:
                stack.append(slow.val)
        
        
        slow = slow.next
        while slow:
            if slow.val != stack.pop(-1):
                return False
            slow = slow.next
            
        return True
            
sol = Solution()

# Test 1
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(sol.isPalindrome(n1))

# Test 2
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(2)
n1.next = n2
n2.next = n3
n3.next = n4

print(sol.isPalindrome(n1))

