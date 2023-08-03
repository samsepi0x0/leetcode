import itertools
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        values = {'1': [""], '2': ["a","b","c"], '3': ["d", "e", "f"], '4': ["g", "h", "i"], '5': ["j","k","l"], '6':["m", "n", "o"], '7': ["p", "q", "r", "s"], '8':["t", "u", "v"], '9':["w", "x", "y", "z"]}

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return values[digits]

        combs = values[digits[0]]

        for i in range(1, len(digits)):
            val = values[digits[i]]
            new_comb = list()
            combs = ["".join(list(i)) for i in list(itertools.product(combs, val))]

            # temp = list(itertools.product(combs, val))
            # for i in temp:
            #     s = "".join(list(i))
            #     new_comb.append(s)
            # combs = new_comb
        return combs
