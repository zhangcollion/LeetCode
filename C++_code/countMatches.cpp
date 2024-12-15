#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;
class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        unordered_map<string, int> info = {{"type",0}, {"color",1}, {"name",2}};
        int res = 0;
        int index = info[ruleKey];
        for (auto &&item : items) {
            if (item[index] == ruleValue) {
                res++;
            }
        }
        return res;
    }
};