# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000


def value(r): 
    if (r == 'I'): 
        return 1
    if (r == 'V'): 
        return 5
    if (r == 'X'): 
        return 10
    if (r == 'L'): 
        return 50
    if (r == 'C'): 
        return 100
    if (r == 'D'): 
        return 500
    if (r == 'M'): 
        return 1000
    return -1

class Solution:
    def romanToInt(self, s: str) -> int:
        index = 0
        ans = 0
        
        while(index<len(s)):
            s1 = value(s[index])
            if( index+1 < len(s)):
                s2 = value(s[index+1])
                if(s1>=s2):
                    ans = ans + s1
                    index +=1
                else:
                    ans= ans+s2-s1
                    index +=2
            else:
                ans = ans + s1
                index +=1
        return ans

