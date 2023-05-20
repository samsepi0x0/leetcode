class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int tail1 = m - 1; // last of array nums1
        int tail2 = n - 1; // last of array nums2

        int fin = m + n - 1; // last of the final array to be created.

        while(tail1 >=0 && tail2 >= 0){ // place bigger elements from last of array
            nums1[fin--] = nums1[tail1] > nums2[tail2] ? nums1[tail1--] : nums2[tail2--];
        }   
        while (tail2 >= 0){ // copy remaining elements from the array
            nums1[fin--] = nums2[tail2--];
        }
    }
}
