#include<iostream>
#include<vector>
using namespace std;
class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> ans;
        for(int i=0; i < words.size(); i ++){
            if( words[i].find(x) != std::string::npos){
                ans.push_back(i);
            }
        }
        return ans;
        
    }
};