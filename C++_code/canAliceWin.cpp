#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    bool canAliceWin(vector<int>& nums) {
        int ans1 = 0;
        int ans2 = 0 ;
        for (auto i : nums){
            if(i >= 10){
                ans2 += i;
            }
            else{
                ans1 += i;
            }
        }
        return ans1 != ans2;
    }
};