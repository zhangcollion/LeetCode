#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        unordered_map<int,int> ans;
        for(auto i : nums){
            ans[i]++;
        }
        vector<int> result;
        for(auto &[k, v] :ans){
            if(v>1){
                result.push_back(k);
            }
        }
        return result;
    }
};