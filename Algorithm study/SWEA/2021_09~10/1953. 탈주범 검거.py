def location(cr, cc, cnt):
    visited[cr][cc] = 1
    tmp_visited[cr][cc] = 1
    # 소요시간 경과하면 중단
    if cnt == L:
        tmp_visited[cr][cc] = 0
        return

    # 현재위치에서 4방향 탐색해서 갈 수 있으면 이동
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    for i in range(4):
        nr = cr + dr[i]
        nc = cc + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not tmp_visited[nr][nc]:
            # 상 / 현재:(1, 2, 4, 7)이고, 다음:(1, 2, 5, 6)이면 가능
            if i == 0:
                if maps[cr][cc] in [1, 2, 4, 7] and maps[nr][nc] in [1, 2, 5, 6]:
                    location(nr, nc, cnt + 1)
            # 우 / 현재:(1, 3, 4, 5)이고, 다음:(1, 3, 6, 7)이면 가능
            elif i == 1:
                if maps[cr][cc] in [1, 3, 4, 5] and maps[nr][nc] in [1, 3, 6, 7]:
                    location(nr, nc, cnt + 1)
            # 하 / 현재:(1, 2, 5, 6)이고, 다음:(1, 2, 4, 7)이면 가능
            elif i == 2:
                if maps[cr][cc] in [1, 2, 5, 6] and maps[nr][nc] in [1, 2, 4, 7]:
                    location(nr, nc, cnt + 1)
            # 좌 / 현재:(1, 3, 6, 7)이고, 다음:(1, 3, 4, 5)이면 가능
            elif i == 3:
                if maps[cr][cc] in [1, 3, 6, 7] and maps[nr][nc] in [1, 3, 4, 5]:
                    location(nr, nc, cnt + 1)
    tmp_visited[cr][cc] = 0


T = int(input())
for tc in range(1, T+1):
    # N: 세로크기, M: 가로크기, R: 맨홀 세로위치, C: 맨홀 가로위치, L: 소요시간
    N, M, R, C, L = map(int, input().split())
    # 0: 없음, 1: 상하좌우, 2: 상하, 3: 좌우
    # 4: 상우, 5: 하우, 6: 하좌, 7: 상좌
    maps = [list(map(int, input().split())) for _ in range(N)]

    visited = list([0] * M for _ in range(N))
    tmp_visited = list([0] * M for _ in range(N))
    location(R, C, 1)
    # 이동가능한 위치 확인
    result = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                result += 1

    print('#{} {}'.format(tc, result))
