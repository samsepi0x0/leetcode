class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        isomorph = dict()
        for index, val in enumerate(s):
            if val in isomorph.keys():
                #print(val, " --> ", isomorph[val], "\t", t[index])
                if not isomorph[val] == t[index]:
                    return False
            else:
                if t[index] in isomorph.values():
                    return False
                isomorph[val] = t[index]
                
                #print(val, " ---> ", isomorph[val], "\t", t[index])
        return True
