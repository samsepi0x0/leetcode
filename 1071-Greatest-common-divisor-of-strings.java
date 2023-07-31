class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if(str1.equals(str2))
            return str1;
        if(!(str1+str2).equals(str2+str1)) // check if s = t + t + .... + t format only
            return "";
        return str1.substring(0, gcd(str1.length(), str2.length())); // substring from 0 to gcd of two lengths of the string.
    }
    public int gcd(int a, int b){
        if(b == 0)
            return a;
        return gcd(b, a % b);
    }
}
