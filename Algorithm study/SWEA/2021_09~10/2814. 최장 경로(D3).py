def bfs(node, cnt):
    global max_cnt

    if max_cnt < cnt:
        max_cnt = cnt

    visited[node] = 1
    # 방문하지 않은 연결된 노드가 있으면 이동
    for d in range(1, N+1):
        if adj[node][d] and not visited[d]:
            bfs(d, cnt+1)
    visited[node] = 0


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(M)]

    # 인접배열 생성
    adj = [[0] * (N+1) for _ in range(N+1)]
    for i in range(M):
        adj[graph[i][0]][graph[i][1]] = 1
        adj[graph[i][1]][graph[i][0]] = 1

    max_cnt = 0
    visited = [0] * (N+1)
    for i in range(1, N+1):
        bfs(i, 1)
    print('#{} {}'.format(tc, max_cnt))

"""
2
1 0
3 2
1 2
3 2

1
6 5
1 2
1 3
2 4
2 5
2 6

[0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0]
[0, 1, 0, 0, 1, 1, 1]
[0, 1, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 0, 0]
"""