# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0): return False
        checkNum = x
        revNum = 0
        while(x != 0):
            temp = x % 10
            revNum = revNum *10 + temp
            x = x // 10

        return True if ( checkNum == revNum ) else False