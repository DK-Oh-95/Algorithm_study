def dfs():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(N):
        if num[i] not in ans:
            ans.append(num[i])
            dfs()
            ans.pop()


N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
ans = []
dfs()