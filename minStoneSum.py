class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        ans = sum(piles)
        info = Counter(piles)
        data = list(info.keys())
        while k > 0:
            if data:
                max_data =  max(data)
                if 1 == max_data:
                    return ans
                if info[max_data] >= k:
                    ans -= floor(max_data/2)*k
                    k = 0
                else:
                    ans -= floor(max_data/2)*info[max_data]
                    k -= info[max_data]
                    data.remove(max_data)
                    
                    if max_data-floor(max_data/2) not in info:
                        data.append(max_data-floor(max_data/2))
                        info[max_data-floor(max_data/2)] = info[max_data]
                    else:
                        info[max_data-floor(max_data/2)] += info[max_data]
                    
            else:
                return 0

        return ans