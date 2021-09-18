class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof, min_price = 0, 10 ** 4
        for i in prices:
            min_price = min(i, min_price)
            curr_prof = i - min_price
            max_prof = max(curr_prof, max_prof)
        return max_prof
