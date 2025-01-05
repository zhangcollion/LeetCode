#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for(int i=0; i < nums.size(); i+=2){
            swap(nums[i+1], nums[i]);
        }

        return nums;
    }
};