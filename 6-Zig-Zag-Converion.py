class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        rows = [[] for x in range(numRows)]
        currRow, down, st = 0, False, ""
        for i in list(s):
            rows[currRow].append(i)
            if currRow == 0 or currRow == numRows - 1:
                down = not down
            currRow += 1 if down else -1
        for i in rows:
            for j in i:
                st += j
        return st
            
