 class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lb, ub = 0, len(nums) - 1
        while lb <= ub:
            mid = (lb + ub) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                ub = mid - 1
            else:
                lb = mid + 1
        return lb
