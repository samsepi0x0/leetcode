class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # used merge sort coz time complexity is O(log(m+n))
        arr = [None]*(len(nums1) + len(nums2))
        i = 0
        j = 0
        k = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                arr[k] = nums1[i]
                k += 1
                i += 1
            else:
                arr[k] = nums2[j]
                k += 1
                j += 1
        while i < len(nums1):
            arr[k] = nums1[i]
            k += 1
            i += 1
        while j < len(nums2):
            arr[k] = nums2[j]
            k += 1
            j += 1
        print(arr)
        index = int(len(arr)/2)
        print(index)
        if len(arr)%2 != 0:
            return arr[index]
        return (arr[index-1] + arr[index])/2
