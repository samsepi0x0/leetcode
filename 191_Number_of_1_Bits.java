public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int r = 0;
        for(r = 0; n != 0; r++){
            n &= (n-1);
        }
        return r;
    }
}
