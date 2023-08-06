class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        if (len(nums) <= 2):
            return True
        for i in range(1, len(nums)):
            if (nums[i] + nums[i-1] >= m): # if anythere in the array 2 elements exists that have the sum >= m then it is possible to break the array into that form.
                return True
        return False
