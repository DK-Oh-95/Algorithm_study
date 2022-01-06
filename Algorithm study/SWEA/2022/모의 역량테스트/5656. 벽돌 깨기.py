from collections import deque
import copy


def drop_marble(cnt, arr):
    global min_num

    # N번 채울 때까지 반복
    for j in range(W):
        copy_bricks = copy.deepcopy(arr)
        # 구슬 떨어뜨려 벽돌 있으면 파괴
        for i in range(H):
            if arr[i][j]:
                break_bricks(i, j, copy_bricks)
                break
        # 벽돌 없으면
        else:
            tmp_cnt = 0
            for i in range(H):
                for j in range(W):
                    if copy_bricks[i][j]:
                        tmp_cnt += 1
            if not tmp_cnt:
                min_num = 0
                return

        # N회 시행 후 전체 벽돌 개수 최소값과 비교
        if cnt == N:
            tmp_num = 0
            for i in range(H):
                for j in range(W):
                    if arr[i][j]:
                        tmp_num += 1

            if min_num > tmp_num:
                min_num = tmp_num
            return

        remove_blank(arr)
        drop_marble(cnt + 1, copy_bricks)


def break_bricks(cr, cc, arr):
    tmp = arr[cr][cc]
    arr[cr][cc] = 0

    if tmp == 1:
        return
    # 벽돌 숫자만큼 주변 벽돌 파괴
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = cr, cc
        for _ in range(tmp - 1):
            nr, nc = nr + dr, nc + dc
            if 0 <= nr < H and 0 <= nc < W and arr[nr][nc]:
                break_bricks(nr, nc, arr)


# 벽돌 파괴 후 빈 공간 제거
def remove_blank(arr):
    for j in range(W):
        for i in range(H):
            if arr[i][j]:
                q.append(arr[i][j])
                arr[i][j] = 0

        for d in range(len(q)):
            arr[H-1-d][j] = q.pop()


for tc in range(int(input())):
    N, W, H = map(int, input().split())
    bricks = [list(map(int, input().split())) for _ in range(H)]

    min_num = 180
    q = deque()
    drop_marble(0, bricks)

    print('#{} {}'.format(tc+1, min_num))
