# Given a non-empty array of digits representing a non-negative integer, 
# plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, 
# and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        for i in range(1,length+1):
            if digits[length-i] < 9:
                digits[length-i] += 1
                return digits
            digits[length-i] = 0 # this step is how a computer does in computation
        return [1]+[0]*length