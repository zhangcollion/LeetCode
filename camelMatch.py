from typing import List
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n = len(queries)
        if n == 0 :
            return []
        ans = []

        def is_valid(data, ref):
            i = 0
            j = 0
            idx = ref[i]
            while j < len(data):
                alpha = data[j]
                if alpha.islower() and not idx.islower() :
                    j += 1
                elif alpha.islower() and idx.islower():
                    if alpha != idx:
                        j += 1
                    else:
                        j += 1
                        i += 1
                        if i == len(ref):
                            left = data[j:]
                            if str(left).lower() != str(left):
                                return False
                            else:
                                return True
                        else:
                            idx = ref[i]
                elif not alpha.islower() and not idx.islower():
                    if alpha == idx:
                        j += 1
                        i += 1
                        if i == len(ref):
                            left = data[j:]
                            if str(left).lower() != str(left):
                                return False
                            else:
                                return True
                        else:
                            idx = ref[i]
                    else:
                        return False
                else:
                    return False


            return False

        for i in queries:
            if is_valid(i, pattern):
                ans.append(True)
            else:
                ans.append(False)
        return ans


if __name__ == "__main__":
    # queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    # pattern = "FB"
    queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    pattern = "FoBa"
    print(Solution().camelMatch(queries, pattern))