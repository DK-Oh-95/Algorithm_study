def prim(start):
    weight = adj[start][:]
    weight[start] = 0
    used = {start}

    result = 0
    while len(used) < N:
        min_v = INF
        min_idx = -1
        for d in range(N):
            if d not in used and min_v > weight[d]:
                min_v = weight[d]
                min_idx = d
        used.add(min_idx)
        result += weight[min_idx] ** 2

        for d in range(N):
            if d not in used and weight[d] > adj[min_idx][d]:
                weight[d] = adj[min_idx][d]
    return result


for tc in range(int(input())):
    N = int(input())  # 섬의 개수
    x = list(map(int, input().split()))  # 각 섬들의 x좌표
    y = list(map(int, input().split()))  # 각 섬들의 y좌표
    E = float(input())  # 환경 부담 세율

    # 인접 배열 생성
    INF = 0xffffff
    adj = [[INF] * N for _ in range(N)]

    # 각 노드의 가중치 설정
    for i in range(N-1):
        for j in range(i+1, N):
            adj[i][j] = adj[j][i] = ((x[i] - x[j])**2 + (y[i] - y[j])**2)**0.5

    # 최소 신장 트리 생성
    print('#{} {}'.format(tc+1, int(round(prim(0)*E))))

