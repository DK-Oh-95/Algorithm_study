def shift(r, c, move, first_value):
    global max_move
    # 네 방향 탐색해서 1크면 이동
    for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and rooms[nr][nc] == rooms[r][c] + 1:
            used[nr][nc] = 1
            shift(nr, nc, move + 1, first_value)
            break
    # 상하좌우에 현재 값보다 1 큰 값 없으면 이동거리 비교
    else:
        if max_move == move:
            start_points.add(first_value)
        elif max_move < move:
            max_move = move
            for d in range(len(start_points)):
                start_points.pop()
            start_points.add(first_value)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    max_move = 0
    start_points = set()
    used = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not used[i][j]:
                shift(i, j, 1, rooms[i][j])

    print('#{} {} {}'.format(tc, min(start_points), max_move))
