import copy


def make_combination():
    if len(com) == N:
        drop_bead(com)
        return
    for d in range(W):
        com.append(d)
        make_combination()
        com.pop()


def drop_bead(arr):
    global tmp_bricks, min_cnt
    if min_cnt == 0:
        return
    tmp_bricks = copy.deepcopy(bricks)
    # 열 우선순회하여 벽돌 만나면 제거
    for j in arr:
        for i in range(H):
            if tmp_bricks[i][j]:
                remove_brick(i, j)
                # 벽돌 제거 작업이 끝나면 빈공간 없애고 다음 작업
                down_brick()
                break

    # 모든 제거 작업 끝나면 남은 벽돌 개수 확인
    cnt = 0
    for i in range(H):
        for j in range(W):
            if tmp_bricks[i][j]:
                cnt += 1
            # 개수 세는 도중 최소값 넘어가면 중단
            if cnt >= min_cnt:
                return
    # 중간에 중단 안 됐으면 최소값 갱신
    min_cnt = cnt


def remove_brick(r, c):
    global tmp_bricks
    # 해당 벽돌 제거하고 값만큼 상하좌우 제거
    tmp = tmp_bricks[r][c]
    tmp_bricks[r][c] = 0
    if tmp > 1:
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            for k in range(1, tmp):
                nr, nc = r + (dr * k), c + (dc * k)
                if 0 <= nr < H and 0 <= nc < W and tmp_bricks[nr][nc]:
                    remove_brick(nr, nc)


def down_brick():
    global tmp_bricks
    # 뒤에서부터 0 만났을 떄 위에 값 있으면 자리 교환
    for i_1 in reversed(range(1, H)):
        for j_1 in reversed(range(W)):
            if not tmp_bricks[i_1][j_1]:
                for i_2 in reversed(range(1, i_1)):
                    if tmp_bricks[i_2][j_1]:
                        tmp_bricks[i_1][j_1], tmp_bricks[i_2][j_1] = tmp_bricks[i_2][j_1], tmp_bricks[i_1][j_1]


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]
    tmp_bricks = []

    min_cnt = 176
    # 구슬을 떨어트릴 모든 경우 구함
    com = []
    make_combination()

    print('#{} {}'.format(tc, min_cnt))
