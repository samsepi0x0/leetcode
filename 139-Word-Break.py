class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        @lru_cache(None) 
        #set maxsize to None , then the cache will grow indefinitely, and no entries will be ever evicted.


        def recur(st):
            if (st == n):
                return True # recursively we are at last of the array, meaning its true we got all words in the dict
            for i in range(st + 1, n+1): # find subset of s in sizes of i
                w = s[st:i]
                if w in wordSet and recur(i): # if word is found then check for remaining string for other combinations.
                    return True # both true aand we got the soln.
            return False # cant find the soln
    
        return recur(0)
            
