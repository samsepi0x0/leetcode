class Solution {
    public int majorityElement(int[] nums) { // O(n^2)
        int criteria = (int)(nums.length/2);
        for(int i = 0; i < nums.length; i++){
            int freq = 1;
            for(int j = i+1; j < nums.length; j++){
                if(nums[i] == nums[j])
                    freq++;
            }
            if(freq > criteria)
                return nums[i];
        }
        return 0;
    }
    public int majorityElement2(int[] nums) {
        int major=nums[0], count = 1; // O(1) awesome approach.
        for(int i=1; i<nums.length;i++){
            if(count==0){
                count++;
                major=nums[i];
            }else if(major==nums[i]){
                count++;
            }else count--;
            
        }
        return major;
    }
}
