def dijkstra(start, arr):  # start: 출발노드, arr: 가중치가 기록된 인접배열
    weight = arr[start][:]  # 출발노드로부터 갈 수 있는 노드들의 가중치 기록한 리스트
    weight[start] = 0
    used = {start}  # 사용한 노드

    while len(used) < N:  # 사용한 노드수가 전체노드 수보다 작으면
        # 출발노드에서 가장 가중치 작은 노드로 이동
        min_v = INF
        min_idx = -1
        for d in range(N+1):
            if d not in used and min_v > weight[d]:
                min_v = weight[d]
                min_idx = d
        used.add(min_idx)  # 해당 노드로 가는 거리를 확정

        for d in range(N+1):
            # 추가되지 않은 노드 중에 출발 노드에서부터의 가중치보다
            # 지금 새로 추가된 노드까지의 가중치와 그 노드로부터의 가중치가 더 작은 노드가 있으면
            # 가중치 업데이트 >> 이 값이 곧 출발노드부터 다른 노드까지의 최소 가중치
            if d not in used and weight[d] > weight[min_idx] + arr[min_idx][d]:
                weight[d] = weight[min_idx] + arr[min_idx][d]
    return weight


for tc in range(int(input())):
    N, M, X = map(int, input().split())  # N: 집 수, M: 도로 수, X: 목표집

    INF = 0xffffff
    adj = [[INF] * (N+1) for _ in range(N+1)]  # 목표집에서 각 집으로 가는 거리
    ajd = [[INF] * (N+1) for _ in range(N+1)]  # 거꾸로 하면 각 집에서 목표집으로 오는 거리

    for _ in range(M):
        s, e, w = map(int, input().split())
        adj[s][e] = w
        ajd[e][s] = w

    departure = dijkstra(X, adj)  # 2번 노드에서 각 노드로 가는 최소 가중치
    arrival = dijkstra(X, ajd)  # 각 노드에서 2번 노드로 오는 최소 가중치
    # 출발 노드를 제외하고 각 노드의 왕복 거리(합) 구함
    max_dist = 0
    for i in range(1, N+1):
        dist = departure[i] + arrival[i]
        if max_dist < dist:
            max_dist = dist

    print("#{} {}".format(tc+1, max_dist))
