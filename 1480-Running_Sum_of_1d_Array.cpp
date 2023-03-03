class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> sum;
        /* O(n^2)
        for(int i = 0;i < nums.size(); i++){
            int temp = 0;
            for(int j = 0; j <= i; j++){
                temp += nums[j];
            }
            sum.push_back(temp);
        }*/
        // O(n)
        sum.push_back(nums[0]);
        for(int i = 1; i < nums.size(); i++){
            sum.push_back(sum[i-1] + nums[i]);
        }
        return sum;
    }
};
