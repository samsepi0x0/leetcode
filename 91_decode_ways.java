class Solution {
    public int numDecodings(String s) {
        // either i can take 1 variable or two variables at a time to decode. The one variable approach is valid if variable is not 0, two variable when value lies b/w 1 and 26. If 2 variables, then either 1+1 or 2, If three variables then 1 + 2 or 2 + 1, if 4: 2 + 2, 1 + 2 + 1.
       if(s == null || s.length() == 0){
           return 0;
       }
       int dp[] = new int[s.length() + 1];
       dp[0] = 1;
       dp[1] = s.charAt(0) == '0' ? 0 : 1;
       for(int i = 2; i <= s.length(); i++){
           int t1 = Integer.valueOf(s.substring(i-1, i));
           int t2 = Integer.valueOf(s.substring(i-2, i));
        //    System.out.println(t1 + "\t" + t2);
            
           if(t1 >= 1 && t1 <= 9){
            //    System.out.println("here " + t1 + "\t" + i + "\t" + dp[i-1]);
               dp[i] += dp[i-1];
           }
           if(t2 >= 10 && t2 <= 26){
            //    System.out.println("here2 " + t1 + "\t" + i + "\t" + dp[i]);
               dp[i] += dp[i-2];
           }
       }
    //    for(int x: dp){
    //        System.out.print(x + "\t");
    //    }
    //    System.out.println();
        return dp[s.length()];

    }
}
