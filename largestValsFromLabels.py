class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        ans  = []
        dict_info = defaultdict(list)
        for idx, value in enumerate(values):
            dict_info[labels[idx]].append(value)
        for i, v in dict_info.items():
            v.sort(reverse=True)
            if len(v) < use_limit:
                ans.extend(v)
            else:
                ans.extend(v[:use_limit])
        ans.sort(reverse=True)
        if ans:
            return(sum(ans[:num_wanted]))
        else:
            return 0