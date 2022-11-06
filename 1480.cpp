class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        if(nums.size() == 1)
            return nums;
        /** time complexity: O(n^2); space complexity: 0(n)
        vector<int> running_sum;
        for(int i = 0; i < nums.size(); i++){
            int sum = 0;
            for(int j = 0; j <= i; j++){
                sum += nums[j];
            }
            running_sum.push_back(sum);
        }
        return running_sum;**/
        /* time omplexity: O(n); space complexity: 0(n)
        vector<int> running_sum;
        running_sum.push_back(nums[0]);
        for(int i = 1; i < nums.size(); i++){
            running_sum.push_back(running_sum.back() + nums[i]);
        }
        return running_sum;
        */
        // time complexity: O(n); space complexity: 0(1)
        for(int i=1; i < nums.size(); i++){
            nums[i] += nums[i-1];
        }
        return nums;
    }
};
