#include<string>
using namespace std;
class Solution {
public:
    string removeTrailingZeros(string num) {
        int index = num.length()-1;
        for(int i = num.length()-1; i >= 0; i--){
            if((num[i] != '0')){
                index = i;
                break;
            }
        }
        string ans = "";
        for(int i = 0; i <= index; i++){
            ans += num[i];
        }
    return ans;
    }
};