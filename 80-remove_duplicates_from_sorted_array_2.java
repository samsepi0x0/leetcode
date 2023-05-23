class Solution {
    public int removeDuplicates(int[] nums) {
       if (nums.length < 2){
           return nums.length;
       } 
       int prev = 1;
       int curr = 2;

       while(curr < nums.length){
           if(nums[curr] == nums[prev] && nums[curr] == nums[prev - 1]){
               curr++;
           } // this is a duplicate and will be overwritten
           else{
               prev++;
               nums[prev] = nums[curr];
               curr++;
           } // shift numbers so that k elements contains the desired array
       }
       return prev + 1;
    }
}
