#include<iostream>
#include<vector>
#include<unordered_set>
using namespace std;
class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        unordered_set wordsSet(words.begin(), words.end());
        unordered_set<string> wordsSeen;
        int ans = 0;
        for (auto w : words){
            string validW = "";
            for(int i = w.size()-1; i >= 0 ; i--){
                validW += w[i];
            }
            if (not w.compare(validW)){
                std::cout << w <<endl;
                continue;
            }
            if((wordsSet.count(validW)>0) and ((wordsSeen.count(w)==0) or (wordsSeen.count(validW)==0))){
                wordsSeen.insert(w);
                wordsSeen.insert(validW);
                ans += 1;
            }
        }
        return ans;

    }
};

int main(){
    vector<string> data = {"cd","ac","dc","ca","zz"};
    int ans = Solution().maximumNumberOfStringPairs(data);
    return ans;
}