def dfs(r, c, percentage_multi):
    global max_percentage
    percentage_multi *= (percentage[r][c] / 100)

    # 현재까지 곱이 최대곱보다 작으면 리턴
    if max_percentage > percentage_multi:
        return

    # 중간에 0이 곱해지면 중단
    if not percentage_multi:
        return

    # 마지막 행까지 곱했으면 최소합과 비교
    if r == N-1:
        if max_percentage < percentage_multi:
            max_percentage = percentage_multi
        return

    # 같은 열 사용 방지
    visited[c] = 1
    for j in range(N):
        # 다음 행의 사용하지 않은 열 사용
        if not visited[j]:
            dfs(r+1, j, percentage_multi)
    visited[c] = 0  # 사용기록 초기화
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    percentage = [list(map(int, input().split())) for _ in range(N)]

    max_percentage = 0
    visited = [0] * N

    for i in range(N):
        dfs(0, i, 1)

    print('#{} {:.6f}'.format(tc, max_percentage * 100))
