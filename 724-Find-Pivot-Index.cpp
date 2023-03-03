class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        /* O(n^2)
        for (int pivot = 0; pivot < nums.size(); pivot ++){
            int ls = 0, rs = 0;
            for(int i = pivot-1; i >= 0; i--){
                ls += nums[i];
            }
            for(int i = pivot+1; i < nums.size(); i++){
                rs += nums[i];
            }
            
            if (ls == rs)
                return pivot;
        }*/
        //O(n)
        int ls = 0;
        int rs = 0;
        for(int i = 0; i < nums.size(); i++)
            rs += nums[i];

        for(int i = 0; i < nums.size(); i++){
            cout << ls << "\t" << i << "\t" << rs  << "\t" << rs - ls - nums[i] << endl;
            if(ls == (rs - ls - nums[i]))
                return i;
            ls += nums[i];
        }
        return -1;
    }
};
