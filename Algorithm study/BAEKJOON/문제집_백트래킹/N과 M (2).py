def dfs():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(1, N+1):
        if i not in ans:
            if ans and ans[-1] > i:
                continue
            ans.append(i)
            dfs()
            ans.pop()


N, M = map(int, input().split())
ans = []
dfs()
