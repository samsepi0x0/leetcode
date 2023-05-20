class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0; // to keep track of all elements that are not equal to val.
        for(int j = 0; j < nums.length; j++) { // iterate the array
            if (nums[j] != val){ // if its a valid number
                int temp = nums[i]; //swap it with the last known valid number
                nums[i] = nums[j];
                nums[j] = temp;
                i ++; // increase counter to 1
            }
        }   
        return i; // return index till where numbers are proper.
    }
}
