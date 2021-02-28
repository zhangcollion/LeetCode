from typing import List
import collections
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ans = 0
        if not items:
            return 0

        for type_idx, color_idx, name_idx in items:
            if ruleKey == "type":
                if type_idx == ruleValue:
                    ans += 1

            if ruleKey == "color":
                if color_idx == ruleValue:
                    ans += 1

            if ruleKey == "name":
                if name_idx == ruleValue:
                    ans += 1

        return ans