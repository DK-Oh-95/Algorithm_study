def dfs(graph, start, distance, dig):
    global longest
    # 현재까지 이동 길이가 최장길이보다 길면 갱신
    if longest < distance:
        longest = distance

    cr, cc = start[0], start[1]
    visited[cr][cc] = 1

    for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        nr, nc = cr + dr, cc + dc
        # 방문 가능하면 방문하고 기록
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if graph[cr][cc] > graph[nr][nc]:
                dfs(graph, (nr, nc), distance + 1, dig)
            # k만큼 파서 갈 수 있으면 경로 재탐색
            elif dig and graph[cr][cc] > graph[nr][nc] - K:
                tmp = graph[nr][nc]
                graph[nr][nc] = graph[cr][cc] - 1
                dfs(graph, (nr, nc), distance + 1, 0)
                graph[nr][nc] = tmp
    visited[cr][cc] = 0


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]

    # 1. 최고높이 찾기
    max_height = 0
    max_height_locations = []
    for i in range(N):
        for j in range(N):
            if max_height < maps[i][j]:
                max_height = maps[i][j]
    # 최고점 위치 찾기
    for i in range(N):
        for j in range(N):
            if max_height <= maps[i][j]:
                max_height_locations.append((i, j))

    # 2. 최고점에서 시작하여 가장 긴 등산로 찾기
    longest = 0
    visited = [[0] * N for _ in range(N)]
    for d in range(len(max_height_locations)):
        dfs(maps, max_height_locations[d], 1, 1)

    print('#{} {}'.format(tc, longest))
