#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Solution {
public:
    // vector<vector<bool>> palin;

    vector<vector<bool>> palindrome(string s) {
        // cout << s << endl;
        int n = s.length();
        vector<vector<bool>> palin(n, vector<bool>(n, false));
        for (int i = 0; i < n; i++) palin[i][i] = true;
        for (int i = 0; i < n-1; i++) palin[i][i+1] = (s[i] == s[i+1]);
        for (int k = 2; k < n; k++)
            for (int i = 0; i + k < n; i++) {
                int j = i + k;
                palin[i][j] = (s[i] == s[j]) && palin[i+1][j-1];
            }
        return palin;
    }

    int minCut(string s) {
        int n = s.length();
        vector<vector<int>> cnt(n, vector<int>(n, n));
        vector<vector<bool>> palin = palindrome(s);
        
        vector<int> dp(n+1);
        for (int i = 0; i <= n; i++) dp[i] = i;
        for (int i = 1; i <= n; i++)
            for (int j = 0; j < i; j++)
                if (palin[j][i-1]) dp[i] = min(dp[i], dp[j] + 1);
        return dp[n]-1;

        // for (int i = 0; i < n; i++) cnt[i][i] = 0;

        // for (int k = 1; k < n; k++) {
        //     for (int i = 0; i + k < n; i++) {
        //         int j = i + k;
        //         if (palin[i][j]) {
        //             cnt[i][j] = 0;
        //         } else {
        //             for (int it = i + 1; it <= j; it++)
        //                 cnt[i][j] = min(cnt[i][j], cnt[i][it-1] + cnt[it][j] + 1);
        //         }
        //     }
        // }
        // return cnt[0][n-1];
    }
};

int main()
{
    string s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    Solution *sol = new Solution();
    cout << sol->minCut(s) << endl;
}