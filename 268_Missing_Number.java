class Solution {
    public int missingNumber(int[] nums) {
  // O(N)
        int sum = 0;
        int n = nums.length;
        for(int i = 0; i < n; i++)
            sum += nums[i];
        return (int)((n*(n+1)) / 2) - sum;
    }
}
