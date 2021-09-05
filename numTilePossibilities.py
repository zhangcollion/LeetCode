class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        self.res = 0
        tiles = sorted(tiles)
        seen = [0] *(len(tiles))
        self.tiles = tiles
        self.get_permute([], seen)
        return self.res
    def get_permute(self, tmp, tmp_seen):
        if tmp :
            self.res += 1
        for i in range(0, len(self.tiles)):
            if tmp_seen[i]:
                continue
            else:
                if i > 0 and self.tiles[i] == self.tiles[i-1] and tmp_seen[i-1]==0:
                    continue
                tmp_seen[i] = 1
                self.get_permute( tmp+[self.tiles[i]], tmp_seen)
                tmp_seen[i] = 0