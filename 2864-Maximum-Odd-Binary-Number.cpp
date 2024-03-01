class Solution {
public:
    string maximumOddBinaryNumber(string s) {
        // Optimized.
        int N = s.length();
        vector<char> newS(N, '0');
        bool first = false;
        int left = 0;
        for(int i = 0; i < N; i++) {
            if (s[i] == '1') {
                if (!first) {
                    newS[N-1] = '1';
                    first = true; 
                } else {
                    newS[left++] = '1';
                }
            }
        }
        string S(newS.begin(), newS.end());
        return S;
    }
};
