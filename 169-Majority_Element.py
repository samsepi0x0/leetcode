class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        majority = 0
        for key, val in zip(d.keys(), d.values()):
            if val > floor(len(nums) / 2):
                majority = key
        return majority
