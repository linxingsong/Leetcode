# Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
# return the length of last word (last word means the last appearing word
#  if we loop from left to right) in the string.

# If the last word does not exist, return 0.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_s = len(s)
        if 0 == len_s:
            return 0

        index = len_s - 1
        while index >= 0 and ' ' == s[index]:
            index -= 1
        len_last_word = 0
        while index >= 0 and ' ' != s[index]:
            len_last_word += 1
            index -= 1
        return len_last_word

        #2nd solution

        #return len(s.rstrip(' ').split(' ')[-1])

