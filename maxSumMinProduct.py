from typing import List
import tensorflow as tf

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms:
            return True

        rooms_num = len(rooms)
        seen = [0]
        dp = [rooms[0]]

        while dp:
            keys = dp.pop()
            for i in keys:
                if i not in seen:
                    seen.append(i)
                    dp.append(rooms[i])

        if len(seen) == rooms_num:
            return True
        else:
            return False


if __name__ == "__main__":
    rooms = [[1], [2], [3], []]
    print(Solution().canVisitAllRooms(rooms))
