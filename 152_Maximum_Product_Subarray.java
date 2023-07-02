class Solution {
    public int maxProduct(int[] nums) {
        // if(nums.length == 1) // O(n^2)
        //     return nums[0];
        // int final_prod = nums[0];
        // for(int i = 0; i < nums.length; i++){
        //     int temp_prod = 1;
        //     for(int j = i; j < nums.length; j++){
        //         temp_prod *= nums[j];
        //         //System.out.println(i + "\t" + j + "\t" + nums.length);
        //         //System.out.println(final_prod + "\t" + temp_prod + "\t" + nums[i] + "\t" + nums[j]);
        //         final_prod = Math.max(temp_prod, final_prod);
        //     }
        // }
        // return final_prod;
        int val = nums[0]; //O(n)
        int imax = nums[0];
        int imin = nums[0];

        for(int i = 1; i < nums.length; i++){
            if (nums[i] < 0){
                int t = imin;
                imin = imax;
                imax = t;
            }

            imax = Math.max(nums[i], nums[i]*imax);
            imin = Math.min(nums[i], nums[i]*imin);

            val = Math.max(imax, val);
        }
        return val;
    }
}
