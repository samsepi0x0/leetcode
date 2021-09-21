class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        st = set()
        for i, x in enumerate(s):
            if not x in st:
                d[x] = i
                st.add(x)
            elif x in d:
                del d[x]
        if d:
            return min(d.values())
        return -1
                
