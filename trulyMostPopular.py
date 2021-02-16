class Union:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def union(self, idx1, idx2):
        root1 = self.find(idx1)
        root2 = self.find(idx2)
        if self.rank[root1] < self.rank[root2]:
            self.parent[root2] = root1
        if self.rank[root2] < self.rank[root1]:
            self.parent[root1] = root2

            # ref = [root1, root2]
            # ref.sort()
            # self.parent[ref[0]] = ref[1]

    def find(self, idx):
        if self.parent[idx] != idx:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        if not synonyms:
            return names
        seen = []

        for name_pair in synonyms:
            i, j = name_pair[1:-1].split(",")
            if i not in seen or not seen:
                seen.append(i)
            if j not in seen or not seen:
                seen.append(j)
        k = 0
        seen.sort()
        name_info = dict()
        for i in seen:
            name_info[i] = k
            k += 1
        uf = Union(k)
        uf.rank = list(range(k))
        for name_pair in synonyms:
            i, j = name_pair[1:-1].split(",")
            idx_i = name_info[i]
            idx_j = name_info[j]
            uf.union(idx_i, idx_j)

        for i in range(len(uf.parent)):
            uf.parent[i] = uf.find(i)

        res = collections.defaultdict()
        ans = []
        for name in names:
            i, j = name[0:-1].split("(")
            if i not in seen:
                ans.append(name)
            else:
                valid_name = seen[uf.find(seen.index(i))]
                if valid_name not in res.keys():
                    res[valid_name] = 0
                res[valid_name] = res[valid_name] + int(j)

        for i in res.keys():
            ans.append(i + "(" + str(res[i]) + ")")
        return ans