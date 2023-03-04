class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        long long count = 0;
        int jmin = -1;
        int jmax = -1;
        int jbad = -1;
        for(int i = 0; i < nums.size(); i++){
            if(!(nums[i] >= minK && nums[i] <= maxK))
                jbad = i;
            if(nums[i] == minK)
                jmin = i;
            if(nums[i] == maxK)
                jmax = i;

            count += max(0, min(jmin, jmax) - jbad);
        }
        return count;
    }
};
