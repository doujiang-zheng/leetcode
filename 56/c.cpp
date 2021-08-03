#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        // vector<int> 
        // vector< int > last(B.size())
        vector< int > vis(B.size(), 0);
        // for (int i = 0; i < A.size(); i++)
        //     vis[i] = *new vector<int>(B.size(), 0);
        // for (int i = 0; i < A.size(); i++)
        //     vis[i][0] = A[i] == B[0] ? 1 : 0;
        for (int j = 0; j < B.size(); j++)
            vis[j] = A[0] == B[j] ? 1 : 0;
        int mmax = 0;
        for (int i = 0; i < B.size(); i++)
            mmax = max(mmax, vis[i]);
        for (int i = 1; i < A.size(); i++) {
            // for (int j = 0; j < B.size(); j++)
            //     vis[j] = A[i] == B[j] ? 1 : 0;
            vis[0] = A[i-1] == B[0] ? 1 : 0;
            for (int j = B.size() - 1; j >= 1; j--) {
                if (A[i] == B[j])
                    vis[j] = vis[j-1] + 1;
                else
                    vis[j] = 0;
                mmax = max(mmax, vis[j]);
            }
        }
        // for (int i = 0; i < A.size(); i++)
        //     for (int j = 0; j < B.size(); j++)
        //         mmax = max(mmax, vis[i][j]);
        return mmax;
    }
};