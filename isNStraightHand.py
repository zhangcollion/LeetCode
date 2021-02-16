from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        while len(hand) > 0:
           hand.sort()
           start = hand[0]
           hand.remove(start)
           left_list = [start+i for i in range(1, W)]
           for i in left_list:
               if i in hand:
                   hand.remove(i)
               else:
                   return False
        return len(hand) == 0


if __name__=="__main__":
    hand = [1,2,3,4,5]
    W = 4
    print(Solution().isNStraightHand(hand, W))