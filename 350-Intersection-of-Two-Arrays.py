class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums3 = []
        for i in nums1:
            if i in nums2:
                nums3.append(i)
                nums2.remove(i)
        return nums3
