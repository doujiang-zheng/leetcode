#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> sub(vector<int>& nums, int i) {
        vector<vector<int>> ret;
        if (i > nums.size()) return ret;
        if (i == nums.size()) {
            ret.push_back(*new vector<int>);
            return ret;
        }
        ret = sub(nums, i + 1);
        vector<vector<int>> ans;
        ans.reserve(ret.size() * 2);
        ans.insert(ans.end(), ret.begin(), ret.end());
        for (int k = 0; k < ret.size(); k++) ret[k].push_back(nums[i]);
        ans.insert(ans.end(), ret.begin(), ret.end());
        return ans;
    }

    vector<vector<int>> subsets(vector<int>& nums) {
        return sub(nums, 0);
    }
};

int main()
{

}