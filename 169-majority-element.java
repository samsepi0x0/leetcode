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
}
