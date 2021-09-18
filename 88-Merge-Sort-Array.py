class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Note: L and R are already given and sorted so only merging is to be done
        """
        i = m + n - 1
        m -= 1
        n -= 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                nums1[m] = 0
                m -= 1
            else:
                nums1[i] = nums2[n]
                nums2[n] = 0
                n -= 1
            i -= 1
        
        while m >= 0:
            nums1[i], nums1[m] = nums1[m], nums1[i]
            i -= 1
            m -= 1
        
        while n >= 0:
            nums1[i], nums2[n] = nums2[n], nums1[i]
            i -= 1
            n -= 1
