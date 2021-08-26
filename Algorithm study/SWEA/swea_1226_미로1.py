def bfs(sr, sc):
    queue = []
    queue.append((sr, sc))

    visited = [[0] * n for _ in range(n)]
    visited[sr][sc] = 1

    while queue:
        # 처음 큐에서 pop 해서 현재 지점 설정
        cr, cc = queue.pop(0)   # queue 특성 상(FIFO) 처음 자리 가져옴
        # 상우하좌 탐색
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            # 찾은 경로에 3이 있으면 1 반환
            if maze[nr][nc] == '3':
                return 1
            # 상우하좌 탐색한 곳이 정상범위 내부이고,(본 문제에선 벽으로 둘러져 있어서 사실 상 불필요)
            # 갈 수 있는 길이고, 방문하지 않았다면 방문
            if 0 <= nr < n and 0 <= nc < n and maze[nr][nc] == '0' and not visited[nr][nc]:
                queue.append((nr, nc))
                visited[nr][nc] = 1
    return 0  # 전부 참조하여 큐가 비었는데 못 찾았다면 0 반환


T = 10
for _ in range(T):
    tc = int(input())
    n = 16
    maze = [input() for _ in range(n)]

    print('#{} {}'.format(tc, bfs(1, 1)))
