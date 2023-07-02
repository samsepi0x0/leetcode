class Solution {
    public int findMin(int[] nums) {
        // int min = nums[0]; //O(n)
        // for(int i = 1; i < nums.length; i++)
        //     if(nums[i] < min)
        //         min = nums[i];
        // return min;
        int left = 0;
        int right = nums.length-1;
        // O(log n)
        while(left < right){
            int mid = (left+right) / 2;
            if(nums[mid] > nums[right])
                left = mid + 1;
            else
                right = mid;
        }
        return nums[left];
    }
}
