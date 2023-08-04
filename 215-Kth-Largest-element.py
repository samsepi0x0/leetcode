class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # troll soln
        nums.sort(reverse=True)
        return nums[k-1]
