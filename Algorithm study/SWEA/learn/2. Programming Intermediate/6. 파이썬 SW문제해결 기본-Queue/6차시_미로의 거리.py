def bfs(arr, r, c):
    """
    :param arr: 참조하려는 미로 배열
    :param r: 출발 행
    :param c: 출발 열
    :return:
    """
    queue = []
    queue.append((r, c, 0))  # 시작점 좌표와 시작점에서 떨어진 거리
    visited = [[0] * N for _ in range(N)]  # 방문한 곳인지 확인하기 위한 미로와 동일한 크기 배열
    visited[r][c] = 1  # 시작점 방문
    path = []

    while queue:
        # 현재 지점, 거리
        cr, cc, distance = queue.pop(0)
        path.append((cr, cc, distance))
        # 현재 지점에서 갈 수 있는 경로 탐색 (상우하좌)
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            # 갈 수 있는 다음 좌표
            nr, nc = cr + dr, cc + dc
            # 갈 수 있는 좌표가 정상 범위 안이고, 벽이 아닌 길이고, 방문하지 않았으면 바로 방문
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '0' and not visited[nr][nc]:
                queue.append((nr, nc, distance + 1))
                visited[nr][nc] = 1
            elif 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '3':
                return distance
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]

    # 출발지점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_r = i
                start_c = j

    print('#{} {}'.format(tc, bfs(maze, start_r, start_c)))