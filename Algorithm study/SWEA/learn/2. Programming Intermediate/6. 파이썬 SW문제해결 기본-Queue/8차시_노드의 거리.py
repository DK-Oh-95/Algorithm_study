def bfs(s, g):
    queue = []
    queue.append((s, 0))  # 시작노드, 거리

    visited = [0] * (V+1)
    visited[s] = 1

    path = []
    path.append(s)

    while queue:
        front, distance = queue.pop(0)
        if front == g:
            return distance
        for i in range(1, V+1):
            if adj[front][i] and not visited[i]:
                queue.append((i, distance+1))
                path.append(i)
                visited[i] = 1
    return 0

T = int(input())
for tc in range(1, T+1):
    # 노드개수 V, 간선개수 E
    V, E = map(int, input().split())
    # 간선 정보
    E_map = [list(map(int, input().split())) for _ in range(E)]
    # 출발 노드 S, 도착노드 G
    S, G = map(int, input().split())

    # 인접행렬 생성
    adj = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        adj[E_map[i][0]][E_map[i][1]] = 1
        adj[E_map[i][1]][E_map[i][0]] = 1

    print('#{} {}'.format(tc, bfs(S, G)))
