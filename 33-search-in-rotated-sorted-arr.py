class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[start] <= nums[mid]: # [4, 5, 6, 7, 0, 1, 2] this is the test case here
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            
            if nums[end] >= nums[mid]:
                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            
        return -1
