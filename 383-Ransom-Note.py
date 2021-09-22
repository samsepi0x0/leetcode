class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(magazine) < len(ransomNote):
            return False
        mg = list(magazine)
        for i in ransomNote:
            if i in mg:
                mg.remove(i)
            else:
                return False
        return True
