#include <set>
#include <vector>
#include <string>
#include <iostream>
#include <unordered_map>
using namespace std;


class Solution {
private:
    unordered_map<string, vector<string>> m;
public:
    vector<string> split(string s, set<string>& dict) {
        if (m.count(s) > 0) return m[s];
        vector<string> ans;
        if (dict.count(s) > 0) ans.push_back(s);
        for (int i = 1; i < s.length(); i++) {
            string tmp = s.substr(0, i);
            if (dict.count(tmp) > 0) {
                vector<string> ret = split(s.substr(i), dict);
                for (string str: ret) 
                    ans.push_back(tmp + ' ' + str);
            }
        }
        m[s] = ans;
        return ans;
    }

    vector<string> wordBreak(string s, vector<string>& wordDict) {
        set<string> dict;
        for (string e : wordDict)
            dict.insert(e);
        
        return split(s, dict);
    }
};

int main()
{
    Solution *so = new Solution();
    string s = "catsanddog";
    vector<string> word = {"cat", "cats", "and", "sand", "dog"};
    vector<string> ans = so->wordBreak(s, word);
    for (string s: ans)
        cout << s << endl;
}