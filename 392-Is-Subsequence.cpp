class Solution {
public:
    bool isSubsequence(string s, string t) {
        if (s.length() > t.length())
            return false;
        if (s.length() == 0)
            return true;
        int subs = 0;
        for(int i=0; i<t.length(); i++){
            if(subs <= s.length()-1)
                if(s.at(subs) == t.at(i))
                    subs += 1;
        }
        return subs == s.length();
    }
};
