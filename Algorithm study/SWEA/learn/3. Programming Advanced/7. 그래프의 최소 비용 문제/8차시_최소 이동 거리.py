def dijkstra(start):
    weight = adj[start][:]
    used = {start}
    while len(used) < N:  # 아직 모든 노드 선택 안됐으면
        min_v = INF
        min_idx = -1
        # 현재지점을 기준으로 갈 수 있는 최소비용 노드 선택
        for d in range(N+1):
            if d not in used and min_v > weight[d]:
                min_v = weight[d]
                min_idx = d
        used.add(min_idx)  # 선택한 노드 추가

        # 새로 선택한 노드로 인해 비용이 작아지는 weight 업데이트
        for d in range(N+1):
            if d not in used and weight[d] > adj[min_idx][d] + weight[min_idx]:
                weight[d] = adj[min_idx][d] + weight[min_idx]
    return weight[-1]


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())

    INF = 0xffffff
    adj = [[INF] * (N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w

    print('#{} {}'.format(tc, dijkstra(0)))


"""
3
2 3
0 1 1
0 2 6
1 2 1
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
"""