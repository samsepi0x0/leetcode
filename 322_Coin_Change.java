class Solution {
    static int[] DP = new int[10001];;
    public int coinChange(int[] coins, int amount) {
        for(int i = 0; i < DP.length; i++)
            DP[i] = -1;
        int soln = solve(coins, amount);
        if(soln >= (int)1e9)
            return -1;
        return soln;
    }
    public int solve(int[] coins, int amount){
        if(amount == 0)
            return 0;
        if(DP[amount] != -1)
            return DP[amount];
        int ans = (int)1e9;
        for(int x: coins){
            if(x <= amount){
                ans = Math.min(ans, solve(coins, amount-x)+1);
            }
        }
        DP[amount] = ans;
        return ans;
    }
}
