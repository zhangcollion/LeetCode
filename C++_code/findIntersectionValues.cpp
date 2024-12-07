#include<iostream>
#include<vector>
#include<unordered_map>
#include<unordered_set>
using namespace std;
class Solution {
public:
    vector<int> findIntersectionValues(vector<int>& nums1, vector<int>& nums2) {
        unordered_map<int, vector<int>>  nums1Map;
        unordered_map<int, vector<int>>  nums2Map;
        for(int i = 0; i < nums1.size(); i++){
            nums1Map[nums1[i]].push_back(i);
        }
        int ans2 = 0;
        for(int i = 0; i < nums2.size(); i++){
            nums2Map[nums2[i]].push_back(i);
            ans2 += nums1Map.count(nums2[i]);
        }
        int ans1 = 0;
        for(int i = 0; i < nums1.size(); i++){
            ans1 += nums2Map.count(nums1[i]);
        } 
    vector<int> ans;
    ans.push_back(ans1);
    ans.push_back(ans2);
    return ans;
    }
};


int main(){
    vector<int> nums1 = { 4,3,2,3,1};
    vector<int> nums2 = {2,2,5,2,3,6};
    vector<int> ans = Solution().findIntersectionValues(nums1, nums2);
    for(int i = 0; i < ans.size(); i++){
        std::cout << ans[i] << endl;
    }
    
    return 0;
}
