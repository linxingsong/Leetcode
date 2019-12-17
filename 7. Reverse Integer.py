# 7. Reverse Integer
# Easy

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 
# when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
       # think about negative
        negativeFlag = False

        rev = 0 #default rev 

        if(x <0):
            negativeFlag = True
            x = -x #change to positive.
        
        while (x != 0):
            curr_digit = x % 10
            rev = (rev * 10) + curr_digit

            if (rev >= 2147483647 or rev <= -2147483648): 
                rev= 0

            x = x // 10 
        
        return -rev if (negativeFlag == True) else rev
        
