#include <string>
#include<iostream>
using namespace std;

class Solution {
public:
    int scoreOfString(string s) {
        int ans = 0 ;
        for (int i = 1; i < s.length(); i++){
            ans += abs(s[i]-s[i-1]);
        }
        return ans;
        
    }
};

int main()
{   string s = "hello";
    int ans = Solution().scoreOfString(s);
    cout << "ans is " << ans << endl;
    return 0;

}