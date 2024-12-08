#include<vector>
using namespace std;
class Solution {
public:
    int numberOfPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        int ans = 0;
        for (int i=0; i < nums1.size(); i++){
            int tmpNums1 = nums1[i];
            for (int j=0; j < nums2.size(); j++){
                if(tmpNums1%(nums2[j]*k) == 0){
                    ans += 1;
                }
            }
        }
        return ans;
    }
};