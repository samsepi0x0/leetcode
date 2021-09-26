class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        chars = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in chars.values():
                stack.append(i)
            if i in chars.keys():
                if stack == [] or chars[i] != stack.pop():
                    return False
        return stack == []
