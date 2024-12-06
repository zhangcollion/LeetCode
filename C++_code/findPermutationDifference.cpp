#include<iostream>
#include<algorithm>
#include<string>
#include<unordered_map>
using namespace std;
class Solution {
public:
    int findPermutationDifference(string s, string t) {
        unordered_map<char, int>  data_map;
        int ans = 0;
        for(int i=0; i<s.length(); i++){
            data_map[s[i]] = i;
        }
        for(int i=0; i<t.length();i++){
            ans += abs(i - data_map[t[i]]);
        }
        return ans;
    }
};

int main(){
    // string s = "abc";
    // string t = "bac";
    string s = "rwohu";
    string t = "rwuoh";
    int so = Solution().findPermutationDifference(s, t);
    cout << so << endl;

}
