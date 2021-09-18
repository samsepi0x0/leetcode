class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        local_max = 0
        global_max = -10 ** 5
        for i in range(0, len(nums)):
            local_max = max(nums[i], (nums[i] + local_max))
            print(local_max)
            if local_max > global_max:
                global_max = local_max
                
        return global_max
