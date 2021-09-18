class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ind = {}
        max_len = 0
        index = 0
        for i in range(0, len(s)):
            if s[i] in ind:
                index = max(index, ind[s[i]] + 1)
            max_len = max(max_len, i-index + 1)
            ind[s[i]] = i
        return max_len
