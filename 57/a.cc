#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
using namespace std;

class Solution {
public:
    string longestWord(vector<string>& words) {
        sort(words.begin(), words.end());
        string ans = "";
        for (int i = 0; i < words.size(); i++)
            if (words[i].length() == 1) {
                ans = words[i]; break;
            }
        for (int i = 0; i < words.size(); i++) {
            int len = words[i].length() - 1;
            for (int j = i - 1; j >= 0 && len > 0; j--)
                if (words[j] == words[i].substr(0, len)) 
                    len--;
            if (len == 0) {
                if (words[i].length() > ans.length()) ans = words[i];
                if (words[i].length() == ans.length() &&
                    words[i] < ans) ans = words[i];
            } 
        }
        return ans;
    }
};
