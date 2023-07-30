class Solution {
    public double myPow(double x, int n) {
        double a = 1.0;
        // int pow = Math.abs(n);
        // for(int i = 0; i < pow; i++)
        //     a *= x;
        // return n >= 0 ? a : (1/a); // does not work for -2147483648.
        // return Math.pow(x, n);
        if(n < 0){
            n = -n;
            x = 1 / x;
        }
        while(n != 0){
            if(n % 2 != 0)
                a *= x;

            x *= x;
            n = n / 2;
        }
        return a;
    }
}
