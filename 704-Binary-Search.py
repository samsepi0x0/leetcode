class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        lb, ub = 0, len(nums)-1
        while lb <= ub:
            mid = (lb+ub) // 2
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                lb = mid + 1
            if target < nums[mid]:
                ub = mid - 1
        return -1
