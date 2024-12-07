#include<string>
#include<iostream>
using namespace std;
class Solution {
public:
    int minimumChairs(string s) {
        int ans = 0;
        int validChairs = 0;
        int leftChairs = 0;
        for(int i = 0 ; i < s.length(); i++){
            if((s[i]) == 'E' ){
                if(leftChairs == 0)
                {
                    validChairs += 1;
                }
                else{
                    leftChairs -= 1;
                }
            }
            else{
                leftChairs += 1;
            }

        }
        return validChairs;
    }
};

int main(){
    int ans = Solution().minimumChairs("ELELEEL");
    std::cout<< ans << endl;
    return 0;
}