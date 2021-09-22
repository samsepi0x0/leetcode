class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sl = list(s)
        st = list(t)
        sl.sort()
        st.sort()
        i = 0
        while i < len(s):
            if sl[i] != st[i]:
                return False
            i += 1
        return True
