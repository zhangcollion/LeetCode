class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        ans = sum(tasks)
        if ans <= sessionTime:
            return 1
        tasks.sort(reverse=True)
        seen = []
        n = len(tasks)
        ans = 0
        ii = 3
        while ii >0  :
            def backtrack(tmp, cur, index):
                if cur > sessionTime:
                    return
                if cur == sessionTime:
                    tmp.sort(reverse=True)
                    res.append(tmp)

                    return
                for i in range(index, n):
                    if i > index and tasks[i] == tasks[i - 1]:
                        continue
                    backtrack(tmp + [tasks[i]], cur + tasks[i], i + 1)

            res = []
            n = len(tasks)
            tasks.sort()
            backtrack([], 0, 0)
            res.sort(reverse=True)
            

            for val in res:
                flag = 1
                info_tasks = Counter(tasks)
                for i in val:
                    info = Counter(val)
                    if i not in tasks or info[i] >info_tasks[i]  :
                        flag = 0
                        break

                if flag == 1:
                    ans+= 1
                    for i in val:
                        tasks.remove(i)
            ii -= 1
        seen = []
        n = len(tasks)
        while len(seen) != n:
            tmp = 0
            for i, val in enumerate(tasks):
                if i not in seen:
                    tmp += val
                    if tmp <= sessionTime:
                        seen.append(i)
                        if tmp == sessionTime:
                            break
                    else:
                        tmp -= val
            ans += 1
        return ans