"""
URL: https://leetcode.com/problems/merge-k-sorted-lists/
Description: 
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __gt__(self, other):
        return self.node.val > other.node.val
    def __lt__(self, other):
        return self.node.val < other.node.val
    def __eq__(self, other):
        return not(self > other) and not(self < other)
from heapq import heappush, heappop, heapify
            
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        resHead = None
        node = None
        heads = []
        n = len(lists) 
        for i in range(n):
            if lists[i] is not None:
                heappush(heads, HeapNode(lists[i]))
                lists[i] = lists[i].next
        while heads:
            nextHeapNode = heappop(heads)
            nextNode = nextHeapNode.node
            if resHead is None:
                resHead = nextNode
                node = resHead
            else:
                node.next = nextNode
                node = nextNode
            nextNode = nextNode.next
            if nextNode is not None:
                heappush(heads, HeapNode(nextNode))
        return resHead
            
            
