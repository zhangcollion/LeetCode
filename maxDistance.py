class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        data = set(colors)
        info = collections.defaultdict(list)
        for i, c in enumerate(colors):
            info[c].append(i)
        
        max_data = 0
        for idx in data:
            start = info[idx][0]
            left_data = data - set([idx])
            for other_idx in left_data:
                end = info[other_idx][-1]
                if end-start > max_data:
                    max_data = end-start
                
        return max_data