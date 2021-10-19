def n_queen(r):
    global sum_v, min_v

    # N-1번 행까지 모든 행에 대해 위치를 결정
    # 재귀호출 할 필요 없음
    if r == N:
        if min_v > sum_v:
            min_v = sum_v
        return
    # 현재 최소값이 더 작으면 그냥 반환
    if min_v < sum_v:
        return

    for j in range(N):
        if col[j]:
            continue
        # j번 열 선택할 수 있으면 선택 후 다음 행 결정
        col[j] = 1
        sum_v += arr[r][j]
        n_queen(r + 1)
        # 사용 다하고 표시한거 없애주기
        col[j] = 0
        sum_v -= arr[r][j]


# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 열에 대한 사용가능 여부를 표시하는 배열
    col = [0] * N  # 0이면 사용가능, 1이면 이미 다른 퀸이 놓여짐
    sum_v = 0
    min_v = 1000

    n_queen(0)
    print('#{} {}'.format(tc, min_v))