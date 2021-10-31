def cost(r, c, cost_sum):
    global min_cost
    cost_sum += costs[r][c]

    # 중간에 최소 합보다 커지면 중단
    if min_cost < cost_sum:
        return

    # 마지막 행까지 더했으면 최소합과 비교
    if r == N-1:
        if min_cost > cost_sum:
            min_cost = cost_sum
        return

    # 같은 열 사용 방지
    visited[c] = 1
    for j in range(N):
        # 다음 행의 사용하지 않은 열 사용
        if not visited[j]:
            cost(r+1, j, cost_sum)
    visited[c] = 0  # 사용기록 초기화
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]

    min_cost = 1500
    visited = [0] * N

    for i in range(N):
        cost(0, i, 0)

    print('#{} {}'.format(tc, min_cost))
