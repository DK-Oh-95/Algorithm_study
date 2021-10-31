def route(r, c, v):
    # r: 현재 row 좌표
    # c: 현재 column 좌표
    # v: 현재까지 지나온 경로의 값들의 합

    global min_sum

    # 현재 지점이 맨 오른쪽 아래면 return
    if r == N-1 and c == N-1:
        # 지나온 경로들의 합이 최소값보다 작으면 갱신
        if min_sum > v:
            min_sum = v
        return

    # 오른쪽으로 갈 수 있으면 이동
    if c + 1 < N:
        route(r, c + 1, v + arr[r][c+1])
    # 더 이상 오른쪽으로 갈 수 없으면 아래로 이동
    if r + 1 < N:
        route(r + 1, c, v + arr[r+1][c])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_sum = 250
    route(0, 0, arr[0][0])

    print('#{} {}'.format(tc, min_sum))
