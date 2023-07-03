class Solution {
    public int search(int[] nums, int target) {
        // O(log n)
        if (nums.length == 1)
            return nums[0] == target ? 0 : -1;
        int l = 0;
        int r = nums.length - 1;

        while (l < r){
            int mid = (l+r) / 2;
            if(nums[mid] > nums[r])
                l = mid + 1;
            else
                r = mid;
        }
        int pivot = l;
        System.out.println(pivot);
        l = 0;
        int r1 = pivot-1;

        while (l <= r1){
            int mid = (l+r1) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target)
                l = mid + 1;
            else
                r1 = mid - 1;
        }
        l = pivot;
        int r2 = nums.length - 1;
        while (l <= r2){
            int mid = (l+r2) / 2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target)
                l = mid + 1;
            else
                r2 = mid - 1;
        }

        return -1;
    }
}
