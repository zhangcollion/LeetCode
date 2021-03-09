from typing import List
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        if not needs:
            return 0
        discard = []
        for packet in special:
            for i in range(len(packet) - 1):
                if packet[i] > needs[i]:
                    discard.append(packet)
                    break
        for i in discard:
            special.remove(i)

        self.ans = float("inf")
        self.get_ans(special, needs, 0, price)
        return self.ans

    def get_ans(self, ref_info, needs, cost, price):
        if sum(needs) == 0:
            self.ans = min(self.ans, cost)
            return
        for ref in ref_info:
            left = [needs[i] - ref[i] for i in range(len(needs))]
            flag = 0
            for i in left:
                if i < 0:
                    flag = 1
                    break
            if 0 == flag:
                self.get_ans(ref_info, left, cost + ref[-1],price)

        tmp = [price[i] * needs[i] for i in range(len(needs))]
        cost += sum(tmp)
        self.ans = min(self.ans, cost)
        return

if __name__ == "__main__":
    p = [2, 5]
    s = [[3, 0, 5], [1, 2, 10]]
    n = [3, 2]
    print(Solution().shoppingOffers(p, s, n))
