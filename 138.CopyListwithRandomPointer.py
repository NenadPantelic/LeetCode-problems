#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:57:41 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/copy-list-with-random-pointer/
    
Problem description: 
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
    
        newHead = None
        node = head
        newNode = None
        prevNode = None
        nodeMap = {}
        idMap = {}
        while node:
            newNode = Node(node.val, None, None)
            nodeMap[id(node)] = id(newNode)
            idMap[id(newNode)] = newNode
            if newHead is None:
                newHead = newNode
            if prevNode:
                prevNode.next = newNode
            prevNode = newNode
            node = node.next
        
        node = head
        while node:
            mappedNode = idMap[nodeMap[id(node)]]
            randomConnectedNode = None
            if node.random:
                randomConnectedNode = idMap[nodeMap[id(node.random)]]
    
            mappedNode.random = randomConnectedNode
            node = node.next
        return newHead
    
n1 = Node(7, None, None)
n2 = Node(13, None, None)
n3 = Node(11, None, None)
n4 = Node(10, None, None)
n5 = Node(1, None, None)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n2.random = n1
n3.random = n5
n4.random = n3
n5.random = n1


def printList(node):
    while node:
        print(node.val, node.next.val if node.next else None, node.random.val if node.random else None, end= " ")
        node = node.next

newHead = Solution().copyRandomList(n1)
printList(newHead)
        
        

            
            
            
        