#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int sumIndicesWithKSetBits(vector<int>& nums, int k) {
        int ans = 0;
        for(int i = 0; i < nums.size(); i++){
            if (getBinary(i)==k){
                ans += nums[i];
            }
        }
        return ans;      
    }
    int getBinary(int num){
        int oneCount = 0;
        while(num != 0){
            oneCount += num%2;
            num = num/2;
        }
        return oneCount;
    }
};

int main(){
    vector<int> nums ={4,3,2,1};// {5,10,1,5,2};
    int k = 2;
    int ans = Solution().sumIndicesWithKSetBits(nums, k);
    std::cout << ans <<endl;
    return 0;

}