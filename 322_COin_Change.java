class Solution {
    static int count = 0;
    public int coinChange(int[] coins, int amount) {
        int soln = solve(coins, amount);
        if(soln == (int)1e4)
            return -1;
        return soln;
    }
    public int solve(int[] coins, int amount){
        if(amount == 0)
            return 0;
        int ans = (int)1e4;
        for(int x: coins){
            if(amount >= x){
                ans = Math.min(ans, solve(coins, amount-x)+1);
            }
        }
        return ans;
    }
}
