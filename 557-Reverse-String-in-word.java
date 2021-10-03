import java.util.StringTokenizer;
class Solution {
    public String reverseWords(String s) {
        String f_s = "";
        StringTokenizer st = new StringTokenizer(s);
        while(st.hasMoreTokens()){
            String r = st.nextToken();
            String temp = "";
            for(int i = r.length() - 1; i >= 0; i--)
                temp += r.charAt(i);
            f_s = f_s + temp + " ";
        }
        return f_s.trim();
    }
}
