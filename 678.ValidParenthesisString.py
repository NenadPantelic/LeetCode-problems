"""
URL: https://binarysearch.com/problems/Balanced-Brackets-Sequel
Description:
Given a string s containing round, curly, and square open and closing brackets, return whether the brackets are balanced.

Constraints

n ≤ 100,000 where n is the length of s
Example 1
Input
s = "[(])"
Output
False
Example 2
Input
s = "([])[]({})"
Output
True
"""

class Solution:
    def solve(self, s: str) -> bool:
    	# write your awesome code here
        stack = []
        bracketMap = {'(':')', '[':']', '{':'}'}
        for bracket in s:
            if bracket in bracketMap:
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                openingBracket = stack.pop(-1)
                if bracketMap[openingBracket] != bracket:
                    return False
        return len(stack) == 0
