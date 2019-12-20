# Given a string containing just the characters 
# '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s: str) -> bool:
        p = {')' : '(', ']': '[', '}' : '{'}
        stack  =  []
        for c in s:
            if c not in p:
                stack.append(c)
            else:
                if not stack or stack[-1] != p[c]: return False
                stack.pop()
        return not stack
        