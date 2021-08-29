from typing import List
from collections import defaultdict

minimizeTheDifference
class UnionFind:
    def __init__(self, data):
        self.parent = list(range(len(data)))

    def union(self, idx1, idx2):
        self.parent[self.find(idx1)] = self.find(idx2)

    def find(self, idx):
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts:
            return accounts

        emailtoindex = dict()
        emailtoname = dict()

        for account in accounts:
            name = account[0]
            info = account[1:]
            for i in info:
                if i not in emailtoindex:
                    emailtoindex[i] =  len(emailtoindex)
                    emailtoname[i] = name

        uf = UnionFind(emailtoindex)


        # 将同一名字下的email做一个连通器
        for i in accounts:
            firstindex = emailtoindex[i[1]]
            for email in i[2:]:
                uf.union(firstindex, emailtoindex[email])

        # 找到父节点将所有的子节点归到一类
        # 找到所有节点的父节点然后将email放到同一父节点下
        indexToEmails = defaultdict(list)
        for email, index in emailtoindex.items():
            index = uf.find(index)
            indexToEmails[index].append(email)

        ans = []
        for email in indexToEmails.values():
            ans.append([emailtoname[email[0]]]+ sorted(email))
        return ans








if __name__ == "__main__":
    accounts = [["David", "David0@m.co", "David5@m.co", "David0@m.co"],
                ["Lily", "Lily4@m.co", "Lily2@m.co", "Lily0@m.co"], ["Fern", "Fern5@m.co", "Fern2@m.co", "Fern6@m.co"],
                ["Gabe", "Gabe0@m.co", "Gabe6@m.co", "Gabe8@m.co"], ["Alex", "Alex7@m.co", "Alex5@m.co", "Alex7@m.co"],
                ["Lily", "Lily4@m.co", "Lily6@m.co", "Lily7@m.co"], ["Alex", "Alex0@m.co", "Alex4@m.co", "Alex5@m.co"],
                ["John", "John4@m.co", "John2@m.co", "John0@m.co"]]
    # accounts = [["Alex", "Alex7@m.co", "Alex5@m.co", "Alex7@m.co"],["Alex", "Alex0@m.co", "Alex4@m.co", "Alex5@m.co"]]
    print(Solution().accountsMerge(accounts))
