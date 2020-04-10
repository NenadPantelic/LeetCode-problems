#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 13:07:24 2020

@author: nenad
"""
"""
Problem description: https://leetcode.com/problems/min-stack/
"""

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None
        
    # O(1)
    def push(self, x: int) -> None:
        # stack is empty
        if self.min is None:
            self.stack.append(x)
            self.min = x
        # new minimum found - store relation to old minimum = 2 * newMin - oldMin
        elif x <= self.min:
            self.stack.append(2*x - self.min)
            self.min = x
        # value is greater than min, store that value
        else:
            self.stack.append(x)
    # O(1)
    def pop(self) -> None:
        # remove top element
        val = self.stack.pop(-1)
        retVal = val
        # we popped minimum - update minimum with the value that was minimum before this value come
        if val <= self.min:
            retVal = self.min
            # update min with the value we got from stack (relation to old minimum)
            if len(self.stack):
                self.min = 2 * self.min - val
            else:
                self.min = None
        return retVal
        
    # O(1)
    def top(self) -> int:
        val = self.stack[-1]
        retVal = val
        if val < self.min:
            retVal = self.min
        return retVal
        
    # O(1)
    def getMin(self) -> int:
        return self.min
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# Test 1      
minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
print(minStack.getMin());#   --> Returns -3.
print(minStack.pop());
print(minStack.top());    #  --> Returns 0.
print(minStack.getMin()); #  --> Returns -2.


# Test 2      
minStack2 = MinStack();
minStack2.push(0);
minStack2.push(1);
minStack2.push(0);
print(minStack2.getMin());#   --> Returns -3.
print(minStack2.pop());
print(minStack2.getMin()); #  --> Returns -2.


def parseInput(commands, values):
    mStack = MinStack()
    for i in range(1, len(commands)):
        command = commands[i]
        if command == "push":
            mStack.push(values[i][0])
        elif command == "top":
            print(mStack.top())
        elif command == "pop":
            print(mStack.pop())
        else:
            print(mStack.getMin())
            
parseInput(["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
,[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]])