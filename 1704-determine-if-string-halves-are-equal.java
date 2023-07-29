class Solution {
    public boolean halvesAreAlike(String s) {
        int c1 = 0;
        int c2 = 0;
        s = s.toLowerCase();
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u'){
                if(i < s.length()/2)
                    c1 += 1;
                else
                    c2 += 1;
            }
        }
        return c1 == c2;
    }
}
