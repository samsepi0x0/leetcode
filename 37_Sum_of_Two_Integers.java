class Solution {
    public int getSum(int a, int b) {
        // O(1)
        // return a+b;
        return (b == 0) ? a : getSum(a^b, (a&b) << 1);
    }
}
