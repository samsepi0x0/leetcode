class Solution {
public:
    vector<vector<int>> generate(int r) {
        vector<vector<int>>v(r);
        v[0].push_back(1);
        for(int i =1;i<r;i++){
            v[i].push_back(1);
            if(i>=2){
                for(int j = 1;j<i;j++){
                    v[i].push_back(v[i-1][j-1]+v[i-1][j]);
                }
            }
            v[i].push_back(1);
        }
        return v;
    }
};

