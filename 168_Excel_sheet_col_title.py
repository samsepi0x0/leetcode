import math
class Solution:
    def convertToTitle(self, col: int) -> str:
        if col >= 1 and col <= 26:
            return chr(65+col-1)
        s = ""
        while col > 0:
            col -= 1
            r = col % 26

            col = int(col/26)

            s = chr(65 + r) + s
        
        return s
