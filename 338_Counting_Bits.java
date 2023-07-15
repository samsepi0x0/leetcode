class Solution {
    public int[] countBits(int n) {
        // O(nlogn)
        int res[] = new int[n+1];
        for(int i = 0; i < res.length; i++){
            int count = 0;
            int index = i;
            for(count = 0; index != 0; count ++){
                index &= (index-1);
            }
            res[i] = count;
        }
        return res;
    }
    public int[] countBits_optimized(int n){
        // O(n)
        int res[] = new int[n+1];
        res[0] = 0;
        for(int i = 1; i < res.length; i++){
            res[i] = res[i >> 1] + (i % 2);
            // divide by 2 and add 0 if even, 1 if odd.
        }
        return res;
    }
}
