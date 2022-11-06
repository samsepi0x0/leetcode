# include<numeric>
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        // time complexity: O(n); space complexity: 0(1)
        int sum = 0;
        int left_sum = 0;
        for(int i=0; i<nums.size(); i++)
            sum += nums[i];
        for(int i=0; i<nums.size(); i++){
            if (left_sum == sum - left_sum - nums[i])
                return i;
            left_sum += nums[i];
        }
        return -1;
    }
};
