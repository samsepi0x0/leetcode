class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # # Troll soln: O(n)
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     return -1

        l = 0
        r = len(nums) - 1

        while(l < r):
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        pivot = l

        l = 0
        r1 = pivot - 1

        while l <= r1:
            mid = (l + r1) // 2
            if (nums[mid] == target):
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r1 = mid - 1
        
        l = pivot
        r2 = len(nums) - 1

        while l <= r2:
            mid = (l + r2) // 2
            if (nums[mid] == target):
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r2 = mid - 1
        
        return -1
        
