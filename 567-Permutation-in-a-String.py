class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        chars1 = dict()
        for i in s1:
            chars1.setdefault(i, 0)
            chars1[i] += 1
        
        i, j = 0, 0
        while j < len(s2):
            j = i + len(s1)
            temp = s2[i:j]
            curr = dict()
            for k in temp:
                curr.setdefault(k, 0)
                curr[k] += 1
            if curr == chars1:
                return True
            i += 1
        
        return False
