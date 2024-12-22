#include<iostream>
#include<vector>
#include<numeric>
using namespace std;
class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        vector<int> ans;
        int leftNums = 0; 
        int rightNums = accumulate(nums.begin(), nums.end(),0);
        for(int i = 0; i < nums.size(); i++){
            rightNums -= nums[i];
            ans.push_back(abs(leftNums-rightNums));
            leftNums += nums[i];
        }
        return ans;
    }
};