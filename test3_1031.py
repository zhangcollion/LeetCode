from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:


if __name__ == "__main__":
    accounts = [["David", "David0@m.co", "David5@m.co", "David0@m.co"],
                ["Lily", "Lily4@m.co", "Lily2@m.co", "Lily0@m.co"], ["Fern", "Fern5@m.co", "Fern2@m.co", "Fern6@m.co"],
                ["Gabe", "Gabe0@m.co", "Gabe6@m.co", "Gabe8@m.co"], ["Alex", "Alex7@m.co", "Alex5@m.co", "Alex7@m.co"],
                ["Lily", "Lily4@m.co", "Lily6@m.co", "Lily7@m.co"], ["Alex", "Alex0@m.co", "Alex4@m.co", "Alex5@m.co"],
                ["John", "John4@m.co", "John2@m.co", "John0@m.co"]]
    # accounts = [["Alex", "Alex7@m.co", "Alex5@m.co", "Alex7@m.co"],["Alex", "Alex0@m.co", "Alex4@m.co", "Alex5@m.co"]]
    print(Solution().accountsMerge(accounts))
