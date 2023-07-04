class Solution { // O(n*n)
    public List<List<Integer>> threeSum(int[] nums) {
       Set<List<Integer>> arr = new HashSet<>();
       if(nums.length == 0) return new ArrayList<>(arr);
       Arrays.sort(nums);
       for(int i = 0; i < nums.length - 2;i++){
           int j = i+1;
           int k = nums.length - 1;
           //System.out.println("#" + i + "\t" + j + "\t" + k);
           while (j < k){
               int sum3 = nums[i] + nums[j] + nums[k];
               if(sum3 == 0){
                   arr.add(Arrays.asList(nums[i], nums[j++], nums[k--]));
               }
               else if (sum3 > 0){
                   k--;
               }
               else{
                   j++;
               }
               //System.out.println(i + "\t" + j + "\t" + k);
           }
       }
       return new ArrayList<>(arr);
    }
}
