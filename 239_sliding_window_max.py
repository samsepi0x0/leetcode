class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque will be required
        d = collections.deque()
        slide_max = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                slide_max += nums[d[0]],
        return slide_max
