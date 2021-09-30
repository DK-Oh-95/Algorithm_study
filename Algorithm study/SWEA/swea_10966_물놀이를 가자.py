def water(cr, cc):
    ######################## 모든 경우 탐색 (Runtime error)
    # global distance
    # if maps[cr][cc] == 'W':
    #     if distance > cnt:
    #         distance = cnt
    #     return
    #
    # visited[cr][cc] = 1
    #
    # for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    #     nr = cr + dr
    #     nc = cc + dc
    #     if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
    #         water(nr, nc, cnt + 1)
    #
    # visited[cr][cc] = 0

    ######################### bfs (제한시간 초과)
    # queue = []
    # queue.append((cr, cc))
    # visited = [[0] * M for _ in range(N)]
    # visited[cr][cc] = 1
    # distance = 0
    #
    # while queue:
    #     for _ in range(len(queue)):
    #         front = queue.pop(0)
    #
    #         for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
    #             nr = front[0] + dr
    #             nc = front[1] + dc
    #             if 0 <= nr < N and 0 <= nc < M and maps[nr][nc] == 'W':
    #                 distance += 1
    #                 return distance
    #             elif 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
    #                 queue.append((nr, nc))
    #                 visited[nr][nc] = 1
    #     distance += 1

    ########################## 그냥 계산 (제한시간 초과)
    distance = N + M - 2
    min_distance = N + M - 2
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'W':
                distance = abs(cr-i) + abs(cc-j)
            if min_distance > distance:
                min_distance = distance
    return min_distance


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    maps = list(input() for _ in range(N))

    result = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 'L':
                result += water(i, j)

    print('#{} {}'.format(tc, result))
