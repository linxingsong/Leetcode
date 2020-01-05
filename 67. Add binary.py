
class Solution:
    def addBinary(self, a: str, b: str) -> str:
    
    #convert to int, than convert to binary format then output if.

    return str(bin(int(a, 2) + int(b, 2)))[2:]