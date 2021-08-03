#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <stack>
using namespace std;

// class Solution {
// public:
    vector<string> removeComments(vector<string>& source) {
        const int code = 0, line = 1, block = 2;
        vector<string> ans(source.size(), "");
        int state = code;
        int num = 0;
        for (int i = 0; i < source.size(); i++) {
            int pos = 0;
            while (pos < source[i].length()) {
                int l = source[i].find("//", pos);
                int bb = source[i].find("/*", pos);
                int be = source[i].find("*/", pos);
                
                // cout <<"line: " << i << " pos: " << pos << " state: " << state << endl; 
                switch(state) {
                    case code:
                        if ((l != string::npos && bb != string::npos && l < bb) ||
                            (l != string::npos && bb == string::npos)) {
                                ans[num] += source[i].substr(pos, l - pos); 
                                state = line; pos = l + 2;
                            } else if ((l != string::npos && bb != string::npos && l > bb) ||
                            (l == string::npos && bb != string::npos)) {
                                ans[num] += source[i].substr(pos, bb - pos);
                                state = block; pos = bb + 2;
                            } else if ((l == string::npos && bb == string::npos)) {
                                ans[num] += source[i].substr(pos);
                                state = code; pos = source[i].length();
                            }
                            // cout << ans[i] << endl;
                        break;
                    case line:
                        state = code; pos = source[i].length();
                        break;
                    case block:
                        if (be == string::npos) {
                            state = block; pos = source[i].length();
                        } else {
                            state = code; pos = be + 2;
                        }
                        break;
                    default: break;
                }
                if (state == code && pos >= source[i].length()) num++;
            }
        }
        vector<string> ret;
        for (int i = 0; i < ans.size(); i++)
            if (ans[i].length() > 0) ret.push_back(ans[i]);
        return ret;
    }
// };

int main()
{
    vector<string> input = {"/*Test program*/"};
    removeComments(input);
}