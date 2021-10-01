class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        f_nums = []
        for x in nums:
            f_nums.append(x ** 2)
        f_nums.sort()
        return f_nums
