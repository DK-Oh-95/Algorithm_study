def dfs(sr, sc):
    stack = []
    stack.append((sr, sc))
    # 방문기록 (미로와 같은 크기의 배열)
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    path = []
    path.append((sr, sc))

    # 탐색 방향 : 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    while stack:
        # current_r, current_c : 현재위치
        cr, cc = stack[-1]
        for i in range(4):
            # next_r, next_c : 길이 있는지 검사하려는 좌표
            nr = cr + dr[i]
            nc = cc + dc[i]
            # 경로 탐색 중 3을 만나면 1반환
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] == '3':
                return 1
            elif 0 <= nr < N and 0 <= nc < N and maze[nr][nc] == '0' and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                path.append((nr, nc))
                break
        else:  # 갈 수 있는 경로가 없음
            stack.pop()
    # 미로를 다 탐색했지만 3을 만나지 못하면 0 반환
    return 0


# 테스트케이스
T = int(input())

for tc in range(1, T+1):
    # 미로크기 N
    N = int(input())
    # 미로
    maze = [input() for _ in range(N)]

    # 미로를 순회하면서 출발지 2를 찾아서 출발정점 정함
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_r = i
                start_c = j

    print('#{} {}'.format(tc, dfs(start_r, start_c)))
