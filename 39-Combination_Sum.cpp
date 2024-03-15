class Solution {
public:
    vector<vector<int>> result;
    void solve(vector<int>& candidates, vector<int>& r, int target, int start) {
        int sum = 0;
        for(int i = 0; i < r.size(); i++)
            sum += r[i];
        if (sum == target) {
            result.push_back(r);
            return;
        } else if (sum > target)
            return;
        else {
            for(int i = start; i < candidates.size(); i++){
                r.push_back(candidates[i]);
                solve(candidates, r, target, start);
                r.pop_back();
                start += 1;
            }
        }
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> temp;
        solve(candidates, temp, target, 0);
        return result;
    }
};
