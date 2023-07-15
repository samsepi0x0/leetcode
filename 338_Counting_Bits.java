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
}
