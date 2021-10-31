def prim(start):
    # 현재 그룹에서 각 노드로 갈 수 있는 가중치를 weight 배열에 저장,
    # 가중치 가장 작은 노드를 선택하면서 그룹과 가중치 업데이트
    weight = [INF] * (V+1)
    weight[start] = 0  # 시작 노드에서 시작노드로 가는 가중치는 0
    group = [0] * (V+1)  # 각 노드가 선택되었는지 표시하는 배열
    result = 0  # MST의 가중치를 저장할 변수

    for _ in range(V+1):
        min_idx = 0
        min_v = INF
        for d in range(V+1):
            if weight[d] < min_v and group[d] == 0:
                min_idx = d
                min_v = weight[d]
        group[min_idx] = 1
        result += weight[min_idx]

        # 새로 추가된 노드에 의해 weight 배열 업데이트
        for d in range(V+1):
            # 지금 추가된 min_idx 노드에서 d 노드로 가는 가중치가 가지고 있던 값보다 작고 그룹에 추가되지 않았으면
            if weight[d] > adj[min_idx][d] and group[d] == 0:
                weight[d] = adj[min_idx][d]

    return result


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    INF = 0xffffff
    adj = [[INF] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
        adj[e][s] = w

    print('#{} {}'.format(tc, prim(0)))
