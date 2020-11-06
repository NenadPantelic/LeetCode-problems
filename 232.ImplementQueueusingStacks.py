#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:30:43 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/problems/implement-queue-using-stacks/
Problem description: 
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.poppingStack = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
    
    def _copyToPoppingStack(self):
        while self.stack:
            self.poppingStack.append(self.stack.pop(-1))

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """

        if not len(self.poppingStack):
            self._copyToPoppingStack()
            
        if not len(self.poppingStack):
            return -1
        return self.poppingStack.pop(-1)
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not len(self.poppingStack):
            self._copyToPoppingStack()
        if not len(self.poppingStack):
            return -1
        return self.poppingStack[-1]
        
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not(self.stack or self.poppingStack)
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()     

        