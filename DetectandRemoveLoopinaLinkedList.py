"""
URL: https://afteracademy.com/problems/detect-and-remove-loop-in-a-linked-list
Description: 
You are given the head of a linked list which probably contains a loop. If the list contains a loop, you need to find the last node of the list which points to one of its previous nodes to create a loop and make it point to NULL, thereby removing the loop

Problem Note:

It's possible that the linked list does not contain a loop
Do not use extra space
Example 1

Input:   1 -> 2 -> 3 -> 4 -> 5
                   |         |
                   |         |    
                   - - - - - -
Output:  1 -> 2 -> 3 -> 4 -> 5
Explanation: The node 5 at the end of loop points to 3 and creates a loop. We make it point to NULL and remove the loop.
Example 2

Input: 2 -> 20 -> 6 -> 19 -> 13 -> 4
Output: 2 -> 20 -> 6 -> 19 -> 13 -> 4
Explanation: No loop present.
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @type of head: ListNode
 	# @return type: ListNode
    def detectAndRemoveLoop(self, head: ListNode) -> ListNode:
        # write your awesome code here
        slow = head
        fast = head.next
        if slow is None or fast is None:
            return head
        while True:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return head
            if slow == fast:
                slow = head
                break
        while True:
            if fast.next == slow:
                fast.next = None
                return head
            fast = fast.next
            slow = slow.next
            
               
