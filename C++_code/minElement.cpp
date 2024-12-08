#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    int minElement(vector<int>& nums) {
        int ans = 10000;
        for(int i : nums){
            int tmpAns = 0 ;
            while(i){
                tmpAns += i%10;
                i = i/10;
            }
            tmpAns += i;
            if(tmpAns < ans){
                ans = tmpAns;
            }
        }
        return ans;
    }
};