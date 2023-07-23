class Solution {
    public boolean isPalindrome(String s) {
        String ns = ""; // new string
        String rns = ""; // reverse of new string
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(Character.isLetterOrDigit(ch)){
                char ch2;
                if(Character.isUpperCase(ch))
                    ch2 = Character.toLowerCase(ch);
                else
                    ch2 = ch;
                ns = ns + ch2;
                rns = ch2 + rns;
            }
        } 
        return ns.equals(rns);  
    }
}
