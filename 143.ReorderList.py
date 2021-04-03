"""
URL: https://leetcode.com/problems/reorder-list/
Description:
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node = head
        deque = []
        while node:
            deque.append(node)
            node = node.next
        
        
        first = 0
        last = len(deque)-1
        head = None
        nextNode = None
        while first <= last:
            leftNode = deque[first]
            rightNode = deque[last]
            if nextNode is None:
                nextNode = leftNode
            if head is None:
                head = nextNode
            if nextNode != leftNode:
                nextNode.next = leftNode
                nextNode = nextNode.next
            if rightNode is not None and leftNode != rightNode:
                nextNode.next = rightNode
                nextNode = rightNode
            nextNode.next = None
            first += 1
            last -= 1
        return head
            
            
        
            
        
