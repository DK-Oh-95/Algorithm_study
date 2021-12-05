def solve(r, c, first_r, first_c, cnt, direction):
    global max_cnt
    # 왼쪽 위로 올라오거나 오른쪽 위로 올라오며 사각형 완성되면 반환
    if direction == 3 and r == first_r + 1 and c == first_c - 1:
        if max_cnt < cnt:
            max_cnt = cnt
        return
    if direction == 4 and r == first_r + 1 and c == first_c - 1:
        if max_cnt < cnt:
            max_cnt = cnt
        return

    visited.append(cafes[r][c])
    # 이전 방향을 확인하고 사각형을 만들 수 있는 방향으로 이동
    # direction : 1(우하), 2(좌하), 3(좌상), 4(우상)
    if direction == 1:
        for dr, dc, direct in [[1, 1, 1], [1, -1, 2]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and cafes[nr][nc] not in visited:
                solve(nr, nc, first_r, first_c, cnt + 1, direct)
        visited.pop()
    elif direction == 2:
        for dr, dc, direct in [[1, -1, 2], [-1, -1, 3]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and cafes[nr][nc] not in visited:
                solve(nr, nc, first_r, first_c, cnt + 1, direct)
        visited.pop()
    elif direction == 3:
        for dr, dc, direct in [[-1, -1, 3], [-1, 1, 4]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and cafes[nr][nc] not in visited:
                solve(nr, nc, first_r, first_c, cnt + 1, direct)
        visited.pop()
    elif direction == 4:
        for dr, dc, direct in [[-1, 1, 4]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and cafes[nr][nc] not in visited:
                solve(nr, nc, first_r, first_c, cnt + 1, direct)
        visited.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]

    max_cnt = -1
    for i in range(N-2):
        for j in range(1, N-1):
            visited = []
            solve(i, j, i, j, 1, 1)

    print('#{} {}'.format(tc, max_cnt))
