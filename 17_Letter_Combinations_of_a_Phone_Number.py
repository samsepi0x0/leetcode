class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        values = {'1': [""], '2': ["a","b","c"], '3': ["d", "e", "f"], '4': ["g", "h", "i"], '5': ["j","k","l"], '6':["m", "n", "o"], '7': ["p", "q", "r", "s"], '8':["t", "u", "v"], '9':["w", "x", "y", "z"]}
        
        if digits == "": # 0
            return list()
        if len(digits) == 1: # 1
            return values[digits]

        combinations = list()
        combinations.append("")
        for i in digits:
            temp_comb = list()
            vals = values[i]
            for c in vals:
                for j in combinations:
                    temp_comb.append(j + c)
            combinations = temp_comb
        return combinations
