#include <iostream>
#include <vector>
#include <algorithm>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <string>
using namespace std;

// class Solution {
// public:
    int root(vector<int>& parent, int p) {
        if (parent[p] == p) return p;
        return parent[p] = root(parent, parent[p]);
    }

    vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
        vector<string> name(accounts.size());
        for (int i = 0; i < accounts.size(); i++) name[i] = accounts[i][0];
        vector<int> parent(accounts.size());
        for (int i = 0; i < accounts.size(); i++) parent[i] = i;
        map<string, int> email;
        
        for (int i = 0; i < accounts.size(); i++) {
           for (int j = 1; j < accounts[i].size(); j++) {
               if (email.count(accounts[i][j]) > 0) {
                   int idx = email.find(accounts[i][j])->second;
                   if (parent[i] == i)  parent[i] = root(parent, idx);
                    else parent[idx] = root(parent, i);
               } else email[accounts[i][j]] = i;
           }
        }
        int cnt = 0;
        for (int i = 0; i < parent.size(); i++) 
            if (parent[i] == i) cnt++;
            else parent[i] = root(parent, i);
        vector<vector<string>> ans(cnt, vector<string>());
        // ans.resize(cnt, vector<string>());
        map<int, int> mmap;
        for (int i = 0, j = 0; i < parent.size(); i++)
            if (parent[i] == i) {
                mmap[i] = j;
                ans[j++].push_back(name[i]);
            }
        vector<set<string>> tmp(cnt, set<string>());
        for (int i = 0; i < accounts.size(); i++)
            for (int j = 1; j < accounts[i].size(); j++)
                tmp[mmap[root(parent, i)]].insert(accounts[i][j]);
        for (int i = 0; i < cnt; i++)
            for (auto it = tmp[i].begin(); it != tmp[i].end(); it++)
                ans[i].push_back(*it);
        return ans;
    }
// };

int main()
{
    vector<vector<string>> input = {{"David","David0@m.co","David1@m.co"},{"David","David3@m.co","David4@m.co"},{"David","David4@m.co","David5@m.co"},{"David","David2@m.co","David3@m.co"},{"David","David1@m.co","David2@m.co"}};
}